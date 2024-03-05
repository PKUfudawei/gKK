from itertools import product
import os,sys
import time

ScritpsTorun_Global = []

class ShellCommands():
    def __init__(self,python,nrun,noptions=1,ScriptsPostfix="", InitRun = True, ):
        self.python         = python
        self.define_year()
        self.nrun           = nrun # nrun for one shell
        self.noptions       = noptions # noptions for different scripts 
        self.InitRun        = InitRun # Init Run on one cluster only runs one job in case takes a long time to run several in parallel

        self.Options            = []
        self.Options_Name       = []
        self.Options_Value_Loop = [] # options values in this list will be corrsponding to different scripts
        self.jobs               = []

        self.Clusters()
        self.HOSTNAME_TORUN = []

        self.ScritpsTorun = []
        self.ScriptsPostfix = ScriptsPostfix

    def define_year(self,):
        self.year = ""
        if "--y 16" in self.python      : self.year = "16"
        if "--y 17" in self.python      : self.year = "17"
        if "--y 18" in self.python      : self.year = "18"
        if "--y 161718" in self.python  : self.year = "161718"

    def Clusters(self,):
        self.HOSTNAMES = []
        with open("HOSTNAME.sh","r") as f :
            for i in f.readlines():
                if len(i.rstrip()) > 0 :
                    if "#" not in i :
                        # print i
                        self.HOSTNAMES.append({
                            "HOSTNAME" : "lxplus%s"%(i.rstrip()),
                            "valid"    : True,
                        })
        HostS = os.listdir("RUN_Status")
        for i in self.HOSTNAMES : 
            if i["HOSTNAME"] in HostS : i["valid"] = False

    def GetClusterName(self,):
        self.WhichRun = getattr(self,"WhichRun",0)
        for i in range(self.WhichRun,len(self.HOSTNAMES)) :
            if self.HOSTNAMES[i]["valid"] : 
                self.WhichRun += 1
                return self.HOSTNAMES[i]["HOSTNAME"]
            self.WhichRun += 1

    def AddOptions(self,Loop,options_name):
        Options = [ i[0] for i in self.Options ]
        if options_name not in Options :
            self.Options.append( (options_name,Loop) )
        self.Options_Name      = [ i[0] for i in self.Options ]
        
    def Jobs(self):
        # simple job will be like : [("Temp1","1"),("Temp2","1"),("Temp3","3")]
        Options_Name  = self.Options_Name
        Options_Value = [ i[1] for i in self.Options ]
        for ijob in product(*Options_Value):
            job = zip(Options_Name,ijob)
            self.Options_Value_Loop.append(ijob[:self.noptions])
            self.jobs.append(job)
        self.Options_Value_Loop = list(set(self.Options_Value_Loop))

    def SplitList(self,list_,Nperrun):
        return [ list_[i:i+Nperrun] for i in range(0,len(list_),Nperrun) ]

    def ScriptsName(self,prefix,name_list,postfix):
        to_remove = ['"',"'","[","]"," ","-",","]
        param = "_".join(name_list)
        for i in to_remove:
            param = param.replace(i,"")
        return "%s%s_%s.%s"%(prefix,self.year,param,postfix)

    def GetJobs(self,options_Values):
        jobs = []
        for j in self.jobs:
            ioptions_name = [ q[1] for q in j ]
            if list(ioptions_name[:self.noptions]) == list(options_Values):
                jobs.append(j)
        return jobs

    def ShellCommands(self,scripts,parameters):
        self.NotFirstCommands = getattr(self,"NotFirstCommands",[])
        if len(self.NotFirstCommands) == 0 :
            write_mode = "w"
            self.NotFirstCommands = [1]
        else:
            write_mode = "a+"
        if not type(parameters) == type(["1"]) : parameters = [parameters,]

        HOSTNAME = self.GetClusterName()
        ScriptsName = "RUNSCRIPS/%s.sh"%(
            HOSTNAME
        )
        with open(ScriptsName,"w") as f:
            # print HOSTNAME
            print "sh %s %s"%( scripts, " ".join(parameters) )
            # cmd_clipboard = "echo 'sh %s %s' | nc -C localhost 8197"%( scripts, " ".join(parameters) ) 
            # os.system(cmd_clipboard)
            self.ScritpsTorun.append( "sh %s %s"%( scripts, " ".join(parameters) ) )
            f.write(
                "sh %s %s\n"%( scripts, " ".join(parameters) )
            )

        return "sh %s %s"%( scripts, " ".join(parameters) )

    def Reset_NOptions(self,):
        if self.noptions == -1 :
            self.noptions = len(self.Options_Name)

    def CreateScripts(self,Scripts_prefix):
        self.Scripts_prefix = Scripts_prefix
        self.Reset_NOptions()
        self.Jobs()
        cmd_clipboard = ""
        for j in self.Options_Value_Loop:
            jobs    = self.GetJobs(j)
            scripts = self.ScriptsName("Run/"+self.Scripts_prefix,j,"sh")
            jobs_   = self.SplitList(jobs, self.nrun)
            content = "#!/bin/bash\n"
            for index,ijobs in enumerate(jobs_):
                icontent_1 = '''
set -o errexit
if [ "$1" = "{icommand}" ];then
starttime=`date +'%Y-%m-%d %H:%M:%S'`
start_seconds=$(date --date="$starttime" +%s);
commands_REPLACE_1
endtime=`date +'%Y-%m-%d %H:%M:%S'`
end_seconds=$(date --date="$endtime" +%s);
echo "Init run time:"$((end_seconds-start_seconds))"s"
fi
                '''.format(icommand=str(index))
                if len(ijobs) > 1:
                    icontent_1 = '''
if [ "$1" = "{icommand}" ];then
starttime=`date +'%Y-%m-%d %H:%M:%S'`
start_seconds=$(date --date="$starttime" +%s);
commands_REPLACE_1
if [ $? -eq 0 ]; then
commands_REPLACE_2
endtime=`date +'%Y-%m-%d %H:%M:%S'`
end_seconds=$(date --date="$endtime" +%s);
echo "Init run time:"$((end_seconds-start_seconds))"s"
for i in $(seq 7200);
do
    npython=`ps aux|grep -o python|wc -l`
    endtime=`date +'%Y-%m-%d %H:%M:%S'`
    end_seconds=$(date --date="$endtime" +%s);
    echo -ne "nrun:"$npython";runtime:"$((end_seconds-start_seconds))"s\\r"
    if [ $i -gt 60 ]
    then
    if [ $npython -lt 3 ]
    then
    echo "sh "$0" "$1" run for : "$((end_seconds-start_seconds))"s"
    break
    fi
    fi
    sleep 1s 
done
else
    exit 1
fi
fi
                    '''.format(icommand=str(index))
                icontent_2 = ""
                icontent_3 = ""
                for jobindex,ijob in enumerate(ijobs) :
                    options_  = " ".join([ "--%s %s"%(iop[0],iop[1]) for iop in ijob ])
                    ops_value = [ iop[1] for iop in ijob ]
                    if ( jobindex == 0 ) & ( self.InitRun ) :  
                        debug     = "> %s 2>&1 ; "%(self.ScriptsName("debug_folder/${HOSTNAME}"+self.Scripts_prefix,ops_value,"debug")  )
                    else:
                        debug     = "> %s 2>&1 & "%(self.ScriptsName("debug_folder/${HOSTNAME}"+self.Scripts_prefix,ops_value,"debug")  )
                    icmd = '{python} {options_} {debug} \n'.format(
                        python   = self.python,
                        options_ = options_,
                        debug    = debug,
                    )
                    if ( jobindex == 0 ) & ( self.InitRun ) : 
                        icontent_2 += icmd
                    else:
                        icontent_3 += icmd
                content += icontent_1.replace( "commands_REPLACE_1", icontent_2 ).replace("commands_REPLACE_2",icontent_3)
                cmd_clipboard += self.ShellCommands( scripts, str(index) )+";"

            with open(scripts,"w") as f:
                f.write(content)
        cmd_clipboard_run = "echo '%s' | nc -C localhost 8197"%( cmd_clipboard ) 
        # os.system(cmd_clipboard_run)
        # time.sleep(1)
        global ScritpsTorun_Global
        ScritpsTorun_Global += self.ScritpsTorun 

    def CreateScripts_Temp(self,ScriptsPostfix):
        with open("/eos/user/q/qiguo/www/gKK/temp%s.sh"%(ScriptsPostfix),"w") as f:
            self.ScritpsTorun.sort()
            for i in self.ScritpsTorun:
                f.write("%s \n"%(i))
        

from optparse import OptionParser
parser = OptionParser()
parser.add_option('--ScriptsPostfix', action="store",type="string",dest="ScriptsPostfix" ,default="")
(options, args) = parser.parse_args()

cmd_clipboard_split = "echo '==============================' | nc -C localhost 8197" 
# os.system(cmd_clipboard_split)
# time.sleep(1.1)

LogInClusters = None

Run = "/afs/cern.ch/work/q/qiguo/public/gKK/plot/v5/./commands/run_commands.py"
ScriptsPostfix = options.ScriptsPostfix
with open(Run,"r") as f:
    exec(f.read())
ScritpsTorun = ShellCommands_.ScritpsTorun

sys.path.append(
    os.path.abspath('.')
) 
from Tool.Assign_Cluster_Tasks.Assign_Cluster_Tasks import *

ClusterTasks_ = ClusterTasks(
    LogInClusters = LogInClusters,
    commands = ScritpsTorun_Global,
)
ClusterTasks_.F_CreateRunShs()

# ShellCommands_.CreateScripts_Temp(ScriptsPostfix)
