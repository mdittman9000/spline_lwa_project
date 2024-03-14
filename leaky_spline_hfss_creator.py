# ----------------------------------------------
# Script Recorded by Ansys Electronics Desktop Version 2023.2.0
# 14:38:14  Feb 10, 2024
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("spline-lwa-2024")
oDesign = oProject.SetActiveDesign("curve-fit-13-slow-wave-taper-no-pmc")
oEditor = oDesign.SetActiveEditor("3D Modeler")

# Width of spline in mm
dx = 30

# Thickness of spline in mm
h = 2

# Input num of slots
slot_num = 30

# Original spline, dir 2, curve-fit-13, h = 2, er = 2.87
#y1_arr = [1.242,3.151,5.125,7.172,9.299,11.515,13.828,16.242,18.763,21.392,24.125,26.953,29.86,32.824,35.818,38.815,41.79,49.13,55.427,61.105,66.409,71.5,76.495,81.49,86.576,91.852,97.432,103.462,110.133,117.675,120.673,123.658,126.607,129.501,132.327,135.074,137.736,140.312,142.801,145.205,147.526]
#z1_arr = [1.543682926,3.856750966,6.115861279,8.309664647,10.42423046,12.44579906,14.35734722,16.136705,17.76181917,19.20622192,20.44143925,21.43962767,22.1759801,22.6327109,22.8023064,22.68944143,22.31007549,20.326882,17.59331596,14.479763,11.16243526,7.739627907,4.277977086,0.832761746,-2.541086695,-5.778716348,-8.786939264,-11.42020633,-13.43096307,-14.3838349,-14.33779552,-14.0399089,-13.49309015,-12.70866389,-11.70355205,-10.49904775,-9.11752978,-7.579671823,-5.905394669,-4.110976715,-2.210114686]

#node_point_y = [0,4.358909211,9.102612816,14.30513684,20.04050729,26.33866451,33.05411201,39.92158047,46.63045823,53.04661229,59.15335383,65.01308259,70.71794326,76.36066548,82.00836953,87.73264656,93.61714511,99.73333701,106.1311997,112.8053743,119.6529992,126.4630597,132.9973564,139.1150706,144.7895668,150]
#node_point_z = [8.29034E-17,5.243459572,10.23913442,14.7382921,18.49220018,21.23655205,22.65220514,22.58910531,21.1628067,18.72638681,15.61163995,12.05878376,8.261295196,4.374639125,0.494806439,-3.271591336,-6.785671833,-9.880285586,-12.35381956,-13.93651752,-14.37681145,-13.51868462,-11.43695969,-8.323780696,-4.427667842,0]

# Full fab spline, Curve-fit-13, h=2, er = 2.87
y1_arr = [16.224,18.154,20.207,22.398,24.736,27.229,29.876,32.664,35.564,38.535,45.953,52.131,57.594,62.626,67.397,72.019,76.582,81.162,85.838,90.701,95.865,101.482,107.754,114.879,117.764,120.532,123.156,125.626,127.941,130.11,132.145]
z1_arr = [1.582400387,3.879553003,6.065048849,8.114633853,9.992579111,11.65905713,13.06778191,14.17207874,14.93311257,15.33085688,14.82619013,13.03113243,10.62743045,7.898471139,4.98727851,1.982427733,-1.053933461,-4.064671733,-6.989582259,-9.750549534,-12.22786283,-14.21545755,-15.3287233,-14.84137868,-14.02691118,-12.87406318,-11.42367034,-9.722143201,-7.816155505,-5.744583735,-3.539275311]

node_point_y = [15,19.8,24.6,29.4,34.2,39,43.8,48.6,53.4,58.2,63,67.8,72.6,77.4,82.2,87,91.8,96.6,101.4,106.2,111,115.8,120.6,125.4,130.2,135]
node_point_z = [9.22632E-16,5.65248,9.89184,12.84096,14.62272,15.36,15.17568,14.19264,12.53376,10.32192,7.68,4.73088,1.59744,-1.59744,-4.73088,-7.68,-10.32192,-12.53376,-14.19264,-15.17568,-15.36,-14.62272,-12.84096,-9.89184,-5.65248,0]


# Original spline, Curve-fit-13, h=2, er = 2.87
#y1_arr = [1.242,3.151,5.125,7.172,9.299,11.515,13.828,16.242,18.763,21.392,24.125,26.953,29.86,32.824,40.452,46.954,52.686,57.908,62.791,67.454,71.986,76.458,80.932,85.469,90.13,94.984,100.115,105.622,111.626,118.255,125.6,128.516,131.367,134.141,136.833,139.439]
#z1_arr = [1.543682926,3.856750966,6.115861279,8.309664647,10.42423046,12.44579906,14.35734722,16.136705,17.76181917,19.20622192,20.44143925,21.43962767,22.1759801,22.6327109,22.51280267,21.06097082,18.88745198,16.29871197,13.4612027,10.4746496,7.405363358,4.303702146,1.213220325,-1.824021905,-4.758469584,-7.52767077,-10.04573031,-12.18229364,-13.7361665,-14.39439675,-13.70831006,-13.00337893,-12.07157683,-10.93332915,-9.609812299,-8.123013843]

#node_point_y = [0,4.358909211,9.102612816,14.30513684,20.04050729,26.33866451,33.05411201,39.92158047,46.63045823,53.04661229,59.15335383,65.01308259,70.71794326,76.36066548,82.00836953,87.73264656,93.61714511,99.73333701,106.1311997,112.8053743,119.6529992,126.4630597,132.9973564,139.1150706,144.7895668,150]
#node_point_z = [8.29034E-17,5.243459572,10.23913442,14.7382921,18.49220018,21.23655205,22.65220514,22.58910531,21.1628067,18.72638681,15.61163995,12.05878376,8.261295196,4.374639125,0.494806439,-3.271591336,-6.785671833,-9.880285586,-12.35381956,-13.93651752,-14.37681145,-13.51868462,-11.43695969,-8.323780696,-4.427667842,0]

# Curve-fit-12, h = 3, er = 2.87, full fab
#y1_arr = [16.224,18.154,20.207,22.398,24.736,27.229,29.876,32.664,35.564,43.18,49.459,54.932,59.914,64.589,69.075,73.458,77.811,82.2,86.692,91.371,96.338,101.732,107.73,114.507,117.404,120.189,122.832,125.322,127.656,129.843,131.894,133.821]
#z1_arr = [1.582400387,3.879553003,6.065048849,8.114633853,9.992579111,11.65905713,13.06778191,14.17207874,14.93311257,15.24701027,13.94187326,11.88202264,9.421521582,6.731696841,3.911481328,1.027321016,-1.869886715,-4.73088,-7.498679651,-10.10148411,-12.42618334,-14.28379954,-15.32701714,-14.91899147,-14.14959275,-13.03748072,-11.62228824,-9.949743336,-8.067539497,-6.01490959,-3.825307747,-1.525968792]

#node_point_y = [15,19.8,24.6,29.4,34.2,39,43.8,48.6,53.4,58.2,63,67.8,72.6,77.4,82.2,87,91.8,96.6,101.4,106.2,111,115.8,120.6,125.4,130.2,135]
#node_point_z = [9.22632E-16,5.65248,9.89184,12.84096,14.62272,15.36,15.17568,14.19264,12.53376,10.32192,7.68,4.73088,1.59744,-1.59744,-4.73088,-7.68,-10.32192,-12.53376,-14.19264,-15.17568,-15.36,-14.62272,-12.84096,-9.89184,-5.65248,0]

# Full Fab data
# The input date
#y1_arr = [16.224,18.154,20.207,22.398,24.736,27.229,29.876,32.664,40.346,46.747,52.287,57.284,61.93,66.35,70.632,74.846,79.052,83.308,87.678,92.235,97.074,102.317,108.115,114.599,121.736,124.291,126.69,128.938,131.045,133.022]
#z1_arr = [1.582400387,3.879553003,6.065048849,8.114633853,9.992579111,11.65905713,13.06778191,14.17207874,15.39600393,14.6589539,12.97214985,10.78098435,8.299873807,5.646812106,2.896566866,0.10266599,-2.689013224,-5.432473712,-8.074637724,-10.54193066,-12.72418337,-14.4364351,-15.35184893,-14.90036451,-12.25302209,-10.68334338,-8.884399665,-6.898991391,-4.763388835,-2.508350328]

#node_point_y = [15,19.8,24.6,29.4,34.2,39,43.8,48.6,53.4,58.2,63,67.8,72.6,77.4,82.2,87,91.8,96.6,101.4,106.2,111,115.8,120.6,125.4,130.2,135]
#node_point_z = [9.22632E-16,5.65248,9.89184,12.84096,14.62272,15.36,15.17568,14.19264,12.53376,10.32192,7.68,4.73088,1.59744,-1.59744,-4.73088,-7.68,-10.32192,-12.53376,-14.19264,-15.17568,-15.36,-14.62272,-12.84096,-9.89184,-5.65248,0]

# Original Spline, curve-fit-12, h = 3, er = 2.87
#y1_arr = [1.242,3.151,5.125,7.172,9.299,11.515,13.828,16.242,18.763,21.392,24.125,26.953,29.86,37.546,44.122,49.882,55.083,59.905,64.471,68.87,73.174,77.439,81.719,86.065,90.531,95.179,100.08,105.321,111.007,117.251,124.137,131.66,134.427,137.11,139.706,142.215,144.639]
#z1_arr = [1.543682926,3.856750966,6.115861279,8.309664647,10.42423046,12.44579906,14.35734722,16.136705,17.76181917,19.20622192,20.44143925,21.43962767,22.1759801,22.77098137,21.8354075,20.04653731,17.76389958,15.18082039,12.41123999,9.529021274,6.584913111,3.622083326,0.677086214,-2.211474065,-4.999479192,-7.631614167,-10.03017684,-12.0822413,-13.61637129,-14.37027445,-13.96828624,-11.96215588,-10.80295906,-9.461383838,-7.95925138,-6.316305499,-4.54927711]

#node_point_y = [0,4.358909211,9.102612816,14.30513684,20.04050729,26.33866451,33.05411201,39.92158047,46.63045823,53.04661229,59.15335383,65.01308259,70.71794326,76.36066548,82.00836953,87.73264656,93.61714511,99.73333701,106.1311997,112.8053743,119.6529992,126.4630597,132.9973564,139.1150706,144.7895668,150]
#node_point_z = [8.29034E-17,5.243459572,10.23913442,14.7382921,18.49220018,21.23655205,22.65220514,22.58910531,21.1628067,18.72638681,15.61163995,12.05878376,8.261295196,4.374639125,0.494806439,-3.271591336,-6.785671833,-9.880285586,-12.35381956,-13.93651752,-14.37681145,-13.51868462,-11.43695969,-8.323780696,-4.427667842,0]

# Sigma male coordinates
#node_point_y = [11.81102362,6.686002538,6.790840414,5.472611956,0.397100006,3.378248016,2.242263879,5.773400396,9.608274693,17.14631469,27.79385499,39.78026765,51.52172307,62.02500727,70.90126505,75.56759568,77.10030908,77.96144006,76.14337024,67.77720948,68.84532234,61.79241115,51.05839165,42.36567369,31.84634908,20.17716535]
#node_point_z = [-4.38247012,6.178738732,18.00954778,29.71684365,40.72319389,51.76444214,63.48436038,74.96962932,86.09476733,95.3233131,100.0557356,101.9535089,101.4796009,96.22426802,88.25791633,77.61220031,65.74867446,54.03313497,42.41614647,34.53613397,22.43865186,13.11330797,8.259133589,0.215402014,-5.143297374,-6.972111554]

# Create substrate spline
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, False,
        [
            "NAME:PolylinePoints",
                            [
                                "NAME:PLPoint",
                                "X:="	, str(-dx/2) + "mm",
                                "Y:="			, str(node_point_y[0]) + "mm",
                                "Z:="			, str(node_point_z[0]) + "mm"
                            ],
                            [
                                "NAME:PLPoint",
                                "X:="		, str(-dx/2) + "mm",
                                "Y:="			, str(node_point_y[1]) + "mm",
                                "Z:="			, str(node_point_z[1]) + "mm"
                            ],
                            [
                                "NAME:PLPoint",
                                "X:="	, str(-dx/2) + "mm",
                                "Y:="			, str(node_point_y[2]) + "mm",
                                "Z:="			, str(node_point_z[2]) + "mm"
                            ],
                            [
                                "NAME:PLPoint",
                                "X:=", str(-dx/2) + "mm",
                                "Y:="		, str(node_point_y[3]) + "mm",
                                "Z:="			, str(node_point_z[3]) + "mm"
                            ],
                            [
                                "NAME:PLPoint",
                                "X:=", str(-dx/2) + "mm",
                                "Y:="	, str(node_point_y[4]) + "mm",
                                "Z:="			, str(node_point_z[4]) + "mm"
                            ],
                            [
                                "NAME:PLPoint",
                                "X:="	, str(-dx/2) + "mm",
                                "Y:="			, str(node_point_y[5]) + "mm",
                                "Z:="			, str(node_point_z[5]) + "mm"
                            ],
                            [
                                "NAME:PLPoint",
                                "X:=", str(-dx/2) + "mm",
                                "Y:="		, str(node_point_y[6]) + "mm",
                                "Z:="			, str(node_point_z[6]) + "mm"
                            ],
                            [
                                "NAME:PLPoint",
                                "X:="	, str(-dx/2) + "mm",
                                "Y:="			, str(node_point_y[7]) + "mm",
                                "Z:="			, str(node_point_z[7]) + "mm"
                            ],
                            [
                                "NAME:PLPoint",
                                "X:=", str(-dx/2) + "mm",
                                "Y:="		, str(node_point_y[8]) + "mm",
                                "Z:="			, str(node_point_z[8]) + "mm"
                            ],
                            [
                                "NAME:PLPoint",
                                "X:=", str(-dx/2) + "mm",
                                "Y:="		, str(node_point_y[9]) + "mm",
                                "Z:="			, str(node_point_z[9]) + "mm"
                            ],
                            [
                                "NAME:PLPoint",
                                "X:=", str(-dx/2) + "mm",
                                "Y:="		, str(node_point_y[10]) + "mm",
                                "Z:="			, str(node_point_z[10]) + "mm"
                            ],
                            [
                                "NAME:PLPoint",
                                "X:=", str(-dx/2) + "mm",
                                "Y:="		, str(node_point_y[11]) + "mm",
                                "Z:="			, str(node_point_z[11]) + "mm"
                            ],
                            [
                                "NAME:PLPoint",
                                "X:=", str(-dx/2) + "mm",
                                "Y:="	, str(node_point_y[12]) + "mm",
                                "Z:="			, str(node_point_z[12]) + "mm"
                            ],
                            [
                                "NAME:PLPoint",
                                "X:=", str(-dx/2) + "mm",
                                "Y:="	, str(node_point_y[13]) + "mm",
                                "Z:="			, str(node_point_z[13]) + "mm"
                            ],
                            [
                                "NAME:PLPoint",
                                "X:=", str(-dx/2) + "mm",
                                "Y:=", str(node_point_y[14]) + "mm",
                                "Z:="		, str(node_point_z[14]) + "mm"
                            ],
                            [
                                "NAME:PLPoint",
                                "X:=", str(-dx/2) + "mm",
                                "Y:=", str(node_point_y[15]) + "mm",
                                "Z:="		, str(node_point_z[15]) + "mm"
                            ],
                            [
                                "NAME:PLPoint",
                                "X:=", str(-dx / 2) + "mm",
                                "Y:=", str(node_point_y[16]) + "mm",
                                "Z:="	, str(node_point_z[16]) + "mm"
                            ],
                            [
                                "NAME:PLPoint",
                                "X:=", str(-dx / 2) + "mm",
                                "Y:=", str(node_point_y[17]) + "mm",
                                "Z:="	, str(node_point_z[17]) + "mm"
                            ],
                            [
                                "NAME:PLPoint",
                                "X:=", str(-dx / 2) + "mm",
                                "Y:=", str(node_point_y[18]) + "mm",
                                "Z:="	, str(node_point_z[18]) + "mm"
                            ],
                            [
                                "NAME:PLPoint",
                                "X:=", str(-dx / 2) + "mm",
                                "Y:=", str(node_point_y[19]) + "mm",
                                "Z:="	, str(node_point_z[19]) + "mm"
                            ],
                            [
                                "NAME:PLPoint",
                                "X:=", str(-dx / 2) + "mm",
                                "Y:=", str(node_point_y[20]) + "mm",
                                "Z:="	, str(node_point_z[20]) + "mm"
                            ],
                            [
                                "NAME:PLPoint",
                                "X:=", str(-dx / 2) + "mm",
                                "Y:=", str(node_point_y[21]) + "mm",
                                "Z:="	, str(node_point_z[21]) + "mm"
                            ],
                            [
                                "NAME:PLPoint",
                                "X:=", str(-dx / 2) + "mm",
                                "Y:=", str(node_point_y[22]) + "mm",
                                "Z:="	, str(node_point_z[22]) + "mm"
                            ],
                            [
                                "NAME:PLPoint",
                                "X:=", str(-dx / 2) + "mm",
                                "Y:=", str(node_point_y[23]) + "mm",
                                "Z:="	, str(node_point_z[23]) + "mm"
                            ],
                            [
                                "NAME:PLPoint",
                                "X:=", str(-dx / 2) + "mm",
                                "Y:=", str(node_point_y[24]) + "mm",
                                "Z:="	, str(node_point_z[24]) + "mm"
                            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Spline",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 25,
                "NoOfSegments:="	, "0"
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Polyline2",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"vacuum\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "ShellElement:="	, False,
        "ShellElementThickness:=", "0mm",
        "ReferenceTemperature:=", "20cel",
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])

# Sweep substrate spline along vector
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Polyline2",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "ClearAllIDs:="		, False,
        "SweepVectorX:="	, str(dx)+ "mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0mm"
    ])


# Thicken the substrate spline
oEditor.ThickenSheet(
    [
        "NAME:Selections",
        "Selections:="		, "Polyline2",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:SheetThickenParameters",
        "Thickness:="		, str(h) + "mm",
        "BothSides:="		, False,
        [
            "NAME:ThickenAdditionalInfo",
            [
                "NAME:ShellThickenDirectionInfo",
                "SampleFaceID:="	, 17019,
                "ComponentSense:="	, True,
                [
                    "NAME:PointOnSampleFace",
                    "X:="			, "5.73573mm",
                    "Y:="			, "149.9442687671mm",
                    "Z:="			, "-0.0475630781023626mm"
                ],
                [
                    "NAME:DirectionAtPoint",
                    "X:="			, "0mm",
                    "Y:="			, "0.649164754826833mm",
                    "Z:="			, "-0.760647829873074mm"
                ]
            ]
        ]
    ])

oEditor.Copy(
    [
        "NAME:Selections",
        "Selections:="		, "Polyline2"
    ])
oEditor.Paste()


# Change the color of the substrate spline
oEditor.ChangeProperty(
    [
        "NAME:AllTabs",
        [
            "NAME:Geometry3DAttributeTab",
            [
                "NAME:PropServers",
                "Polyline2"
            ],
            [
                "NAME:ChangedProps",
                [
                    "NAME:Color",
                    "R:="			, 255,
                    "G:="			, 255,
                    "B:="			, 255
                ]
            ]
        ]
    ])

# Change the color of the substrate spline
oEditor.ChangeProperty(
    [
        "NAME:AllTabs",
        [
            "NAME:Geometry3DAttributeTab",
            [
                "NAME:PropServers",
                "Polyline3"
            ],
            [
                "NAME:ChangedProps",
                [
                    "NAME:Color",
                    "R:="			, 255,
                    "G:="			, 255,
                    "B:="			, 255
                ]
            ]
        ]
    ])

# Sweep the wrap spline more
oEditor.ChangeProperty(
    [
        "NAME:AllTabs",
        [
            "NAME:Geometry3DCmdTab",
            [
                "NAME:PropServers",
                "Polyline3:SweepAlongVector:1"
            ],
            [
                "NAME:ChangedProps",
                [
                    "NAME:Vector",
                    "X:="			, str(dx + 6) + "mm",
                    "Y:="			, "0mm",
                    "Z:="			, "0mm"
                ]
            ]
        ]
    ])

# Move the wrap spline back to center
oEditor.Move(
    [
        "NAME:Selections",
        "Selections:="		, "Polyline3",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:TranslateParameters",
        "TranslateVectorX:="	, str(-3) + "mm",
        "TranslateVectorY:="	, "0mm",
        "TranslateVectorZ:="	, "0mm"
    ])

# Place to store the final adjusted values for HFSS
y1_arr_final = []
z1_arr_final = []

# Append "mm" onto the end of each value
for y1 in y1_arr:

    y1_arr_final.append(str(y1) + str("mm"))

# For y1 too
for z1 in z1_arr:

    z1_arr_final.append(str(z1) + str("mm"))


# Just 23 for now because that's how many strips we have, this can be changed later.
for i in range(1, slot_num + 1):
    # Create a slot
    oEditor.CreateRectangle(
        [
            "NAME:RectangleParameters",
            "IsCovered:="	, True,
            "XStart:="		, str(-dx/2) + "mm",
            "YStart:="		, y1_arr_final[i-1],
            "ZStart:="		, z1_arr_final[i - 1],
            "Width:="		, str(dx) + "mm",
            "Height:="		, "2mm",
            "WhichAxis:="		, "Z"
        ],
        [
            "NAME:Attributes",
            "Name:="		, "Rectangle" + str(i),
            "Flags:="		, "",
            "Color:="		, "(143 175 143)",
            "Transparency:="	, 0,
            "PartCoordinateSystem:=", "Global",
            "UDMId:="		, "",
            "MaterialValue:="	, "\"vacuum\"",
            "SurfaceMaterialValue:=", "\"\"",
            "SolveInside:="		, True,
            "ShellElement:="	, False,
            "ShellElementThickness:=", "0mm",
            "ReferenceTemperature:=", "20cel",
            "IsMaterialEditable:="	, True,
            "UseMaterialAppearance:=", False,
            "IsLightweight:="	, False
        ])

    # Wrap the slot
    oEditor.WrapSheet(
        [
            "NAME:Selections",
            "Selections:="		, "Rectangle" + str(i) + ",Polyline3"
        ],
        [
            "NAME:WrapSheetParameters",
            "Imprinted:="		, False
        ])

    #oEditor.ChangeProperty(
    #    [
    #        "NAME:AllTabs",
    #        [
    #            "NAME:Geometry3DCmdTab",
    #            [
    #                "NAME:PropServers",
    #                "Rectangle" + str(i) + ":CreateRectangle:1"
    #            ],
    #            [
    #                "NAME:ChangedProps",
    #                [
    #                    "NAME:Position",
    #                    "X:="		, str(-dx/2) + "mm",
    #                    "Y:="			, y1_arr_final[i-1],
    #                    "Z:="			, z1_arr_final[i - 1]
    #                ]
    #            ]
    #        ]
    #    ])

# Unite the slots
#oEditor.Unite(
#	[
#		"NAME:Selections",
#		"Selections:="		, "Rectangle1,Rectangle2,Rectangle3,Rectangle4,Rectangle5,Rectangle6,Rectangle7,Rectangle8,Rectangle9,Rectangle10,Rectangle11,Rectangle12,Rectangle13,Rectangle14,Rectangle15,Rectangle16,Rectangle17,Rectangle18,Rectangle19,Rectangle20,Rectangle21,Rectangle22,Rectangle23,Rectangle24,Rectangle25,Rectangle26,Rectangle27,Rectangle28,Rectangle29,Rectangle30,Rectangle31,Rectangle32,Rectangle33,Rectangle34,Rectangle35,Rectangle36,Rectangle37"
#	],
#	[
#		"NAME:UniteParameters",
#		"KeepOriginals:="	, False,
#		"TurnOnNBodyBoolean:="	, True
#	])

# Change the color to make the slots easier to see
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers",
				"Polyline2_ObjectFromFace1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Color",
					"R:="			, 0,
					"G:="			, 128,
					"B:="			, 0
				]
			]
		]
	])

# Create an object from the face of the substrate polyline
oEditor.CreateObjectFromFaces(
	[
		"NAME:Selections",
		"Selections:="		, "Polyline2",
		"NewPartsModelFlag:="	, "Model"
	],
	[
		"NAME:Parameters",
		[
			"NAME:BodyFromFaceToParameters",
			"FacesToDetach:="	, [23]
		]
	],
	[
		"CreateGroupsForNewObjects:=", False
	])

# Create the msg from the subtraction of the united slots from the face of the substrate spline
oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "Polyline2_ObjectFromFace1",
		"Tool Parts:="		, "Rectangle1"
	],
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False,
		"TurnOnNBodyBoolean:="	, True
	])

# Create a place for the feed to be placed
oEditor.CreateObjectFromFaces(
	[
		"NAME:Selections",
		"Selections:="		, "Polyline3",
		"NewPartsModelFlag:="	, "Model"
	],
	[
		"NAME:Parameters",
		[
			"NAME:BodyFromFaceToParameters",
			"FacesToDetach:="	, [57]
		]
	],
	[
		"CreateGroupsForNewObjects:=", False
	])
oEditor.ThickenSheet(
	[
		"NAME:Selections",
		"Selections:="		, "Polyline3_ObjectFromFace1",
		"NewPartsModelFlag:="	, "Model"
	],
	[
		"NAME:SheetThickenParameters",
		"Thickness:="		, "10mm",
		"BothSides:="		, False,
		[
			"NAME:ThickenAdditionalInfo",
			[
				"NAME:ShellThickenDirectionInfo",
				"SampleFaceID:="	, 1938,
				"ComponentSense:="	, True,
				[
					"NAME:PointOnSampleFace",
					"X:="			, "2.648628mm",
					"Y:="			, "1.10364867647113mm",
					"Z:="			, "-0.915490040076778mm"
				],
				[
					"NAME:DirectionAtPoint",
					"X:="			, "0mm",
					"Y:="			, "-0.638447095715299mm",
					"Z:="			, "-0.76966571053458mm"
				]
			]
		]
	])
oEditor.Copy(
	[
		"NAME:Selections",
		"Selections:="		, "Polyline3_ObjectFromFace1"
	])
oEditor.Paste()

oEditor.CreateObjectFromFaces(
	[
		"NAME:Selections",
		"Selections:="		, "Polyline3",
		"NewPartsModelFlag:="	, "Model"
	],
	[
		"NAME:Parameters",
		[
			"NAME:BodyFromFaceToParameters",
			"FacesToDetach:="	, [59]
		]
	],
	[
		"CreateGroupsForNewObjects:=", False
	])
oEditor.ThickenSheet(
	[
		"NAME:Selections",
		"Selections:="		, "Polyline3_ObjectFromFace3",
		"NewPartsModelFlag:="	, "Model"
	],
	[
		"NAME:SheetThickenParameters",
		"Thickness:="		, "10mm",
		"BothSides:="		, False,
		[
			"NAME:ThickenAdditionalInfo",
			[
				"NAME:ShellThickenDirectionInfo",
				"SampleFaceID:="	, 2056,
				"ComponentSense:="	, True,
				[
					"NAME:PointOnSampleFace",
					"X:="			, "2.64862800000013mm",
					"Y:="			, "150.930867442924mm",
					"Z:="			, "-1.09070996064842mm"
				],
				[
					"NAME:DirectionAtPoint",
					"X:="			, "-0mm",
					"Y:="			, "0.76064247141928mm",
					"Z:="			, "0.649171033452025mm"
				]
			]
		]
	])
oEditor.Copy(
	[
		"NAME:Selections",
		"Selections:="		, "Polyline3_ObjectFromFace3"
	])
oEditor.Paste()

# Create equation based surface
oEditor.CreateEquationSurface(
	[
		"NAME:EquationBasedSurfaceParameters",
		"XuvFunction:="		, "_v*exp(180*_u)",
		"YuvFunction:="		, "_u",
		"ZuvFunction:="		, "0",
		"uStart:="		, "-10mm",
		"uEnd:="		, "0",
		"vStart:="		, "-15mm",
		"vEnd:="		, "15mm",
		"Version:="		, 1
	],
	[
		"NAME:Attributes",
		"Name:="		, "EquationSurface1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"ReferenceTemperature:=", "20cel",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor.WrapSheet(
	[
		"NAME:Selections",
		"Selections:="		, "Polyline3_ObjectFromFace2,EquationSurface1"
	],
	[
		"NAME:WrapSheetParameters",
		"Imprinted:="		, False
	])
