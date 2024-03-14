import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

c = 3E8  # m/s
f = 27E9  # Hz
lam = c/f  # wavelength
k_0 = 2*np.pi/lam  # wavenumber
dy = 5E-3 # m
N = 55  # Number of elements

FIRST_SLOT_WIDTH = 3E-3

def parse_extracted_antenna_parameters(filename):
    file = filename
    df = pd.read_excel(file, usecols='B,C,E,H')

    print(df)

    # Distance array
    d = []

    for i in range(0, len(df) - 1):

        d.append((df.iloc[i][0], df.iloc[i][1], df.iloc[i][3], df.iloc[i][6]))

    return d

def compute_planar_af(theta, dy, pointing_angle):
    """
    Compute the array factor of the spline
    :return:
    """

    # Place to store the compute array factor
    AF = []

    #
    theta_naught = (pointing_angle) * np.pi / 180

    for angle in theta:

        AF_cur = 0

        angle = angle * np.pi/180

        # Sum each of the elements
        for n in range(1, N):

            x_i = n*dy
            beta_y = k_0*dy*np.sin(theta_naught)
            I_0 = 1
            I_n = I_0 * np.exp(-1j * n * beta_y)
            AF_cur += I_n * np.exp(1j * k_0 * x_i * np.sin(angle))

        AF.append(AF_cur)

    return AF

def compute_spline_af(theta, R, desired_angle):
    """
    Compute the array factor of the spline
    :return:
    """

    # Place to store the compute array factor
    AF = []

    # Loop through all the angles we want to calculate the array factor at
    for angle in theta:

        # What's the current array factor at this angle?
        AF_cur = 0

        # Convert the angle to radians
        angle = angle * np.pi / 180

        # Sum each of the elements for a specific angle
        for y, z, p, normal_vector_angle in R:

            #print("y, z : ", y, z)
            #print(y)
            if p > 1:

                # Playing parameters
                alpha = 0#leakage_retriever(p)
                I_0 = 1 # equal excitation

                # Convert y and z to mm
                y = y * (10**-3)
                z = z * (10**-3)
                p = p * (10**-3)

                #print(p)

                theta_naught = desired_angle * np.pi / 180
                # The dot product of hat(r) and vec(r)_i
                d = np.sin(angle)*y + np.cos(angle)*z
                d2 = np.sin(theta_naught)*y + np.cos(theta_naught)*z

                # The excitation
                I_n = 1

                # The final array factor for a specific angle
                AF_cur += I_n*np.exp(1j * k_0 * d)  * np.exp(-1j * k_0 * d2)

        AF.append(AF_cur)

    return AF

def retrieve_element_factor(filename):
    """
    Retrieve the element pattern from an hfss simulation and store it in an array
    :param filename:
    :return:
    """

    pass


# Create a numpy array from -90 to 90 with 1000 elements
theta = np.linspace(-90, 90, 1000)

# Plot with grid on
plt.grid()

#####################
# Planar leaky-wave #
#####################

pointing_direction = 0 # Degrees

AF = compute_planar_af(theta, dy, pointing_direction)
plt.plot(theta, 10*np.log(np.abs(AF)/np.max(np.abs(AF))), label="planar-array-factor")
plt.title("Planar LWA Directivty")
plt.ylabel("Normalized Directivity (dB)")
plt.xlabel("Theta (degrees)")
plt.legend()
plt.savefig("R:\\Code Repository\\Spline LWA project\\output\\planar-array-factor-alone", dpi=450)
plt.clf()

FILENAME = "output/extracted_antenna_parameters.xlsx"

R = parse_extracted_antenna_parameters(FILENAME)

# Spline leaky-wave
plt.grid()
AF = compute_spline_af(theta, R, 0)
plt.plot(theta, 10*np.log(np.abs(AF)/np.max(np.abs(AF))), label="Array Factor")
plt.legend()
#plt.plot(theta, AF)
plt.xlim([-90, 90])
plt.title("Spline-LWA Array Factor")
plt.savefig("R:\\Code Repository\\Spline LWA project\\output\\spline-array-factor-alone", dpi=450)
