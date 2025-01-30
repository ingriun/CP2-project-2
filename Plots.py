import matplotlib.pyplot as plt
import numpy as np


def thermalization():

    # Value of magnetization for each config
    config = np.loadtxt("magnetisation.csv")
    print(config)

    # indice of the current config
    indice = np.arange(1,len(config)+1)

    fig, ax = plt.subplots()

    ax.plot(indice,config)

    ax.set_xlabel("Indice")
    ax.set_ylabel("Magnetization M")

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

thermalization()