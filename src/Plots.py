import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
import pandas as pd
import csv
import random

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


def calculate_mean_and_error(csv_filename: str, start_config: int=100, end_config: int=1000):
    replica_means = []
    current_replica_data = []

    with open(csv_filename, 'r') as file:
        reader = csv.reader(file)
        
        for row in reader:
            if not row:
                continue

            #detect start of a new replica
            if row[0] == '*':
                if current_replica_data:
                    #process the previous replica
                    process_replica_data(current_replica_data, replica_means, start_config, end_config)
                #reset for next replica and skip parameter line
                current_replica_data=[]
                inside_replica=True
                next(reader, None)  #skip parameter line
            else:
                    #collect values for current replica
                    try:
                        current_replica_data.append(float(row[0]))
                    except ValueError:
                        continue
        
        if current_replica_data:
            process_replica_data(current_replica_data, replica_means, start_config, end_config)

    #compute expectation value and error
    num_replicas = len(replica_means)
    
    expectation_value = np.mean(replica_means)
    statistical_error = np.sqrt((1/(num_replicas*(num_replicas-1)))*np.sum((replica_means-expectation_value)**2))

    print("Expectation Value:", expectation_value)
    print("Statistical Error:", statistical_error)
    return expectation_value, statistical_error

def process_replica_data(data, replica_means, start_config, end_config):
    """Process a single replica's data, compute the mean and append it to replica_means."""
    if len(data) >= end_config:
        thermalised_data = data[start_config:end_config]
        mean_value = np.mean(thermalised_data)
        replica_means.append(mean_value)


def plot_data_subset(csv_filename,start_line: int=2, end_line: int=1002):
    travel = [x*1002 for x in range(1,500)]

    N = random.choice(travel)
    print("N = ", N)

    data = pd.read_csv(csv_filename).iloc[start_line+N:end_line+1+N]  
    data = data.apply(pd.to_numeric, errors='coerce') 
    data = data.dropna()

    plt.figure(figsize=(10,6))

    for col in data.columns:
        plt.plot(data[col].values, label='Energy')

    plt.yscale('linear')  
    plt.ylim(data.min().min(), data.max().max())  
    plt.xlim(0,1000)
    plt.xlabel('Configurations')
    plt.ylabel('Energy')
    plt.title('Energy over 1000 Configurations')

    ax = plt.gca()
    ax.yaxis.set_major_locator(MaxNLocator(nbins=10))  # Maximum 10 y-ticks

    plt.show()


def magnetization_plot():

    # x axis
    mag = pd.read_csv("data/analysis/Analysis of files - Ark 1.csv").iloc[0:24]

    beta = mag['Beta'].tolist()
    print(beta)

    # y axis
    energy = mag['Mean_1'].tolist()
    print(energy) 

    #w/ error bars
    en_err = mag['Error_1'].tolist()

    fig, ax = plt.subplots()

    ax.errorbar(beta, energy, en_err)

    ax.set_xlabel("Temperature (k_b T)/J")
    ax.set_ylabel("Exp value of magnetisation <M>")

    plt.show()
#magnetization_plot()

csv_filename = 'data/energy/energydata.csv'
#plot_data_subset(csv_filename,start_line=2, end_line=1002)

calculate_mean_and_error(csv_filename,start_config=100, end_config=1000)

