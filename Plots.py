import matplotlib.pyplot as plt
import numpy as np


def thermalization():

    # Value of magnetization for each config
    mag = np.loadtxt("magnetisation.csv")

    # indice of the current config
    indice = np.arange(1,len(mag)+1)

    fig, ax = plt.subplots()

    ax.plot(indice,mag)

    ax.set_xlabel("Indice")
    ax.set_ylabel("Magnetization M")

    energy = np.loadtxt("energy.csv")

    fig, ax1 = plt.subplots()

    ax1.plot(indice,energy)

    ax1.set_xlabel("Indice")
    ax1.set_ylabel("Energy H")

    plt.show()



def magnetization_plot():

    # x axis
    temperature = [1,2,3,4,5,6,7,8,9,10]

    # y axis
    magnetization = [43,42,39.5,37,34,31,29,28,27.5,27.25]
    #w/ error bars
    mag_err = [1,1,1.4,2,2.3,1.3,1.5,1.6,1.2,1]

    fig, ax = plt.subplots()

    ax.errorbar(temperature, magnetization, mag_err)

    ax.set_xlabel("Temperature (k_b T)/J")
    ax.set_ylabel("Exp value of magnetization <M>")

    plt.show()


def average():

    mag_all = 0
    mag_array = np.loadtxt("magnetisation.csv")

    for i in range(150,1000):
        mag_all += mag_array[i]

    mean_mag = 1/(1000 - 150)*mag_all

    energy_all = 0
    energy_array = np.loadtxt("energy.csv")

    for i in range(150,1000):
        energy_all += energy_array[i]

    mean_energy = 1/(1000 - 150)*energy_all

    return mean_mag, mean_energy 

def varying_b_beta():

    mag_arrays = np.loadtxt("magnetisation_varying_b_beta.txt", delimiter = '\n')
    b_values = mag_arrays[0]
    beta_values = np.linspace(0.1,5,49)
    mag_array = np.array(x.split(',') for x in mag_arrays)

    plt.plot(beta_values, mag_array[1])
    



thermalization()

mean_mag,mean_energy = average()
print("Mean magnetisation : ", mean_mag)
print("Mean energy : ", mean_energy)