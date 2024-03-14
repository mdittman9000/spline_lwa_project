# ----------------------------------------------
# Script Recorded by Ansys Electronics Desktop Version 2021.2.0
# 14:56:23  Jul 20, 2023
# ----------------------------------------------
import ScriptEnv
#from txt_convert import serve_data

#dy_file = open("dy.csv", "r")

# Input num of slots
slot_num = 37

# The input date
y1_arr = [1.242,3.151,5.125,7.172,9.299,11.515,13.828,16.242,18.763,21.392,24.125,26.953,34.647,41.312,47.144,52.377,57.193,61.718,66.045,70.244,74.373,78.481,82.615,86.82,91.145,95.646,100.386,105.442,110.905,116.868,123.406,130.519,133.318,136.035,138.666,141.211]
z1_arr = [1.543682926,3.856750966,6.115861279,8.309664647,10.42423046,12.44579906,14.35734722,16.136705,17.76181917,19.20622192,20.44143925,21.43962767,22.77021785,22.38843515,21.00156076,19.02366292,16.68301189,14.11378783,11.39976603,8.59876772,5.753342182,2.899736683,0.070816785,-2.697600007,-5.364531219,-7.87805058,-10.16535698,-12.12270472,-13.59571057,-14.35380753,-14.07492819,-12.37389967,-11.29490513,-10.02464411,-8.585141216,-6.996354908]

# Place to store the final adjusted values for HFSS
y1_arr_final = []
z1_arr_final = []

# Append "mm" onto the end of each value
for y1 in y1_arr:

	y1_arr_final.append(str(y1) + str("mm"))

# For y1 too
for z1 in z1_arr:

	z1_arr_final.append(str(z1) + str("mm"))

#radius, first_strip_width, dy = serve_data()

ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("spline-lwa-2023")
oDesign = oProject.SetActiveDesign("leaky_spline_7")

# Just 23 for now because that's how many strips we have, this can be changed later.
for i in range(1, slot_num + 1):
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
						"NAME:y" + str(i),
						"Value:="	, y1_arr_final[i-1]
					]
				]
			]
		])
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
						"NAME:z" + str(i),
						"Value:=", z1_arr_final[i - 1]
					]
				]
			]
		])
