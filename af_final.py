import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

c = 3E8  # m/s
f = 27E9  # Hz
lam = c/f  # wavelength
k_0 = 2*np.pi/lam  # wavenumber
planar_periodicity = 5E-3 # m
N = 55  # Number of elements

print("k_0", k_0)

simulation_filename_planar = "R:\\My Results\\Fall 2023\\Leaky-project\\Simulations\\array_theory_planar\\active\\planar-extended.csv"
simulation_filename_spline = "R:\\My Results\\Fall 2023\\Leaky-project\\Simulations\\spline-data\\leaky-spline-6\\data\\normalized\\-15.csv"

# Array theory graphing
SOURCE_DIR = "R:\\My Results\\Fall 2023\\Leaky-project\\Simulations\\array_theory_planar\\simulated directivity.csv"
OUTPUT_DIR = "R:\\Code Repository\\EM_grapher\\output\\spline_leaky_15_deg"

FIRST_SLOT_CENTER = 3E-3

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

    return k_0 * alpha_over_knaught[min_index]

def phase_retriever(periodicity):

    dy = [4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6, 6.1, 6.2, 6.3,
          6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 7, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 8]

    min = math.inf
    min_index = 0

    for i in range(0, len(dy)):

        diff = abs(dy[i] - periodicity)

        if diff < min:
            min = diff
            min_index = i


    beta_over_knaught = [-0.958819735,-0.917060074,-0.882947593,-0.833885822,-0.777145961,-0.725374371,-0.669130606,
                         -0.622514637,-0.580702956,-0.529919264,-0.49242356,-0.4539905,-0.414693243,-0.382683432,
                         -0.342020143,-0.3007058,-0.275637356,-0.233445364,-0.199367934,-0.173648178,-0.139173101,
                         -0.113203214,-0.087155743,-0.06104854,-0.017452406,-0.008726535,-0.008726535,0,0.043619387,
                         0.069756474,0.095845753,0.121869343,0.139173101,0.156434465,0.182235525,0.199367934,
                         0.216439614,0.233445364,0.250380004,0.267238376]


    return k_0 * beta_over_knaught[min_index]

def parse_extracted_antenna_parameters(filename):
    file = filename
    df = pd.read_excel(file, usecols='B,C,E,H')

    print(df)

    # Distance array
    d = []

    for i in range(0, len(df) - 1):

        d.append((df.iloc[i][0], df.iloc[i][1], df.iloc[i][3], df.iloc[i][6]))

    return d

def read_hfss(filename):
    """
    Read the directivity file exported by hfss
    :param filename: The filename to read as a .csv file. There are FOUR EXPECTED COLUMNS (frequency, theta, phi, directivity)
    :return:
    """

    # Open the filename
    f = open(filename)

    # Store the outputs
    arr0 = {}
    arr1 = {}
    arr2 = {}
    arr3 = {}

    name0 = "no name"
    name1 = "no name"
    name2 = "no name"
    name3 = "no name"

    count = 0

    # Iterate through the content of the file
    for line in f:

        content = line.split(",")

        # Debugging to see the data
        # print(content)

        if count == 0:

            # Record the names of the data series
            name0 = content[0]
            name1 = content[1]
            name2 = content[2]
            name3 = content[3]

            arr0[name0] = []
            arr1[name1] = []
            arr2[name2] = []
            arr3[name3] = []

        else:

            # Append the
            arr0[name0].append(content[0])
            arr1[name1].append(content[1])
            arr2[name2].append(float(content[2]))
            arr3[name3].append(float(content[3]))

        count += 1

    #print(arr3)

    return arr0, arr1, arr2, arr3

def plot_hfss(x, y, filename):
    """
    Plot two x and y variables against each other
    :param x:
    :param y:
    :return:
    """

    name = create_legend_name(filename)

    plt.plot(x, y, label=name, color='red', linewidth=1)
    plt.xlim([-90, 90])
    plt.legend()
    plt.xlabel("Theta (\N{DEGREE SIGN})", fontsize=14)
    plt.ylabel("Normalized Directivity (dB)", fontsize=14)
    plt.grid()

def create_legend_name(filename):
    """
    Create the name of the legend for the current file
    :param filename:
    :return:
    """

    content = filename.split("\\")

    print(content)

    last = content[len(content)-1].split(".")[0]

    print(last)

    name = ""

    item_counter = 0
    for item in last.split("_"):

        if item_counter != 0:
            name += "-" + item
        else:
            name += item

        item_counter += 1

    return name

def compute_planar_af(theta, p):
    """
    Compute the array factor of the spline
    :return:
    """

    AF = []

    for angle in theta:

        AF_cur = 0

        angle = angle * np.pi/180

        # Sum each of the elements
        for n in range(1, N):
            alpha = 3.95
            I_0 = 2
            theta_naught = (-26)*np.pi/180
            Xi = -(n - 1) * k_0 * p * np.sin(theta_naught)
            I_n = I_0*(np.exp(-alpha*(n - 1) * p))
            AF_cur += I_n * (np.exp(1j * k_0 * ((n-1) * p) * np.sin(angle))) * (np.exp(1j * Xi))

        AF.append(AF_cur)

    return AF

def compute_planar_af_2(theta, p, pointing_angle):
    """
    Compute the array factor of the spline
    :return:
    """

    AF = []

    for angle in theta:

        AF_cur = 0

        angle = angle * np.pi/180

        # Sum each of the elements
        for n in range(1, N):
            alpha = 5.9217
            print(alpha)
            I_0 = 1
            theta_naught = (pointing_angle)*np.pi/180
            beta = ((n-1) * p + FIRST_SLOT_CENTER) * k_0 * np.sin(theta_naught)
            I_n = I_0*(np.exp(-alpha*((n-1) * p + FIRST_SLOT_CENTER) - 1j * beta))
            AF_cur += I_n * (np.exp(1j * k_0 * ((n-1) * p + FIRST_SLOT_CENTER) * np.sin(angle)))

        AF.append(AF_cur)

    return AF

def compute_planar_af_check(theta, p, pointing_angle):
    """
    Compute the array factor of the spline
    :return:
    """

    AF = []
    theta_naught = (pointing_angle) * np.pi / 180

    for angle in theta:

        AF_cur = 0

        angle = angle * np.pi/180

        # Sum each of the elements
        for n in range(1, N):
            alpha = 5.9217
            I_0 = 1
            d = ((n-1) * p + FIRST_SLOT_CENTER)
            beta = k_0 * np.sin(theta_naught)
            gamma = beta - 1j*alpha
            I_n = np.exp(-alpha*d)
            AF_cur += I_n * (np.exp(1j * k_0 * d * np.sin(angle))) * np.exp(-1j*d*beta)

        AF.append(AF_cur)

    return AF

def compute_spline_af(theta, R, desired_angle):
    """
    Compute the array factor of the spline
    :return:
    """

    AF = []

    # Loop through all the angles we want to calculate the array factor at
    for angle in theta:

        AF_cur = 0

        # Convert the angle to radians
        angle = angle * np.pi / 180

        #print("XXXX Angle XXXX", angle)

        # Sum each of the elements for a specific angle
        for y, z, p, normal_vector_angle in R:

            #print("y, z : ", y, z)
            #print(y)
            if p > 4.3:

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
                #r = 1
                #R_n = np.sqrt((r*np.sin(angle) - y*np.sin(angle))**2 + (r*np.cos(angle) - z*np.cos(angle))**2)
                #d = d * R_n
                #print(d)

                # Beta
                #beta = - k_0 * d * np.sin(theta_naught)
                #print("beta, k_0", beta, k)
                # Gamma
                #gamma = 1j * alpha + beta

                # The excitation
                I_n = np.exp(-alpha*d)

                # The final array factor for a specific angle
                AF_cur += I_n*np.exp(1j * k_0 * d) * np.exp(-1j * k_0* d2)


        AF.append(AF_cur)

    return AF

# Planar Leaky-wave graphing
frequency, phi, theta, normalized_directivity = read_hfss(simulation_filename_planar)

x = theta['"Theta [deg]"']
y = normalized_directivity['"dB10normalize(DirTotal) []"\n']
plot_hfss(x, y, simulation_filename_planar)

theta = np.linspace(-180, 180, 1000)

# Planar leaky-wave
AF = compute_planar_af_check(theta, planar_periodicity, -28.7)
plt.plot(theta, 10*np.log(np.abs(AF)/np.max(np.abs(AF))), label="Theoretical-planar-array-factor")
plt.title("Planar LWA Directivty")
plt.legend()
plt.savefig("R:\\Code Repository\\Spline LWA project\\output\\planar-array-factor", dpi=450)
plt.clf()

# Spline leaky-wave graphing
FILENAME = "output/extracted_antenna_parameters.xlsx"
frequency, phi, theta, normalized_directivity = read_hfss(simulation_filename_spline)
x = theta['"Theta [deg]"']
y = normalized_directivity['"dB10normalize(DirTotal) []"\n']
plot_hfss(x, y, simulation_filename_spline)

theta = np.linspace(-90, 90, 1000)

R = parse_extracted_antenna_parameters(FILENAME)
# Alpha variation for spline-leaky
AF = compute_spline_af(theta, R, -15)
plt.plot(theta, 10*np.log(np.abs(AF)/np.max(np.abs(AF))), label="Theoretical-spline-array-factor")
plt.legend()
#plt.plot(theta, AF)
plt.xlim([-90, 90])
plt.title("Spline LWA Directivity")
plt.savefig("R:\\Code Repository\\Spline LWA project\\output\\spline-array-factor", dpi=450)
