import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import xlrd

c = 3E8  # m/s
f = 27E9  # Hz
lam = c/f  # wavelength
k = 2*np.pi/lam  # wavenumber
beta = 0
planar_periodicity = 5E-3  # m
element_number = 40

FILENAME = "output/extracted_antenna_parameters.xlsx"

def parse_extracted_antenna_parameters(filename):
    file = filename
    df = pd.read_excel(file, usecols='B,C')

    # Distance array
    d = []

    for i in range(0, len(df) - 1):

        d.append(np.sqrt(df.iloc[i][0]**2 + df.iloc[i][1]**2))

    return d

def compute_planar_af(theta, periodicity):
    """
    Compute the array factor of the spline
    :return:
    """

    # Variable to store array fator
    AF_res = []

    # Calculate the array factor for every angle
    for angle in theta:

        AF = 0  # The current array factor

        # Calculate the array factor for all the elements
        for n in range(1, element_number):

            print(n * periodicity)

            AF += np.exp(1j * (n - 1) * k * periodicity * np.cos(angle) + beta)

        # Append the
        AF_res.append(AF)

    # Return the array factor
    return AF_res

def compute_spline_af(theta, R):
    """
    Compute the array factor of the spline
    :return:
    """

    # Variable to store array fator
    AF_res = []

    # Calculate the array factor for every angle
    for angle in theta:

        AF = 0  # The current array factor

        # Calculate the array factor for all the elements
        for d in R:

            AF += np.exp(1j * k * d * np.cos(angle) + beta)

        # Append the
        AF_res.append(AF)

    # Return the array factor
    return AF_res

def get_directive_gain(g, minDdBi=-40):
    """Return the "directive gain" of the antenna array producing gain g."""
    DdBi = 10 * np.log10(g / np.max(g))
    return np.clip(DdBi, minDdBi, None)

# Theta that we want to look at
theta = np.linspace(-np.pi, np.pi, 1000)

# Compute the planar array factor
planar_af = compute_planar_af(theta, planar_periodicity)
plt.polar(theta, planar_af)
plt.title("Array Factor - Planar")
ax1 = plt.gca()
ax1.set_theta_zero_location("N")
plt.show()
plt.clf()

# Parse data for spline
d_arr = parse_extracted_antenna_parameters(FILENAME)
print("Distances from origin to slot center : ", d_arr)

spline_af = compute_spline_af(theta, d_arr)
plt.polar(theta, spline_af)
plt.title("Array Factor - Spline")
ax1 = plt.gca()
ax1.set_theta_zero_location("N")
plt.show()
plt.clf()

# Parse data for spline
d_arr = parse_extracted_antenna_parameters(FILENAME)
print("Distances from origin to slot center : ", d_arr)
