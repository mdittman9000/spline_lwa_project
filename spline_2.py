import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splprep, splev
import math

OUTPUT_DIR = "R:\\Code Repository\\Spline LWA project\\output"

##################################
# Step 0 -> Basic math functions #
##################################

def dot_product(v1, v2):
    """
                                                                         [0]        [1]
    Return the dot product of two arrays. THE ARRAYS MUST BE OF FORM ( (X1, X2), (Y1, Y2) )
    :param v1: The first vector
    :param v2: The second vector
    :return:
    """
    return ((v1[0][1] - v1[0][0]) * (v2[0][1] - v2[0][0])) + ((v1[1][1] - v1[1][0]) * (v2[1][1] - v2[1][0]))

def vector_length(v1):
    """
    Return the length of a vector
    :param v1: The vector to return the length of
    :return:
    """
    return math.sqrt(dot_product(v1, v1))

################################
# Step 1 -> Choose node points #
################################

# Choose your node points
# First spline example
#node_point_x = (0, 10, 20, 30)
#node_point_y = (0, 20, -10, 0)

node_point_x = (0, 100, 200, 300)
node_point_y = (0, 20, -10, 0)

# Other spline examples
#node_point_x = (0, 1, 2, 3, 4, 5)
#node_point_y = (0, 2, 0, 0, 0, 2)

# We need the node start and end
node_end_x = node_point_x[len(node_point_x) - 1]
node_start_x = node_point_x[0]

# Convert them to a numpy array
nodes = np.array((node_point_x, node_point_y))

#################################
# Step 2 -> Create spline curve #
#################################

# Interpolate the nodes, when s = 0 the interpolation must pass through all the points
tck, u = splprep(nodes, s=0)  # tck is a tuple (t, c, k) that contains the vector of knots, the B-spline
                                          # coefficients, and the degree of the spline
                                          # u is an array of the values of the parameter

INTERPOLATION_STEP_SIZE = 0.001
INTERPOLATION_END = 1.01
NUMBER_OF_INTERPOLATION_POINTS = INTERPOLATION_END/INTERPOLATION_STEP_SIZE

# How many points in the spline?
u_new = np.arange(0, INTERPOLATION_END, INTERPOLATION_STEP_SIZE)

# Return the interpolated points based on a tck tuple and an array 'u or u-new (for higher discretization)' of x-points
interpolated_x, interpolated_y = splev(u_new, tck)

#############################################
# Step 3 - 1-> Numeric derivatives (for later) #
#############################################

x_prime = []

for i in range(0, len(interpolated_x)-1):
    x_prime.append(interpolated_x[i+1] - interpolated_x[i])

###################################################
# Step 3 - 2 -> Polynomial curve fit + derivative #
###################################################

# What power will the polynomial curve-fit for the spline curve be
POLYFIT_POWER = 10

# Compute the coefficients and the function of the polynomial curve fit of the spline curve
polynomial_curve_fit_coefficients = np.polyfit(interpolated_x, interpolated_y, POLYFIT_POWER)
polynomial_curve_fit_function = np.poly1d(polynomial_curve_fit_coefficients)

POLYNOMIAL_STEP_SIZE = 0.001
POLYNOMIAL_END = 3
NUMBER_OF_POLYNOMIAL_POINTS = POLYNOMIAL_END/POLYNOMIAL_STEP_SIZE

# Create the x and y points of the polynomial curve fit
polynomial_curve_fit_x_points = np.arange(node_start_x, node_end_x, POLYNOMIAL_STEP_SIZE)
polynomial_curve_fit_y_points = polynomial_curve_fit_function(polynomial_curve_fit_x_points)

# Calculate the first derivative of the polynomial-curve fit
polynomial_curve_fit_first_derivative = np.polyder(polynomial_curve_fit_function)
polynomial_curve_fit_first_derivative_y_points = polynomial_curve_fit_first_derivative(polynomial_curve_fit_x_points)

#######################################################
# Step 3 - 2a -> Calculation of tangent line on curve #
#######################################################

# What point are we intereseted in calculating the tangent line of?
point_to_calculate_tangent_line = 12

# Calculate the slope, the y-point the tangent line comes in contact with and use this information to calculate b,
# which is the y-intercept
slope_of_tangent_line = polynomial_curve_fit_first_derivative(point_to_calculate_tangent_line)
y_point_of_tangent_line = polynomial_curve_fit_function(point_to_calculate_tangent_line)
b_tangent = -slope_of_tangent_line*point_to_calculate_tangent_line + y_point_of_tangent_line

# Create some x_points around the point that we are calculating the tangent point at, and feed this into the tangent
# line function to create the y points
tangent_x_points = np.arange(point_to_calculate_tangent_line-.5, point_to_calculate_tangent_line+.5, .01)
tangent_y_points = tangent_x_points * slope_of_tangent_line + b_tangent

######################################################
# Step 3 - 2b -> Calculation of normal line on curve #
######################################################

# The point we want to calculate the perpendicular line at will be the same as where we calculate the tangent line
point_to_calculate_perpendicular_line = point_to_calculate_tangent_line

# Calculate the slope of the perpendicular line which is just -1 over slope_tangent_line
slope_of_perpendicular_line = -1/slope_of_tangent_line
y_point_of_perpendicular_line = y_point_of_tangent_line
b_perpendicular = -slope_of_perpendicular_line*point_to_calculate_perpendicular_line + y_point_of_perpendicular_line

perpendicular_x_points = np.arange(point_to_calculate_perpendicular_line-.5, point_to_calculate_perpendicular_line+.5, .01)
perpendicular_y_points = perpendicular_x_points * slope_of_perpendicular_line + b_perpendicular

########################################################################
# Step 3 - 2c -> Find the angle between the normal line and the y-axis #
########################################################################

# What are the individual points to deal with of the y-axis parallel line?
y_axis_x_point_1 = point_to_calculate_perpendicular_line
y_axis_y_point_1 = y_point_of_perpendicular_line
y_axis_x_point_2 = y_axis_x_point_1
y_axis_y_point_2 = y_axis_y_point_1 + 10

# Put the y-axis parallel line in an array
y_axis_x_cord = (y_axis_x_point_1, y_axis_x_point_2)
y_axis_y_cord = (y_axis_y_point_1, y_axis_y_point_2)

# Y-axis vec
y_axis_vec = (y_axis_x_cord, y_axis_y_cord)

# What are the individual points to deal with from the perpendicular-spline line?
perpendicular_line_x_point_1 = point_to_calculate_perpendicular_line
perpendicular_line_y_point_1 = y_point_of_perpendicular_line

# What angle to calculate based on the sign of the slope
if slope_of_perpendicular_line < 0:
    perpendicular_line_x_point_2 = perpendicular_line_x_point_1 - 10

elif slope_of_perpendicular_line > 0:
    perpendicular_line_x_point_2 = perpendicular_line_x_point_1 + 10

else:
    print("You haven't made it this far yet")

perpendicular_line_y_point_2 = perpendicular_line_x_point_2 * slope_of_perpendicular_line + b_perpendicular

# Put the y-axis parallel line in an array
perpendicular_line_x_cord = (perpendicular_line_x_point_1, perpendicular_line_x_point_2)
perpendicular_line_y_cord = (perpendicular_line_y_point_1, perpendicular_line_y_point_2)

# Perpendicular vec
perpendicular_vec = (perpendicular_line_x_cord, perpendicular_line_y_cord)

# Find all the intermediate components necessary to calculate the angle
dot_product_of_y_axis_and_perpendicular_line = dot_product(y_axis_vec, perpendicular_vec)
length_of_y_axis_vec = vector_length(y_axis_vec)
length_of_perpendicular_line = vector_length(perpendicular_vec)

# Calculate the angle
angle = (180/3.14)*math.acos(dot_product_of_y_axis_and_perpendicular_line/(length_of_y_axis_vec*length_of_perpendicular_line))

##########################################
# Step 4 -> Print diagnostic information #
##########################################

# Spline curve and curve-fit information
print("############################################################################################")
print("Spline curve and curve-fit information")
print("\nNumber of interpolation points for spline curve :", NUMBER_OF_INTERPOLATION_POINTS)
print("\nInterpolated_x difference between consecutive points : ", x_prime)
print("\nThe coefficients of the polynomial curve fit of the spline curve : ", polynomial_curve_fit_coefficients)
print("\nThe function of the curve fit of the spline curve : ", polynomial_curve_fit_function)
print("\nPolynomial curve-fit first derivative : ", polynomial_curve_fit_first_derivative)
print("\nPolynomial curve-fit x-points : ", polynomial_curve_fit_x_points)
print("\nPolynomial curve-fit y-points : ", polynomial_curve_fit_y_points)
print("############################################################################################")

# Tangent line information
print("############################################################################################")
print("Tangent line information")
print("\nSlope of tangent line : ", slope_of_tangent_line)
print("\ny-point of tangent line: ", y_point_of_tangent_line)
print("\ny-intercept (b) of slope-intercept form of tangent line", b_tangent)
print("############################################################################################")

# Perpendicular line information
print("############################################################################################")
print("Perpendicular line information")
print("\nSlope of perpendicular line : ", slope_of_perpendicular_line)
print("\ny-point of perpendicular line: ", y_point_of_perpendicular_line)
print("\ny-intercept (b) of slope-intercept form of perpendicular line", b_perpendicular)
print("############################################################################################")

# Print intermediate information before calculating the angle
print("############################################################################################")
print("\n                   (x1, x2)               (y1, y2)")
print("Y-axis vector : ", y_axis_vec)
print("Normal vector : ", perpendicular_vec)
print("\nDot product of y-axis and perpendicular line : ", dot_product_of_y_axis_and_perpendicular_line)
print("\nLength of the y-axis vector : ", length_of_y_axis_vec)
print("\nLength of the perpendicular line vector : ", length_of_perpendicular_line)

# Print the angle between the perpendicular line and y-axis
print("\nAngle between y-axis and perpendicular line : ", str(angle) + u'\N{DEGREE SIGN}')
print("############################################################################################")

######################################################
# Step 5a -> Preliminary plot generation information #
######################################################


# Location to put the angle?
#angle_text_position_x = (perpendicular_line_x_point_2 - perpendicular_line_x_point_1)/2 + perpendicular_line_x_point_1
#angle_text_position_y = (perpendicular_line_y_point_2 - perpendicular_line_y_point_1)/2 + perpendicular_line_y_point_1

#angle_text_position_x = (perpendicular_line_x_point_2 - perpendicular_line_x_point_1)/2 + perpendicular_line_x_point_1
#angle_text_position_y = (y_axis_y_point_2 - perpendicular_line_y_point_1)/2 + perpendicular_line_y_point_2

angle_text_position_x = perpendicular_line_x_point_1 - 3
angle_text_position_y = perpendicular_line_y_point_1 - 3

###########################################
# Step 5b -> Graph all of the information #
###########################################

fig, ax = plt.subplots()
ax.set_xlabel("X-cord of antenna [mm]", fontsize=14)
ax.set_ylabel("Y-cord of antenna [mm]", fontsize=14)
#ax.plot(node_point_x, node_point_y, 'ob', label='Nodes')
#ax.plot(interpolated_x, interpolated_y, 'r-', label='Spline-interpolation')
ax.plot(polynomial_curve_fit_x_points, polynomial_curve_fit_y_points, "g-", label="Spline-curve-fit")
#ax.plot(polynomial_curve_fit_x_points, polynomial_curve_fit_first_derivative_y_points, label="Spline-curve-fit-first-derivative")
#ax.plot(tangent_x_points, tangent_y_points, label="Tangent line at point of interest")
#ax.plot(perpendicular_x_points, perpendicular_y_points, label="Perpendicular line at point of interest")
ax.plot(perpendicular_line_x_cord, perpendicular_line_y_cord, 'go', linestyle='--')
ax.plot(y_axis_x_cord, y_axis_y_cord, 'go', linestyle="--")

# Label the angle of a single point
ax.text(angle_text_position_x, angle_text_position_y, str(round(angle, 2)) + u'\N{DEGREE SIGN}', fontsize=12)

plt.xlim([0, 15])
plt.ylim([0, 15])
ax.set_aspect('equal', adjustable='box')
ax.grid()
ax.legend()
plt.savefig(OUTPUT_DIR + "\\spline_representation", dpi=450)
plt.show()
