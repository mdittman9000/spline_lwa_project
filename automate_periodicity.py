# ----------------------------------------------
# Script Recorded by Ansys Electronics Desktop Version 2021.2.0
# 14:56:23  Jul 20, 2023
# ----------------------------------------------
import ScriptEnv
#from txt_convert import serve_data

#dy_file = open("dy.csv", "r")

dy_arr = [3.93565109,3.944666663,3.955432803,3.968103525,3.982847166,3.999848146,4.019309002,4.041452776,4.06652579,4.094800923,4.126581458,4.162205633,4.202052052,4.246546125,4.296167801,4.351460862,4.413044188,4.481625467,4.558017986,4.64316135,4.738147203,4.844251412,4.962974691,5.096094283]
dy_final = []

for dy in dy_arr:

	dy_final.append(str(dy) + str("mm"))

#radius, first_strip_width, dy = serve_data()

ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("LWA_basic")
oDesign = oProject.SetActiveDesign("LWA-conformal")

# Just 23 for now because that's how many strips we have, this can be changed later.
for i in range(1, 24):
	oDesign.ChangeProperty(
		[
			"NAME:AllTabs",
			[
				"NAME:LocalVariableTab",
				[
					"NAME:PropServers",
					"LocalVariables"
				],
				[
					"NAME:ChangedProps",
					[
						"NAME:dy" + str(i),
						"Value:="		, dy_final[i-1]
					]
				]
			]
		])
