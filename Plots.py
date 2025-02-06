import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
import pandas as pd

"""def split_large_csv():
    for i,chunk in enumerate(pd.read_csv('energy.csv', chunksize=501000)):
        filename = f'energy_{i}.csv'
        chunk.to_csv(filename, index=False)
        print(f'created: {filename}')

    for j,chunk in enumerate(pd.read_csv('magnetisation.csv', chunksize=501000)):
        filename = f'magnetisation_{j}.csv' 
        chunk.to_csv(filename, index=False)
        print(f'created: {filename}')


split_large_csv()"""



def plot_data_subset(start_line: int=2, end_line: int=1002):
    data = pd.read_csv('energy_27.csv').iloc[start_line:end_line+1]

    plt.figure(figsize=(10,6))

    for col in data.columns:
        plt.plot(data[col].values, label='Energy')

    plt.xlabel('Configuration')
    plt.ylabel('Energy')
    plt.title('Energy')

    ax = plt.gca()
    ax.yaxis.set_major_locator(MaxNLocator(nbins=10))  # Maximum 10 y-ticks

    plt.show()

plot_data_subset(start_line=2, end_line=1002)

"""def thermalization():

    # Value of magnetization for each config
    mag = np.loadtxt("magnetisationdata.csv")

    # indice of the current config
    indice = np.arange(1,len(mag)+1)

    fig, ax = plt.subplots()

    ax.plot(indice,mag)

    ax.set_xlabel("Indice")
    ax.set_ylabel("Magnetization M")

    energy = np.loadtxt("energydata.csv")

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
    mag_array = np.loadtxt("magnetisationdata.csv")

    for i in range(150,1000):
        mag_all += mag_array[i]

    mean_mag = 1/(1000 - 150)*mag_all

    energy_all = 0
    energy_array = np.loadtxt("energydata.csv")

    for i in range(150,1000):
        energy_all += energy_array[i]

    mean_energy = 1/(1000 - 150)*energy_all

    return mean_mag, mean_energy 


#thermalization()

mean_mag,mean_energy = average()
print("Mean magnetisation : ", mean_mag)
print("Mean energy : ", mean_energy)"""