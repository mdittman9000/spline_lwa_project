import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import xlrd
import math

c = 3E8  # m/s
f = 27E9  # Hz
lam = c/f  # wavelength
k = 2*np.pi/lam  # wavenumber
beta = 0
planar_periodicity = 5E-3 # m
N = 27  # Number of elements

FILENAME = "output/extracted_antenna_parameters.xlsx"

def leakage_retriever(periodicity):

    dy = [4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6, 6.1, 6.2, 6.3,
          6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 7, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 8]

    min = math.inf
    min_index = 0

    for i in range(0, len(dy)):

        diff = abs(dy[i] - periodicity)

        if diff < min:
            min = diff
            min_index = i


    alpha_over_knaught = [0.005761349, 0.01544223, 0.015484701, 0.010806276, 0.007795475, 0.007155208, 0.008200802,
                          0.008052201, 0.007402886, 0.007323576, 0.006912635, 0.005923797, 0.005828093, 0.004921677,
                          0.00461025, 0.004803124, 0.004001749, 0.004398749, 0.004491214, 0.004298364, 0.004161314,
                          0.003968462, 0.003498085, 0.00382274, 0.005282073, 0.001290923, 0.000971322, 0.000932831,
                          0.001234667, 0.00174391, 0.001974021, 0.002315732, 0.002357862, 0.002188281, 0.002477857,
                          0.002738564, 0.002426412, 0.002562889, 0.002479492, 0.002436988]

    return k * alpha_over_knaught[min_index]
def parse_extracted_antenna_parameters(filename):
    file = filename
    df = pd.read_excel(file, usecols='B,C,E,H')

    print(df)

    # Distance array
    d = []

    for i in range(0, len(df) - 1):

        d.append((df.iloc[i][0], df.iloc[i][1], df.iloc[i][3], df.iloc[i][6]))

    return d

def parse_extracted_antenna_parameters_2(filename):
    file = filename
    df = pd.read_excel(file, usecols='B,C')

    # Distance array
    d = []

    for i in range(0, len(df) - 1):

        d.append(np.sqrt(df.iloc[i][0]**2 + df.iloc[i][1]**2))

    return d

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
    return 6.14702119153055 + (5.83245977360812*pow(10, -2)*angle_to_bend) + (6.1885747242777*(pow(10, -4)*(angle_to_bend**2))) + (3.27556335842171*(pow(10, -6))*(angle_to_bend**3)) + (-1.01273660742494*pow(10, -7)*(angle_to_bend**4)) + (-4.02657714686286*pow(10, -9)*(angle_to_bend**5)) + (-5.28348954913997*pow(10, -11)*(angle_to_bend**6)) + (-2.37380794347022*pow(10, -13)*(angle_to_bend**7))


def compute_planar_af(theta, periodicity):
    """
    Compute the array factor of the spline
    :return:
    """

    AF = []

    for angle in theta:

        AF_cur = 0

        # Sum each of the elements
        for n in range(1, N):
            alpha = 2.5
            I_n = np.exp(-alpha*(n - 1)*periodicity)
            q = -1
            beta_naught = 1.7
            x = (beta_naught - (q*2*np.pi/periodicity))/k
            #print(x)
            theta_naught = (-26)*np.pi/180
            Xi = -(n - 1)*k*periodicity*np.sin(theta_naught)
            AF_cur += I_n * np.exp( (1j * (n - 1) * k * periodicity * np.sin(angle)) + (1j * Xi))

        AF.append(AF_cur)

    return AF

def compute_planar_af_2(theta, periodicity):
    """
    Compute the array factor of the spline
    :return:
    """

    AF = []

    for angle in theta:

        AF_cur = 0

        # Sum each of the elements
        for n in range(1, N):
            alpha = 2.5
            I_n = np.exp(-alpha*(n - 1)*periodicity)
            q = -1
            beta_naught = 1.7
            x = (beta_naught - (q*2*np.pi/periodicity))/k #Naming a variable "periodicity" is fucking mental, name it p man!!!
            #print(x)
            theta_naught = (-26)*np.pi/180
            Xi = -(n - 1)*k*periodicity*np.sin(theta_naught)
            psi = k * periodicity * np.cos(angle) + Xi
            AF_cur += I_n * np.exp( (1j * (n-1)*psi))

        AF.append(AF_cur)

    return AF

def compute_spline_af(theta, R):
    """
    Compute the array factor of the spline
    :return:
    """

    AF = []

    for angle in theta:

        AF_cur = 0

        # Sum each of the elements
        for y, z, p, t in R:
            alpha = leakage_retriever(p)

            y = y * (10**-3)
            z = z * (10**-3)

            d = np.sin(angle) * y + np.cos(angle) * z

            print(d)
            theta_naught = (15) * np.pi / 180
            Xi = -k * d * np.sin(theta_naught)
            AF_cur += (np.exp(-alpha * d)) * (np.exp(1j * d * k * np.sin(angle))) * (np.exp(1j * Xi))

        AF.append(AF_cur)

    return AF

def compute_spline_af_alpha_variation(theta, R):
    """
    Compute the array factor of the spline
    :return:
    """


    for alpha in range(0, 20):

        print("Computing...alpha = ", alpha)
        AF = []

        for angle in theta:

            AF_cur = 0

            # Sum each of the elements
            for d in R:
                d = d * (10**-3)
                #print(d)
                theta_naught = (15) * np.pi / 180
                Xi = -k * d * np.sin(theta_naught)
                print(Xi)
                AF_cur += (np.exp(-alpha * d)) * (np.exp(1j * d * k * np.cos(angle))) * (np.exp(1j * Xi))

            AF.append(AF_cur)

        plt.polar(theta, 10 * np.log(np.abs(AF) / np.max(np.abs(AF))))
        plt.title("Alpha = " + str(alpha))
        ax1 = plt.gca()
        ax1.set_theta_zero_location("N")
        ax1.set_theta_direction(-1)
        plt.savefig("output\\array_theory_alpha_variation\\alpha=" + str(alpha))
        plt.clf()
def compute_planar_af_3(theta, p):
    """
    Compute the array factor of the spline
    :return:
    """

    AF = []

    for angle in theta:

        AF_cur = 0

        # Sum each of the elements
        for n in range(1, N):
            alpha = 2.5

            theta_naught = (-26)*np.pi/180
            Xi = -(n - 1) * k * p * np.sin(theta_naught)
            AF_cur += (np.exp(-alpha*(n - 1) * p)) * (np.exp(1j * (n-1) * k * p * np.sin(angle))) * (np.exp(1j * Xi))

        AF.append(AF_cur)

    return AF

print("K_0 : ", k)
theta = np.linspace(-np.pi / 2, np.pi / 2, 1000)
R = parse_extracted_antenna_parameters(FILENAME)
# Alpha variation for spline-leaky
#compute_spline_af_alpha_variation(theta, R)

# Planar leaky-wave
AF = compute_spline_af(theta, R)
plt.polar(theta, 10*np.log(np.abs(AF)/np.max(np.abs(AF))))
plt.title("Planar LWA, p = 5mm")
ax1 = plt.gca()
ax1.set_theta_zero_location("N")
ax1.set_theta_direction(-1)
plt.show()
"""
theta_save = np.array(theta)  # Theta
AF_save = np.array(10*np.log(np.abs(AF)/np.max(np.abs(AF))))  # db10 normalized AF
save_array = theta_save, AF_save
df = pd.DataFrame(save_array).T
df.to_excel(excel_writer = "output/array_theory_computation_planar.xlsx")
#plt.show()
plt.clf()

# Spline
R = parse_extracted_antenna_parameters(FILENAME)
print(R)
AF = compute_spline_af(theta, R)
plt.polar(theta, 10*np.log(np.abs(AF)/np.max(np.abs(AF))))
plt.title("Spline LWA")
ax1 = plt.gca()
ax1.set_theta_zero_location("N")
ax1.set_theta_direction(-1)

theta_save = np.array(theta)  # Theta
AF_save = np.array(10*np.log(np.abs(AF)/np.max(np.abs(AF))))  # db10 normalized AF
save_array = theta_save, AF_save
df = pd.DataFrame(save_array).T
df.to_excel(excel_writer = "output/array_theory_computation_spline.xlsx")
plt.show()
plt.clf()
"""