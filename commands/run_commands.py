# ShellCommands_ = ShellCommands( 
#     'python Makeplots_gql_gKK_Intime_Compile_plot.py --MODE 2DPlot  --standalone "Run/Common/TF.py" ' ,
#     8,
#     noptions = -1,
# )
# ShellCommands_.AddOptions(["161718"],"y",)
# ShellCommands_.AddOptions(["V18"],"Temp",)
# ShellCommands_.AddOptions([
#     # "SR1a",
#     # "SR1b",
#     # "SR2a",
#     # "SR2b",
#     # "SR3a",
#     # "SR3b",
#     # "SR23a",
#     # "SR23b",
#     # "SR4a",
#     # "SR4b",
#     "SR2ra",
#     "SR2rb",
#     "SR3ra",
#     "SR3rb",
#     "SR23ra",
#     "SR23rb",
# ],"REGION",)
# ShellCommands_.AddOptions(["V3"],"Temp12",)
# ShellCommands_.AddOptions(["20","21","30","31"],"Temp31",)
# # ShellCommands_.AddOptions(["30",],"Temp31",)
# ShellCommands_.CreateScripts("TF_plots_",)



if "1" in args:
    ShellCommands_ = ShellCommands( 
        'python backup/Antonis/Makeplots_gKK_Intime_Compile_plot_TF.py  --MODE COMP ' ,
        1,
        noptions = -1,
    )
    ShellCommands_.AddOptions(["V33"],"Version",)
    # ShellCommands_.AddOptions(["1","2","3","4"],"Temp",)
    # ShellCommands_.AddOptions(["1","2","3","4","5","6","7","8"],"Temp",)
    # ShellCommands_.AddOptions(["1","2","5","6",],"Temp",)
    ShellCommands_.AddOptions(["2",],"Temp",)
    ShellCommands_.AddOptions(["MassSB",],"CRVersion",)
    # ShellCommands_.AddOptions(["1","2","3","4","5","6","7",],"Temp2",)
    ShellCommands_.AddOptions([
        # "16",
        # "17",
        # "18",
        "161718"
    ],"y",)
    ShellCommands_.AddOptions([
        # "SR1_1a","SR1_2a",
        # "SR2_1a","SR2_2a",
        # "SR3_1a","SR3_2a",
        # "SR4_1a","SR4_2a","SR4_3a",
        # "SR4_1b","SR4_2b","SR4_3b",
        "VR4_1a","VR4_2a","VR4_3a",
        "VR4_1b","VR4_2b","VR4_3b",
    ],"REGION",)
    # ShellCommands_.AddOptions([
    #     "pol1","pol2","pol3","pol4","pol5",
    #     # "pol6","pol7",
    #     # "pol8","pol9",
    # ],"func",)
    # ShellCommands_.AddOptions([
    #     # "1",
    #     # "2",
    #     "3",
    #     # "4",
    # ],"Bin",)
    ShellCommands_.CreateScripts("AA_TF_",)


if "3" in args:
    ShellCommands_ = ShellCommands( 
        'python Makeplots_gql_gKK_Intime_Compile_plot.py --MODE MCvsDATA --REGION PS3 --standalone "Run/Limit/LimitShape.py" ' ,
        1,
        noptions = 1,
    )
    ShellCommands_.AddOptions([
        # "Limit_V33",
        "Limit_V36",
        # "Limit_V50",
    ],"Temp3",)
    ShellCommands_.AddOptions(["161718"],"y",)
    # ShellCommands_.AddOptions(["V27"],"Temp",)
    ShellCommands_.AddOptions([
        # "bR4_1a",'bR4_2a','bR4_3a',
        # "bR4_4a",'bR4_5a',
        # "bR4_1b",'bR4_2b','bR4_3b',
        # "bR4_4b",'bR4_5b'
        "SR4_1a",'SR4_2a','SR4_3a',
        "SR4_4a",'SR4_5a',
        "SR4_1b",'SR4_2b','SR4_3b',
        "SR4_4b",'SR4_5b'
        # "VR4_1a",'VR4_2a','VR4_3a',
        # "VR4_4a",'VR4_5a',
        # "VR4_1b",'VR4_2b','VR4_3b',
        # "VR4_4b",'VR4_5b',
    ],"Temp1",)
    ShellCommands_.AddOptions([
        "invar_m",
        # "MJJ_bin2",
        # "MJJ_or",
        # "DPhi_ac","DEta_ac",
        # "PTj_a","PTj_a",
        # "MET"
        # "MR_mer",
    ],"Temp2",)
    ShellCommands_.AddOptions(["MassSB"],"Temp6",)
    ShellCommands_.AddOptions(["QCD","QCD_MUp","QCD_MDn","Top",],"Temp4",)
    # ShellCommands_.AddOptions(["Top",],"Temp4",)
    # ShellCommands_.AddOptions(["1","2","3","4"],"Temp5",)
    ShellCommands_.AddOptions(["2"],"Temp5",)
    # ShellCommands_.AddOptions(["1","2"],"Temp5",)
    ShellCommands_.CreateScripts("Shape_plots_",)

if "2" in args:
    ShellCommands_ = ShellCommands(
        'python Tool/limit/limit.py ',
        6,
        noptions = -1,
    )
    # ShellCommands_.AddOptions(["Pre_PostFit"],"action",)
    # ShellCommands_.AddOptions(["PrepareInput"],"action",)
    ShellCommands_.AddOptions(["gof"],"action",)
    # ShellCommands_.AddOptions(["impact"],"action",)
    # ShellCommands_.AddOptions(["impact","gof"],"action",)
    # ShellCommands_.AddOptions(["Pre_PostFit_MC"],"action",)
    ShellCommands_.AddOptions(["Limit_V362_y161718",],"version",)
    ShellCommands_.AddOptions(["V1"],"subversion",)
    ShellCommands_.AddOptions([
        "\"['SR4_1a','SR4_2a','SR4_3a','SR4_4a','SR4_5a','SR4_1b','SR4_2b','SR4_3b','SR4_4b','SR4_5b']\"",
        # "\"['VR4_1a','VR4_2a','VR4_3a','VR4_4a','VR4_5a','VR4_1b','VR4_2b','VR4_3b','VR4_4b','VR4_5b']\"",
        # "\"['SR4_1a']\"",
        # "\"['SR4_2a']\"",
        # "\"['SR4_3a']\"",
        # "\"['SR4_4a']\"",
        # "\"['SR4_5a']\"",
        # "\"['SR4_1b']\"",
        # "\"['SR4_2b']\"",
        # "\"['SR4_3b']\"",
        # "\"['SR4_4b']\"",
        # "\"['SR4_5b']\"",

        # "\"['bR4_1a']\"",
        # "\"['bR4_2a']\"",
        # "\"['bR4_3a']\"",
        # "\"['bR4_4a']\"",
        # "\"['bR4_5a']\"",
        # "\"['bR4_1b']\"",
        # "\"['bR4_2b']\"",
        # "\"['bR4_3b']\"",
        # "\"['bR4_4b']\"",
        # "\"['bR4_5b']\"",

        # "\"['VR4_1a']\"",
        # "\"['VR4_2a']\"",
        # "\"['VR4_3a']\"",
        # "\"['VR4_4a']\"",
        # "\"['VR4_5a']\"",
        # "\"['VR4_1b']\"",
        # "\"['VR4_2b']\"",
        # "\"['VR4_3b']\"",
        # "\"['VR4_4b']\"",
        # "\"['VR4_5b']\"",
    ],"regions",)

    ShellCommands_.CreateScripts("pre_postfit_",)


if "4" in args:
    ShellCommands_ = ShellCommands( 
        'python Makeplots_gql_gKK_Intime_Compile_plot.py --MODE MCvsDATA --REGION PS2 --standalone "Run/MER/PS/DVM/DVM.py" ' ,
        1,
        noptions = 2,
    )
    ShellCommands_.AddOptions(["V33",],"Temp",)
    ShellCommands_.AddOptions(["161718"],"y",) 
    ShellCommands_.AddOptions([
        "MJJ_star",
        ],"Temp1",)
    ShellCommands_.AddOptions([
        "VerySlimmedTree",
        # "Full",
    ],"Temp2",)
    ShellCommands_.AddOptions([
        # "SR1_1b",
        # "SR1_2b",
        "CR1_1",
        "CR1_2",
        # "SR1_Tmp",
    ],"Temp3",)
    # ShellCommands_.AddOptions(["1","2","3","4"],"Temp41",)
    ShellCommands_.AddOptions(["5","6","7","8"],"Temp41",)
    # ShellCommands_.AddOptions(["BDTR"],"Temp31",)
    # ShellCommands_.AddOptions(["1"],"Temp32",)
    # ShellCommands_.AddOptions(["1","2","3","4","5","6","7","8","9","10","11"],"Temp33",)
    # ShellCommands_.AddOptions(["1","2","3","4","5","6",],"Temp33",)
    ShellCommands_.CreateScripts("MER_PS_DVM_",)

if "5" in args:
    ShellCommands_ = ShellCommands( 
        'python Makeplots_gql_gKK_Intime_Compile_plot.py --MODE MCvsDATA --REGION PS2 --standalone "Run/RES/PS/DVM/DVM.py" ' ,
        6,
        noptions = -1,
    )
    ShellCommands_.AddOptions(["V32"],"Temp",)
    ShellCommands_.AddOptions([
        # "MJJ",
        # "MJJJ",
        "PNetWa",
        "PNetWb",
        "Mj_Pneta",
        "Mj_Pnetb",
    ],"Temp2",)
    # ShellCommands_.AddOptions(["16","17","18","161718"],"y",)
    ShellCommands_.AddOptions(["161718"],"y",)
    ShellCommands_.AddOptions([
        "VR4_1a","VR4_2a","VR4_3a",
        "VR4_1b","VR4_2b","VR4_3b",
        "VCR4_1a","VCR4_2a","VCR4_3a",
        "VCR4_1b","VCR4_2b","VCR4_3b",
        # "CR4_1a","CR4_2a","CR4_3a",
        # "CR4_1b","CR4_2b","CR4_3b",
    ],"Temp1",)
    ShellCommands_.CreateScripts("RES_PS_DVM",)

if "6" in args:
    ShellCommands_ = ShellCommands( 
        'python backup/V3/Makeplots_gKK_Intime_Compile_plot.py --y 161718 ' ,
        6,
        noptions = -1,
    )
    ShellCommands_.AddOptions([
        # "MCvsDATA",
        # "COMP",
        "2DPlot",
    ],"MODE",)
    ShellCommands_.AddOptions([
        # "VR4_1a","VR4_1b",
        # "VR4_2a","VR4_2b",
        # "VR4_3a","VR4_3b",
        "VCR4_1a","VCR4_1b",
        "VCR4_2a","VCR4_2b",
        "VCR4_3a","VCR4_3b",
        # "VR4_1a","VR4_2a","VR4_3a",
    ],"REGION",)
    # ShellCommands_.AddOptions(["16","17","18","161718"],"y",)
    # ShellCommands_.AddOptions(["161718"],"y",)
    # ShellCommands_.AddOptions(["VR4_1a",],"Temp1",)
    ShellCommands_.CreateScripts("RES_PS_DVM",)

if "7" in args:
    ShellCommands_ = ShellCommands( 
        'python Makeplots_gql_gKK_Intime_Compile_plot.py --MODE 2DPlot --REGION PS3 --standalone "Run/Limit/UN/UN.py" ' ,
        5,
        noptions = -1,
    )
    # ShellCommands_.AddOptions(["161718"],"y",)
    ShellCommands_.AddOptions([
        "161718",
        # "16","17","18"
    ],"y",)
    ShellCommands_.AddOptions(["V18"],"Temp",)
    ShellCommands_.AddOptions([
        "SR4_1a","SR4_2a",
        "SR4_3a","SR4_4a","SR4_5a",
        "SR4_1b","SR4_2b",
        "SR4_3b","SR4_4b","SR4_5b",
        # "VR4_1a","VR4_2a",
        # "VR4_3a","VR4_4a","VR4_5a",
        # "VR4_1b","VR4_2b",
        # "VR4_3b","VR4_4b","VR4_5b",
        # "PS3",
    ],"Temp1",)
    ShellCommands_.AddOptions(["MJJJ_MR"],"Temp2",)
    ShellCommands_.AddOptions(["Limit_V362"],"Temp3",)
    ShellCommands_.AddOptions([
        # "muF",
        # "yields",
        # "PDF",
        "JEC",
        "JER",
    ],"Temp4",)
    ShellCommands_.CreateScripts("UN_plots_",)

if "10" in args:
    ShellCommands_ = ShellCommands( 
        'python Makeplots_gql_gKK_Intime_Compile_plot.py --MODE 2DPlot --REGION PS3 --standalone "Run/Limit/UN/UN.py" ' ,
        8,
        noptions = 1,
    )
    ShellCommands_.AddOptions(["161718"],"y",)
    ShellCommands_.AddOptions(["V18"],"Temp",)
    ShellCommands_.AddOptions([
        # "SR4_1a",
        # "SR4_2a",
        # "SR4_3a",
        # "SR4_4a",
        # "SR4_5a",
        # "SR4_1b",
        # "SR4_2b",
        # "SR4_3b",
        # "SR4_4b",
        # "SR4_5b",
    ],"Temp1",)
    ShellCommands_.AddOptions(["MJJJ_MR"],"Temp2",)
    ShellCommands_.AddOptions(["Limit_V332"],"Temp3",)
    ShellCommands_.AddOptions([
        "PDF",
    ],"Temp4",)
    ShellCommands_.AddOptions([str(i) for i in range(72)],"Temp5",)
    ShellCommands_.CreateScripts("UN_plots_",)


if "8" in args:
    ShellCommands_ = ShellCommands( 
        'python Makeplots_gql_gKK_Intime_Compile_plot.py --MODE MC --REGION PS2 --standalone "Run/Common/MC.py" ' ,
        8,
        noptions = 1,
    )
    ShellCommands_.AddOptions([
        "CR4_1a","CR4_2a","CR4_3a","CR4_4a","CR4_5a",
        "CR4_1b","CR4_2b","CR4_3b","CR4_4b","CR4_5b",
        # "SR4_1a","SR4_3a",
        # "SR4_5a","SR4_5b",
        # "SR4V2_1a","SR4V2_3a","SR4V2_5a",
    ],"Temp3",)
    ShellCommands_.AddOptions(["V43",],"Temp",)
    ShellCommands_.AddOptions([
        # "16","17","18",
        # "18"
        "161718",
    ],"y",)
    ShellCommands_.AddOptions([
        # "MJJJ_star","MJJ_corr",
        # "MJJJ_star",
        "Mass50",
        # "BDTgc","BDTRHa","BDTRLa",
        # "Etaj_a","Etaj_c",
        # "Mj_a","Mj_b",
        # "Mj_Pneta","Mj_Pnetb","Mj_Pnetc",
        # "PartNet_MD_W_Pneta","PartNet_MD_W_Pnetb","PartNet_MD_W_Pnetc",
        # "MET",
        # "BDTL","BDTH","BDTH2"
        # "MJJ_MJJJ_Ratio",
        ],"Temp1",)
    ShellCommands_.AddOptions([
        "VerySlimmedTree",
        # "Full",
        ],"Temp2",)
    ShellCommands_.AddOptions(["V3"],"Temp41",)
    ShellCommands_.AddOptions(["1",],"Temp42",)
    ShellCommands_.AddOptions(["90","95","85"],"Temp43",)
    ShellCommands_.AddOptions(["50","45","55"],"Temp45",)
    ShellCommands_.CreateScripts("MER_PS_MC_",)

if "9" in args:
    print "test"
    ShellCommands_ = ShellCommands( 
        'python Makeplots_gql_gKK_Intime_Compile_plot.py --MODE 2DFromTable --standalone "Run/Limit/Table_2D.py" ' ,
        8,
        noptions = -1,
    )
    ShellCommands_.AddOptions([
        "\"['SR4_1a','SR4_2a','SR4_3a','SR4_4a','SR4_5a','SR4_1b','SR4_2b','SR4_3b','SR4_4b','SR4_5b']\"",
        # "\"['SR4_1a']\"",
        # "\"['SR4_2a']\"",
        # "\"['SR4_3a']\"",
        # "\"['SR4_4a']\"",
        # "\"['SR4_5a']\"",
        # "\"['SR4_1b']\"",
        # "\"['SR4_2b']\"",
        # "\"['SR4_3b']\"",
        # "\"['SR4_4b']\"",
        # "\"['SR4_5b']\"",
        # "\"['VR4_1a']\"",
        # "\"['VR4_2a']\"",
        # "\"['VR4_3a']\"",
        # "\"['VR4_4a']\"",
        # "\"['VR4_5a']\"",
        # "\"['VR4_1b']\"",
        # "\"['VR4_2b']\"",
        # "\"['VR4_3b']\"",
        # "\"['VR4_4b']\"",
        # "\"['VR4_5b']\"",
    ],"Temp13",)
    ShellCommands_.AddOptions([
        # "10", # muF
        # "8", # PDF
        "11", # JEC
        "12", # JER
        "7", # Limit
        ],"Temp",)
    ShellCommands_.AddOptions(["V1"],"Temp12",)
    ShellCommands_.AddOptions(["Limit_V362_y161718",],"Temp11",)
    ShellCommands_.CreateScripts("UN__",)

if "11" in args:
    ShellCommands_ = ShellCommands( 
        'python Tool/limit/limit.py --action RunInjection ' ,
        12,
        noptions = 3,
    )
    ShellCommands_.AddOptions(["V1"],"subversion",)
    ShellCommands_.AddOptions(list([str(i) for i in range(0,1)]),"TmpID",)
    # ShellCommands_.AddOptions(["0",],"TmpID",)
    ShellCommands_.AddOptions([
        "0",
        "0.2",
        "0.6", 
        "1",
        "3",
        "5", 
        ],"Injection_Strength",)
    ShellCommands_.AddOptions([
        "\"['SR4_1a','SR4_2a','SR4_3a','SR4_4a','SR4_5a','SR4_1b','SR4_2b','SR4_3b','SR4_4b','SR4_5b','bR4_1a','bR4_2a','bR4_3a','bR4_4a','bR4_5a','bR4_1b','bR4_2b','bR4_3b','bR4_4b','bR4_5b']\"",
        # "\"['SR4_1a']\"",
        # "\"['SR4_2a']\"",
        # "\"['SR4_3a']\"",
        # "\"['SR4_4a']\"",
        # "\"['SR4_5a']\"",
        # "\"['SR4_1b']\"",
        # "\"['SR4_2b']\"",
        # "\"['SR4_3b']\"",
        # "\"['SR4_4b']\"",
        # "\"['SR4_5b']\"",
    ],"regions",)
    ShellCommands_.AddOptions(["Limit_V362_y161718",],"version",)
    # ShellCommands_.AddOptions(["True",],"skipdone",)
    # ShellCommands_.AddOptions(["True",],"SkipCreateRFile",)
    ShellCommands_.AddOptions(["50",],"NToy",)
    # ShellCommands_.AddOptions(list([str(i) for i in range(0,10)]),"DirID",)
    # ShellCommands_.AddOptions(list([str(i) for i in range(10,18)]),"DirID",)
    # ShellCommands_.AddOptions(list([str(i) for i in range(30,40)]),"DirID",)
    ShellCommands_.AddOptions(list([str(i) for i in range(840,880)]),"DirID",)
    ShellCommands_.AddOptions(["1"],"mask_channels")
    ShellCommands_.AddOptions(["Injection_ScaleBKG10"],"AddLines")
    ShellCommands_.CreateScripts("UN__",)

if "12" in args:
    ShellCommands_ = ShellCommands( 
        'python Tool/limit/limit.py --action Run --skipdone True ' ,
        1,
        noptions = 3,
    )
    ShellCommands_.AddOptions(["V1"],"subversion",)
    ShellCommands_.AddOptions([
        "\"['SR4_1a','SR4_2a','SR4_3a','SR4_4a','SR4_5a','SR4_1b','SR4_2b','SR4_3b','SR4_4b','SR4_5b']\"",
        # "\"['SR4_1a','SR4_1b']\"",
        # "\"['SR4_2a','SR4_2b']\"",
        # "\"['SR4_3a','SR4_3b']\"",
        # "\"['SR4_4a','SR4_4b']\"",
        # "\"['SR4_5a','SR4_5b']\"",
    ],"regions",)
    ShellCommands_.AddOptions(["Limit_V362_y161718",],"version",)
    ShellCommands_.CreateScripts("UN__",)

# cp /eos/user/q/qiguo/ROOTFILE/GKK/FullTree/UL161718/V3/PKUTree_gKK_2500_2250_161718.root /eos/user/q/qiguo/ROOTFILE/GKK/VerySlimmedTree/UL161718/V3/PKUTree_gKK_2500_2250_161718.root


if "13" in args:
    ShellCommands_ = ShellCommands( 
        'python backup/Antonis/V5/Makeplots_gKK_Intime_Compile_plot.py  --MODE COMP ' ,
        1,
        noptions = -1,
    )
    ShellCommands_.AddOptions(["V35"],"Version",)
    # ShellCommands_.AddOptions(["1","2","3","4"],"Temp",)
    # ShellCommands_.AddOptions(["1","2","3","4","5","6","7","8"],"Temp",)
    # ShellCommands_.AddOptions(["1","2","5","6",],"Temp",)
    # ShellCommands_.AddOptions(["2",],"Temp",)
    # ShellCommands_.AddOptions(["MassSB",],"CRVersion",)
    # ShellCommands_.AddOptions(["1","2","3","4","5","6","7",],"Temp2",)
    ShellCommands_.AddOptions([
        # "16",
        # "17",
        # "18",
        "161718"
    ],"y",)
    ShellCommands_.AddOptions([
        "SR1a","SR2a","SR3a","SR4a","SR5a",
        "SR1b","SR2b","SR3b","SR4b","SR5b",
    ],"REGION",)
    # ShellCommands_.AddOptions([
    #     "pol1","pol2","pol3","pol4","pol5",
    #     # "pol6","pol7",
    #     # "pol8","pol9",
    # ],"func",)
    # ShellCommands_.AddOptions([
    #     # "1",
    #     # "2",
    #     "3",
    #     # "4",
    # ],"Bin",)
    ShellCommands_.CreateScripts("AA_COMP_",)

if "14" in args:
    ShellCommands_ = ShellCommands( 
        'python backup/Antonis/V5/Makeplots_gKK_Intime_Compile_plot.py  --MODE 2DPlot ' ,
        1,
        noptions = -1,
    )
    ShellCommands_.AddOptions(["V36"],"Version",)
    # ShellCommands_.AddOptions(["1","2","3","4"],"Temp",)
    # ShellCommands_.AddOptions(["1","2","3","4","5","6","7","8"],"Temp",)
    # ShellCommands_.AddOptions(["1","2","5","6",],"Temp",)
    # ShellCommands_.AddOptions(["2",],"Temp",)
    # ShellCommands_.AddOptions(["MassSB",],"CRVersion",)
    # ShellCommands_.AddOptions(["1","2","3","4","5","6","7",],"Temp2",)
    ShellCommands_.AddOptions([
        # "16",
        # "17",
        # "18",
        "161718"
    ],"y",)
    ShellCommands_.AddOptions([
        "PS",
        "SR1a","SR2a","SR3a","SR4a","SR5a",
        "SR1b","SR2b","SR3b","SR4b","SR5b",
    ],"REGION",)
    # ShellCommands_.AddOptions([
    #     "pol1","pol2","pol3","pol4","pol5",
    #     # "pol6","pol7",
    #     # "pol8","pol9",
    # ],"func",)
    # ShellCommands_.AddOptions([
    #     # "1",
    #     # "2",
    #     "3",
    #     # "4",
    # ],"Bin",)
    ShellCommands_.CreateScripts("AA_2DPlot_",)

if "15" in args:
    ShellCommands_ = ShellCommands( 
        'python backup/Antonis/V5/Makeplots_gKK_Intime_Compile_plot.py  --MODE MC ' ,
        1,
        noptions = -1,
    )
    ShellCommands_.AddOptions(["V37"],"Version",)
    # ShellCommands_.AddOptions(["1","2","3","4"],"Temp",)
    # ShellCommands_.AddOptions(["1","2","3","4","5","6","7","8"],"Temp",)
    # ShellCommands_.AddOptions(["1","2","5","6",],"Temp",)
    # ShellCommands_.AddOptions(["2",],"Temp",)
    # ShellCommands_.AddOptions(["MassSB",],"CRVersion",)
    # ShellCommands_.AddOptions(["1","2","3","4","5","6","7",],"Temp2",)
    ShellCommands_.AddOptions([
        # "16",
        # "17",
        # "18",
        "161718"
    ],"y",)
    ShellCommands_.AddOptions([
        "PS",
        "SR1a","SR2a","SR3a","SR4a","SR5a",
        "SR1b","SR2b","SR3b","SR4b","SR5b",
    ],"REGION",)
    # ShellCommands_.AddOptions([
    #     "pol1","pol2","pol3","pol4","pol5",
    #     # "pol6","pol7",
    #     # "pol8","pol9",
    # ],"func",)
    # ShellCommands_.AddOptions([
    #     # "1",
    #     # "2",
    #     "3",
    #     # "4",
    # ],"Bin",)
    ShellCommands_.CreateScripts("AA_2DPlot_",)

if "16" in args:
    '''
    python Makeplots_gKK_Intime_Compile_plot_DECO.py --MODE DECO --REGION SR1a --y 18 --signal1 2500_500 &
    python Makeplots_gKK_Intime_Compile_plot_DECO.py --MODE DECO --REGION SR1b --y 18 --signal1 2500_500 &
    python Makeplots_gKK_Intime_Compile_plot_DECO.py --MODE DECO --REGION SR2a --y 18 --signal1 2500_850 &
    python Makeplots_gKK_Intime_Compile_plot_DECO.py --MODE DECO --REGION SR2b --y 18 --signal1 2500_850 &
    python Makeplots_gKK_Intime_Compile_plot_DECO.py --MODE DECO --REGION SR3a --y 18 --signal1 2500_1250 &
    python Makeplots_gKK_Intime_Compile_plot_DECO.py --MODE DECO --REGION SR3b --y 18 --signal1 2500_1250 &
    python Makeplots_gKK_Intime_Compile_plot_DECO.py --MODE DECO --REGION SR4a --y 18 --signal1 2500_1650 &
    python Makeplots_gKK_Intime_Compile_plot_DECO.py --MODE DECO --REGION SR4b --y 18 --signal1 2500_1650 &
    python Makeplots_gKK_Intime_Compile_plot_DECO.py --MODE DECO --REGION SR5a --y 18 --signal1 2500_2000 &
    python Makeplots_gKK_Intime_Compile_plot_DECO.py --MODE DECO --REGION SR5b --y 18 --signal1 2500_2000 &
    '''

if "17" in args:
    '''
    cd /eos/user/q/qiguo/gKK/limit/CMSSW_10_2_13/src
    cmsenv
    cd /eos/user/q/qiguo/www/GKK/Limit/Limit_V362_y161718/V1_VR4_3a/AllGKK/GKK_3000_180
    text2workspace.py /eos/user/q/qiguo/www/GKK/Limit/Limit_V362_y161718/V1_VR4_3a/AllGKK/GKK_3000_180/datacard.tmp -o /eos/user/q/qiguo/www/GKK/Limit/Limit_V362_y161718/V1_VR4_3a/AllGKK/GKK_3000_180/workspace.root > /eos/user/q/qiguo/www/GKK/Limit/Limit_V362_y161718/V1_VR4_3a/AllGKK/GKK_3000_180/spacew.log 2>&1
    combine -M GoodnessOfFit --algo=saturated -d /eos/user/q/qiguo/www/GKK/Limit/Limit_V362_y161718/V1_VR4_3a/AllGKK/GKK_3000_180/workspace.root -D data_obs --fixedSignalStrength 0 --bypassFrequentistFit  -n data_obs >>/eos/user/q/qiguo/www/GKK/Limit/Limit_V362_y161718/V1_VR4_3a/AllGKK/GKK_3000_180/gof.1.log 2>&1
    combine -M GoodnessOfFit --algo=saturated -d /eos/user/q/qiguo/www/GKK/Limit/Limit_V362_y161718/V1_VR4_3a/AllGKK/GKK_3000_180/workspace.root --fixedSignalStrength 0 -t 500 --toysFrequentist --bypassFrequentistFit  -n toys500 >>/eos/user/q/qiguo/www/GKK/Limit/Limit_V362_y161718/V1_VR4_3a/AllGKK/GKK_3000_180/gof.2.log 2>&1

    rm /eos/user/q/qiguo/www/GKK/Limit/Limit_V362_y161718/V1_VR4_5b/Impact/

    python /afs/cern.ch/work/q/qiguo/public/gKK/plot/v5/Tool/scripts/Limit/code/gof/plot.py
    '''

if "None" in args:
    '''
# plot injection
python Tool/Make_PPTX/Make_table.py --pptxname "/eos/user/q/qiguo/www/gKK/plots/Table.pptx" --PATH "/eos/user/q/qiguo/www/GKK/Limit/Limit_V362_y161718/V1_SR4_1a_SR4_2a_SR4_3a_SR4_4a_SR4_5a_SR4_1b_SR4_2b_SR4_3b_SR4_4b_SR4_5b/Bias_Mean/"
python Tool/Make_PPTX/Make_table.py --pptxname "/eos/user/q/qiguo/www/gKK/plots/Table.pptx" --PATH "/eos/user/q/qiguo/www/GKK/Limit/Limit_V362_y161718/V1_SR4_1a_SR4_2a_SR4_3a_SR4_4a_SR4_5a_SR4_1b_SR4_2b_SR4_3b_SR4_4b_SR4_5b/Mean/"

# retrive for table

    '''

if "None" in args:
    '''
# 2D limit

# XS interpolation
python Makeplots_gql_gKK_Intime_Compile_plot.py --MODE 2DFromTable --standalone "Run/Limit/Table_2D.py" --Temp 4 --Temp22 2 --Temp23 50

# signal strength uppper limit
python Makeplots_gql_gKK_Intime_Compile_plot.py --MODE 2DFromTable --standalone "Run/Limit/Table_2D.py" --Temp 7 --Temp22 2 --Temp13 "['SR4_1a','SR4_2a','SR4_3a','SR4_4a','SR4_5a','SR4_1b','SR4_2b','SR4_3b','SR4_4b','SR4_5b']" --Temp12 V1 --Temp11 Limit_V362_y161718 --Temp21 table_Step4 --Temp23 1

python Makeplots_gql_gKK_Intime_Compile_plot.py --MODE 2DFromTable --standalone "Run/Limit/Table_2D.py" --Temp 7 --Temp22 1 --Temp13 "['SR4_1a','SR4_2a','SR4_3a','SR4_4a','SR4_5a','SR4_1b','SR4_2b','SR4_3b','SR4_4b','SR4_5b']" --Temp12 V1 --Temp11 Limit_V362_y161718 --Temp21 table_Step4 --Temp23 0

# cross section uppper limit
python Makeplots_gql_gKK_Intime_Compile_plot.py --MODE 2DFromTable --standalone "Run/Limit/Table_2D.py" --Temp 702 --Temp22 2 --Temp13 "['SR4_1a','SR4_2a','SR4_3a','SR4_4a','SR4_5a','SR4_1b','SR4_2b','SR4_3b','SR4_4b','SR4_5b']" --Temp12 V1 --Temp11 Limit_V362_y161718 --Temp21 table_Step4 --Temp23 500

python Tool/limit/Plot_1DLimit.py --Version Limit_V362_y161718 --ratios "[0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.85]"

python Tool/limit/Plot_1DLimit.py --Version Limit_V362_y161718 --ratios "[0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85]"

python Tool/limit/Plot_1DLimit.py --Version Limit_V362_y161718 --ratios "[0.5]"
    '''
