############################
# Author : Michael Dittman #
############################

import numpy as np
from numpy import diff
import matplotlib.pyplot as plt
from scipy.interpolate import splprep, splev
from scipy import integrate
import math
import pandas as pd

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

def required_periodicity_for_angle(angle_to_bend):
    """
    Return required periodicity from the angle to bend
    The angle to bend is determined as -(perpendicular_angle_of_slot - desired_angle)
    :param angle_to_bend: The angle to bend of the slot
    :return:
    """

    # Curve-fit-1
    #return 6.31+(0.05966)*(angle_to_bend) + (0.000555)*(angle_to_bend**2) + (0.00000023692)*(angle_to_bend**3) - (0.0000000474)*(angle_to_bend**4) - (0.00000000030856)*(angle_to_bend**5)


    # Curve-fit-3
    #
    #print("Periodicity is : ", str(6.14702119153055 + (5.83245977360812*pow(10, -2)*angle_to_bend) + (6.1885747242777*(pow(10, -4)*(angle_to_bend**2))) + (3.27556335842171*(pow(10, -6))*(angle_to_bend**3)) + (-1.01273660742494*pow(10, -7)*(angle_to_bend**4)) + (-4.02657714686286*pow(10, -9)*(angle_to_bend**5)) + (-5.28348954913997*pow(10, -11)*(angle_to_bend**6)) + (-2.37380794347022*pow(10, -13)*(angle_to_bend**7))))
    #return 6.14702119153055 + (5.83245977360812*pow(10, -2)*angle_to_bend) + (6.1885747242777*(pow(10, -4)*(angle_to_bend**2))) + (3.27556335842171*(pow(10, -6))*(angle_to_bend**3)) + (-1.01273660742494*pow(10, -7)*(angle_to_bend**4)) + (-4.02657714686286*pow(10, -9)*(angle_to_bend**5)) + (-5.28348954913997*pow(10, -11)*(angle_to_bend**6)) + (-2.37380794347022*pow(10, -13)*(angle_to_bend**7))

    #print("Periodicity is : ",  str(6.9474143296995088 + (8.3032010656602151*pow(10, -2)*angle_to_bend) + (3.3411549930261568*(pow(10, -3)*(angle_to_bend**2))) + (-6.5912959244645712*(pow(10, -6))*(angle_to_bend**3)) + (-1.4076366246101404*pow(10, -5)*(angle_to_bend**4)) + (-6.1251164709887581*pow(10, -7)*(angle_to_bend**5)) + (-4.1090393439246056*pow(10, -9)*(angle_to_bend**6)) + (3.0912870352796139*pow(10, -10)*(angle_to_bend**7)) + (8.5510012063374104*pow(10, -12)*(angle_to_bend**8)) + (8.7344825867715888*pow(10, -14)*(angle_to_bend**9)) + (3.2484651094068338*pow(10, -16)*(angle_to_bend**10))))

    # curve-fit-5
    #return 6.9474143296995088 + (8.3032010656602151*pow(10, -2)*angle_to_bend) + (3.3411549930261568*(pow(10, -3)*(angle_to_bend**2))) + (-6.5912959244645712*(pow(10, -6))*(angle_to_bend**3)) + (-1.4076366246101404*pow(10, -5)*(angle_to_bend**4)) + (-6.1251164709887581*pow(10, -7)*(angle_to_bend**5)) + (-4.1090393439246056*pow(10, -9)*(angle_to_bend**6)) + (3.0912870352796139*pow(10, -10)*(angle_to_bend**7)) + (8.5510012063374104*pow(10, -12)*(angle_to_bend**8)) + (8.7344825867715888*pow(10, -14)*(angle_to_bend**9)) + (3.2484651094068338*pow(10, -16)*(angle_to_bend**10))

    # curve-fit-6
    #return 6.9604490558418082 + (7.3719152042775876*pow(10, -2)*angle_to_bend) + (8.7864577271711940*(pow(10, -4)*(angle_to_bend**2))) + (5.0449252349248393*(pow(10, -6))*(angle_to_bend**3))

    # WHAT IN THE HELL IS THIS ONE??? h = 3.0mm, er = 3.05
    #return  6.592387738269 + (6.502548726*pow(10, -2)*angle_to_bend) + (6.82996459*(pow(10, -4)*(angle_to_bend**2))) + (3.36637154*(pow(10, -6))*(angle_to_bend**3))

    # curve-fit-11
    #return 6.63245188 + (6.742907*pow(10, -2)*angle_to_bend) + (7.1589545658*(pow(10, -4)*(angle_to_bend**2))) + (3.5534671527*(pow(10, -6))*(angle_to_bend**3))

    # Curve-fit-12
    #return 6.951678 + (7.26906919*pow(10, -2)*angle_to_bend) + (7.483190*(pow(10, -4)*(angle_to_bend**2))) + (3.21570266*(pow(10, -6))*(angle_to_bend**3))

    # Curve-fit-13
    return 7.3118623085018557 + (7.7226269233673053 * pow(10, -2) * angle_to_bend) + (7.9873519666050848 * (pow(10, -4) * (angle_to_bend ** 2))) + (3.6470448267764143 * (pow(10, -6)) * (angle_to_bend ** 3))

def find_x_y_coord_corresponding_to_arc_length(current_arc_length, arc_length_array, x_coordinates, y_coordinates):
    """
    Find the x coordinate of the current arc length of the slot center. This x-cordinate is then used to construct the
    tangent line from the first derivative, which in turn constructs the normal vector to the surface. The angle of this
    normal vector with respect to the y-axis is then used as the perpendicular angle of the slot, which determines the
    angle required to bend, which in turn determines the periodicity required between this slot center and the next slot
    center to achieve that steering.
    :param current_arc_length: The arc length of the current slot center
    :param arc_length_array: The numerically computed arc length
    :param x_coordinates: The array of x-coordinates
    :return: The x-coordinate that this current arc length corresponds to
    """

    # Debug to see how close the found arc length is to the one we need
    #print("Arc length to find : ", current_arc_length)
    #print(len(arc_length_array))

    # Iterate through the entire arc_length array until the first greater arc length then our arc length is found
    for i in range (0, len(arc_length_array) - 1):

        if arc_length_array[i] >= current_arc_length:

            # Debug to see how close the found arc length is to the one we need
            #print("Arc length found", arc_length_array[i])

            return x_coordinates[i], y_coordinates[i]

################################
# Step 1 -> Choose node points #
################################

# Choose your node points
# First spline example
#node_point_x = (0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150)
#node_point_y = (0, 11.09, 18.47, 22.2, 22.58, 20, 15.128, 8.75, 1.865, -4.6778, -10, -13.405, -14.365, -12.550, -7.78,0)

# USE THESE
node_point_x = (15, 45, 75, 105, 135)
node_point_y = (0, 15, 0, -15, 0)

# sigma male jawline
#node_point_x = (11.81102362,6.791338583,6.791338583,3.641732283,0.393700787,3.346456693,1.968503937,4.921259843,9.05511811,18.99606299,34.64566929,52.55905512,62.5984252,72.53937008,76.87007874,78.0511811,76.47637795,68.11023622,68.99606299,63.77952756,51.96850394,43.30708661,34.3503937,20.17716535)
#node_point_y = (-4.38247012,5.378486056,18.02788845,33.96414343,41.53386454,48.60557769,57.7689243,72.11155378,84.96015936,96.61354582,101.2948207,101.1952191,95.81673307,85.85657371,68.22709163,52.39043825,42.82868526,35.55776892,24.30278884,14.34262948,8.864541833,0.996015936,-4.282868526,-6.972111554)

# Number of points to sample, this will sample n + 1 points. The more points you've sampled, the more accurate your spline will be
# but the more you'll have to edit the leaky_spline_hfss_creator.py script :)
node_point_sampling = 25

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

#########################################################################################
# Step 2a -> Sample some interpolation points to force hfss to have more accurate curve #
#########################################################################################

node_sample_point_x = []
node_sample_point_y = []
sample_interval = math.floor(NUMBER_OF_INTERPOLATION_POINTS/node_point_sampling)
print("Sampling Interval is : ", sample_interval)

for i in range(0, int(NUMBER_OF_INTERPOLATION_POINTS)):

    if i%sample_interval == 0:
        node_sample_point_x.append(interpolated_x[i])
        node_sample_point_y.append(interpolated_y[i])

################################################
# Step 3 - 1-> Numeric derivatives (for later) #
################################################

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

POLYNOMIAL_STEP_SIZE = INTERPOLATION_STEP_SIZE
POLYNOMIAL_END = 3
NUMBER_OF_POLYNOMIAL_POINTS = POLYNOMIAL_END/POLYNOMIAL_STEP_SIZE

# Create the x and y points of the polynomial curve fit
polynomial_curve_fit_x_points = np.arange(node_start_x, node_end_x, POLYNOMIAL_STEP_SIZE)
polynomial_curve_fit_y_points = polynomial_curve_fit_function(polynomial_curve_fit_x_points)

# Calculate the first derivative of the polynomial-curve fit
polynomial_curve_fit_first_derivative = np.polyder(polynomial_curve_fit_function)
polynomial_curve_fit_first_derivative_y_points = polynomial_curve_fit_first_derivative(polynomial_curve_fit_x_points)

###############################################################
# Step 3 - 3 -> Compute the numeric derivative and arc length #
###############################################################

# Compute the numeric derivative
dx = INTERPOLATION_STEP_SIZE
dy = diff(polynomial_curve_fit_y_points)/dx

# Arc length integrand
arc_length_integrand = np.sqrt((1+(dy**2)))

# Integrate to find the arc length
arc_length_int = integrate.cumtrapz(arc_length_integrand, polynomial_curve_fit_x_points[0:len(polynomial_curve_fit_x_points)-1], initial=0)

print("\nPolynomial X - points", polynomial_curve_fit_x_points)
print("\nArc length", arc_length_int)

###################################################
# Step 3 - 4 -> Plot the spline curve            #
###################################################

# This is done first so that the perpendicular points can be calculated later.

fig, ax = plt.subplots()
ax.set_xlabel("X-cord of antenna [mm]")
ax.set_ylabel("Y-cord of antenna [mm]")
ax.plot(node_point_x, node_point_y, 'ob', label='Nodes')
ax.plot(interpolated_x, interpolated_y, 'r-', label='Spline-interpolation')
ax.plot(polynomial_curve_fit_x_points, polynomial_curve_fit_y_points, "y-", label="Spline-curve-fit")

print("Interpolated x and y points are : ", interpolated_x, interpolated_y)

#########################################################################
# Step 4 -> Calculation of tangent line on curve at various points #
#########################################################################

# Calculate the angles of the slots
# 6.31+(0.05966)*(M2) + (0.000555)*(M2^2) + (0.00000023692)*(M2^3) - (0.0000000474)*(M2^4) - (0.00000000030856)*(M2^5) -> This will give you required periodicity from desired angle

# Antenna parameters
first_strip_width = 2 #mm
slot_width = 2 #mm
antenna_radius = 329.54 #mm
number_of_slots = 28

######### DESIRED BENDING ANGLE #########
desired_angle = 0   # Desired angle to bend to

# Intermediate parameters
first_slot_center = first_strip_width + (slot_width/2) #mm

# Place to store the calculated periodicities
slot_arc_length_centers = []
slot_center_x_coordinates = []
slot_center_y_coordinates = []
slot_center_periodicities = []

# Slot start coordinates
slot_start_x_coordinates = []
slot_start_y_coordinates = []

# Normal vector angle
slot_normal_vector_angle = []

# Put the first slot_center in
slot_arc_length_centers.append(first_slot_center)

# Calculate the center of the slots
for i in range(0, number_of_slots):#node_point_x[len(node_point_x) - 1]):

    if i == 0:
        # What point are we intereseted in calculating the tangent line of?

        # Find the x, y coordinates of the first slot center, current using the interpolated y points of the ACTUAl spline curve, but this can change
        x_center, y_center = find_x_y_coord_corresponding_to_arc_length(first_slot_center, arc_length_int, polynomial_curve_fit_x_points, polynomial_curve_fit_y_points)

        # Append the coordinates to the proper arrays
        slot_center_x_coordinates.append(x_center)
        slot_center_y_coordinates.append(y_center)

        # What is the arc length of the first slot start?
        first_slot_start = first_slot_center - slot_width/2

        # find the x and y coordinates of the start of the slot
        x_start, y_start = find_x_y_coord_corresponding_to_arc_length(first_slot_start, arc_length_int, polynomial_curve_fit_x_points, polynomial_curve_fit_y_points)

        # The slot start coordinates of the first slot
        slot_start_x_coordinates.append(x_start)
        slot_start_y_coordinates.append(y_start)

        # The point to calculate the tangent line at with thus be the x point on the spline curve that corresponds to an arc length = first_slot_center
        point_to_calculate_tangent_line = x_center

    else:

        # Find the x, y coordinates of the first slot center, current using the interpolated y points of the ACTUAl spline curve, but this can change
        x_center, y_center = find_x_y_coord_corresponding_to_arc_length(slot_arc_length_centers[len(slot_arc_length_centers) - 1], arc_length_int, polynomial_curve_fit_x_points, polynomial_curve_fit_y_points)

        # Append the coordinates to the proper arrays
        slot_center_x_coordinates.append(x_center)
        slot_center_y_coordinates.append(y_center)

        # What is the arc length of the first slot start?
        slot_start = slot_arc_length_centers[len(slot_arc_length_centers) - 1] - slot_width/2

        # find the x and y coordinates of the start of the slot
        x_start, y_start = find_x_y_coord_corresponding_to_arc_length(slot_start, arc_length_int,
                                                                      polynomial_curve_fit_x_points,
                                                                      polynomial_curve_fit_y_points)

        # The slot start coordinates of the first slot
        slot_start_x_coordinates.append(x_start)
        slot_start_y_coordinates.append(y_start)

        # The point to calculate the tangent line at with thus be the x point on the spline curve that corresponds to an arc length = first_slot_center
        point_to_calculate_tangent_line = x_center

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
    # Step 4 - 1 -> Calculation of normal line on curve #
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
    # Step 4 - 2 -> Find the angle between the normal line and the y-axis #
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

    # Fix the sign of the angle
    if slope_of_tangent_line > 0:
        angle = -angle

    slot_normal_vector_angle.append(angle)

    # Determine the required periodicity
    periodicity = required_periodicity_for_angle(-(angle-desired_angle))

    # Catch for if the periodicity returns a negative #
    if periodicity < 2:
        periodicity = 3

    # Make sure we stay between 4mm and 8mm
    if periodicity > 8.0:

        # If it is greater than 8, make it a slow wave
        periodicity = 3

    # THIS IS FOR A CURRENT DESIGN
    #if angle < 0:
    #    if -angle > 11.8:
    #        periodicity = 3

    # Append the newly determined periodicity from the new slot center angle. This becomes the next periodicity
    # used for the slots.
    slot_center_periodicities.append(periodicity)
    slot_arc_length_centers.append(slot_arc_length_centers[len(slot_arc_length_centers)-1] + periodicity)

    #########################################################################
    # Step 4 - 1&2a -> Diagnostic Information for tangent/perpendicular lines #
    #########################################################################

    # Tangent line information
    #print("############################################################################################")
    #print("Tangent line information")
    #print("\nSlope of tangent line : ", slope_of_tangent_line)
    #print("\ny-point of tangent line: ", y_point_of_tangent_line)
    #print("\ny-intercept (b) of slope-intercept form of tangent line", b_tangent)
    #print("############################################################################################")

    # Perpendicular line information
    #print("############################################################################################")
    #print("Perpendicular line information")
    #print("\nSlope of perpendicular line : ", slope_of_perpendicular_line)
    #print("\ny-point of perpendicular line: ", y_point_of_perpendicular_line)
    #print("\ny-intercept (b) of slope-intercept form of perpendicular line", b_perpendicular)
    #print("############################################################################################")

    ax.plot(perpendicular_line_x_cord, perpendicular_line_y_cord, 'go', linestyle='--')
    ax.plot(y_axis_x_cord, y_axis_y_cord, 'go', linestyle="--")

    angle_text_position_x = perpendicular_line_x_point_1 - 0.5
    angle_text_position_y = perpendicular_line_y_point_1 - 10

    #################################################################
    # Step 4 - 3 -> Plot the angle of the normal vector on the plot #
    #################################################################

    # Label the angle of a single point
    ax.text(angle_text_position_x, angle_text_position_y, str(round(angle, 2)) + u'\N{DEGREE SIGN}', fontsize=5)

#################################################################
# Step 5 -> Save the required antenna design parameters         #
#################################################################

# The required parameters are the x and y positions of the slot centers
# as well as the periodicity between the slot centers

slot_x_coordinates_save = np.array(slot_center_x_coordinates) # The retrieved x coordinates of the slot centers

slot_y_coordinates_save = np.array(slot_center_y_coordinates) # The retrieved y coordinates of the slot centers

slot_arc_length_centers_save = np.array(slot_arc_length_centers) # The arc length centers of the slot centers
                                                                 # as determined by the previous slot center
                                                                 # and the periodicity between the slots

slot_center_periodicities_save = np.array(slot_center_periodicities) # The periodicity between consecutive slot centers

slot_start_x_coordinates_save = np.array(slot_start_x_coordinates) # The x coordinate of the slot start

slot_start_y_coordinates_save = np.array(slot_start_y_coordinates) # The y coordinate of the slot start

slot_normal_vector_angle = np.array(slot_normal_vector_angle) # The normal vector angle of the slots

node_sample_point_x_save = np.array(node_sample_point_x) # The sampled points on the spline (x-coord)

node_sample_point_y_save = np.array(node_sample_point_y) # The sampled poitns on the spline (y-coord)

save_array = slot_x_coordinates_save, slot_y_coordinates_save, slot_arc_length_centers_save, \
    slot_center_periodicities_save, slot_start_x_coordinates_save, slot_start_y_coordinates_save, slot_normal_vector_angle,\
    node_sample_point_x_save, node_sample_point_y_save

df = pd.DataFrame(save_array).T

df.to_excel(excel_writer = "output/extracted_antenna_parameters.xlsx")

##########################################
# Step 6 -> Print diagnostic information #
##########################################

# plot the x and y positions retrieved from the arc length positions
ax.plot(slot_center_x_coordinates, slot_center_y_coordinates, 'ro', label="Retrieved x and y coordinates of slot centers")
ax.plot(slot_start_x_coordinates, slot_start_y_coordinates, 'o', color="orange", label="Retrieved x and y coordinates of slot start")

# Spline curve and curve-fit information
print("############################################################################################")
print("Spline curve and curve-fit information")
print("\nNumber of interpolation points for spline curve :", NUMBER_OF_INTERPOLATION_POINTS)
print("\nInterpolated_x difference between consecutive points : ", x_prime)
print("\nThe coefficients of the polynomial curve fit of the spline curve : ", polynomial_curve_fit_coefficients)
print("\nThe function of the curve fit of the spline curve : ", polynomial_curve_fit_function)
print("\nPolynomial curve-fit first derivative : ", polynomial_curve_fit_first_derivative)
print("\nArc length integrand (arc length of curve-fit): ", arc_length_integrand)
print("\nPolynomial curve-fit x-points : ", polynomial_curve_fit_x_points)
print("\nPolynomial curve-fit y-points : ", polynomial_curve_fit_y_points)
print("############################################################################################")

# Print intermediate information before calculating the angle
#print("############################################################################################")
#print("\n                   (x1, x2)               (y1, y2)")
#print("Y-axis vector : ", y_axis_vec)
#print("Normal vector : ", perpendicular_vec)
#print("\nDot product of y-axis and perpendicular line : ", dot_product_of_y_axis_and_perpendicular_line)
#print("\nLength of the y-axis vector : ", length_of_y_axis_vec)
#print("\nLength of the perpendicular line vector : ", length_of_perpendicular_line)

# Print the angle between the perpendicular line and y-axis
#print("\nAngle between y-axis and perpendicular line : ", str(angle) + u'\N{DEGREE SIGN}')
#print("############################################################################################")

###########################################
# Step 6 -> Print all antenna information #
###########################################

#print("\nSlot arc length centers : ", slot_arc_length_centers)
#print("\nPeriodicities : ", periodicities)

plt.xlim([-10, 160])
plt.ylim([-50, 50])
ax.set_aspect('equal', adjustable='box')
ax.grid()
ax.legend()
plt.savefig('output/spline-visualization', bbox_inches='tight', dpi = 250)
plt.show()
##plt.clf()
# Create a seperate plot for verification of numerical methods and such
##debug_fig, debug_ax = plt.subplots()

# What do we want to see the debug of? The spline curve, the curve-fit, the derivative of the curve fit, the numerical
# Derivative + numerical arc length

##debug_ax.set_title("Diagnostic information plot")
##debug_ax.plot(polynomial_curve_fit_x_points, polynomial_curve_fit_y_points, label="spline-curve-fit")
##debug_ax.plot(polynomial_curve_fit_x_points, polynomial_curve_fit_first_derivative_y_points, label="spline-curve-fit-first-der", linewidth=3)
##debug_ax.plot(polynomial_curve_fit_x_points[0:-1], dy, label="Numeric first derivative", linewidth=1)
##debug_ax.plot(polynomial_curve_fit_x_points[0:-1], arc_length_int, label="Numeric arc length")
##debug_ax.grid()
##debug_ax.legend()

##plt.show()