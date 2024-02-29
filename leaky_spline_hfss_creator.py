# ----------------------------------------------
# Script Recorded by Ansys Electronics Desktop Version 2023.2.0
# 14:38:14  Feb 10, 2024
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("spline-lwa-2024")
oDesign = oProject.SetActiveDesign("HFSSDesign2")
oEditor = oDesign.SetActiveEditor("3D Modeler")

# Width of spline in mm
dx = 30

# Thickness of spline in mm
h = 3.0

# Input num of slots
slot_num = 27

# The input date
y1_arr = [16.224,18.154,20.207,22.398,24.736,27.229,29.876,32.664,40.346,46.747,52.287,57.284,61.93,66.35,70.632,74.846,79.052,83.308,87.678,92.235,97.074,102.317,108.115,114.599,121.736,124.291,126.69,128.938,131.045,133.022]
z1_arr = [1.582400387,3.879553003,6.065048849,8.114633853,9.992579111,11.65905713,13.06778191,14.17207874,15.39600393,14.6589539,12.97214985,10.78098435,8.299873807,5.646812106,2.896566866,0.10266599,-2.689013224,-5.432473712,-8.074637724,-10.54193066,-12.72418337,-14.4364351,-15.35184893,-14.90036451,-12.25302209,-10.68334338,-8.884399665,-6.898991391,-4.763388835,-2.508350328]

node_point_y = [15,19.8,24.6,29.4,34.2,39,43.8,48.6,53.4,58.2,63,67.8,72.6,77.4,82.2,87,91.8,96.6,101.4,106.2,111,115.8,120.6,125.4,130.2,135]
node_point_z = [9.22632E-16,5.65248,9.89184,12.84096,14.62272,15.36,15.17568,14.19264,12.53376,10.32192,7.68,4.73088,1.59744,-1.59744,-4.73088,-7.68,-10.32192,-12.53376,-14.19264,-15.17568,-15.36,-14.62272,-12.84096,-9.89184,-5.65248,0]

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
oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "Rectangle1,Rectangle2,Rectangle3,Rectangle4,Rectangle5,Rectangle6,Rectangle7,Rectangle8,Rectangle9,Rectangle10,Rectangle11,Rectangle12,Rectangle13,Rectangle14,Rectangle15,Rectangle16,Rectangle17,Rectangle18,Rectangle19,Rectangle20,Rectangle21,Rectangle22,Rectangle23,Rectangle24,Rectangle25,Rectangle26,Rectangle27,Rectangle28,Rectangle29,Rectangle30,Rectangle31,Rectangle32,Rectangle33,Rectangle34,Rectangle35,Rectangle36,Rectangle37"
	],
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False,
		"TurnOnNBodyBoolean:="	, True
	])

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
