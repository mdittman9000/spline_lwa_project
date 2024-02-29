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
y1_arr = [1.242,3.151,5.125,7.172,9.299,11.515,13.828,16.242,18.763,21.392,24.125,26.953,34.562,41.197,47.024,52.263,57.088,61.624,65.962,70.172,74.311,78.429,82.571,86.784,91.116,95.622,100.365,105.42,110.873,116.815,123.311,130.355,133.158,135.88,138.517,141.066,143.529]
z1_arr = [1.543682926,3.856750966,6.115861279,8.309664647,10.42423046,12.44579906,14.35734722,16.136705,17.76181917,19.20622192,20.44143925,21.43962767,22.76618888,22.40630732,21.03918927,19.07339987,16.7387039,14.17023983,11.45371162,8.64778368,5.796403274,2.935728607,0.100477514,-2.674544185,-5.347399675,-7.865472324,-10.15613792,-12.115372,-13.58917533,-14.35121453,-14.08765452,-12.42990566,-11.36285967,-10.10302035,-8.672171389,-7.092073165,-5.380497055]

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
oDesign = oProject.SetActiveDesign("leaky_spline_9")

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
