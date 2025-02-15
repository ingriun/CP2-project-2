import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
import pandas as pd
import seaborn as sns
import csv
import random

#################### Splitting large files into smaller chunks ##############################

def split_large_csv():
    for i,chunk in enumerate(pd.read_csv('data/energy_task2.csv', chunksize=1002)):
        filename = f'data/task2/energy_task2_{i}.csv'
        chunk.to_csv(filename, index=False)
        print(f'created: {filename}')

    for j,chunk in enumerate(pd.read_csv('data/magnetisation_task2.csv', chunksize=1002)):
        filename = f'data/task2/magnetisation_task2_{j}.csv' 
        chunk.to_csv(filename, index=False)
        print(f'created: {filename}')

#split_large_csv()

######################### Statistical Analysis ################################################

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


#csv_filename = 'data/energy/energydata.csv'
#calculate_mean_and_error(csv_filename,start_config=100, end_config=1000)

############################## Plots ###########################################

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
    plt.xlim(0,100000)
    plt.xlabel('Configurations')
    plt.ylabel('Energy')
    plt.title('Energy over 1000 Configurations')

    ax = plt.gca()
    ax.yaxis.set_major_locator(MaxNLocator(nbins=10))  # Maximum 10 y-ticks

    plt.show()

#plot_data_subset(csv_filename,start_line=2, end_line=1002)

def task4():
    energies = np.zeros(500)
    magnetisation = np.zeros(500)
    for i in range(0, 500):
        filename = f'data/task2/energy_task2_{i}.csv'
        data = pd.read_csv(filename)
        data = data.apply(pd.to_numeric, errors='coerce') 
        data = data.dropna()
        thermalised_data = data.iloc[200:1002]
        energies[i] = np.mean(thermalised_data)

        filename = f'data/task2/magnetisation_task2_{i}.csv'
        data = pd.read_csv(filename)
        data = data.apply(pd.to_numeric, errors='coerce') 
        data = data.dropna()
        thermalised_data = data.iloc[200:1002]
        magnetisation[i] = np.mean(thermalised_data)

    plt.figure()
    plt.hist(energies)
    plt.show()

    plt.figure()
    plt.hist(magnetisation)
    plt.show()

def final_plot():
    x = [10, 5.0, 4.6, 4.2, 3.8, 3.4, 1/0.3, 3.0, 2.8, 2.6, 2.4, 2.2,1/0.5, 1/0.7, 1/0.9, 1/1.1, 1/1.3, 1/1.5, 1/1.7, 1/1.9, 1/2.1, 1/2.3, 1/2.5, 1/2.7, 1/2.9, 1/3.1, 1/3.3, 1/3.5, 1/3.7, 1/3.9, 1/4.1, 1/4.3, 1/4.5, 1/4.7] # Shared X-axis values
   
    """Expectation Values of the Magnetisation for different b"""
    """
    # Dataset 1: b=0.01
    y1 = [156.7661, 285.377915, 325.16157, 384.4177, 482.2113, 671.72622, 720.7546, 1145.4566, 1729.3776, 3138.5396, 6126.8686, 8316.1482, 9161.3095, 9386.7449, 9049.4680, 8455.9671, 7947.4597, 7866.8933, 7990.5107, 8038.1568, 7908.1914, 7510.4477, 7611.8665, 7014.9385, 6776.9865, 7458.9634, 7353.4580, 7264.3459, 7297.3389, 7140.2847, 7861.3086, 7598.7323, 7240.1511, 7111.6231]
    y1_err = [0.0811, 0.216966, 0.25581, 0.321205, 0.417833, 0.64840, 0.6951, 1.8099, 1.1778448, 3.3247, 3.1133, 0.8243, 1.7501, 127.7027, 179.3196, 224.0626, 265.3931, 261.2306, 251.7684, 241.7665, 247.2677, 269.6901, 258.9316, 293.1543, 292.4698, 257.2117, 267.0550, 271.3180, 272.4467, 281.0468, 232.5742, 253.2783, 271.8849, 276.3810]

    # Dataset 2: b=0.005
    y2 = [78.31714514514515, 142.95505, 162.89134, 192.4652, 242.14071, 337.4762, 361.4178218218218, 575.6686, 888.1606, 1717.4756, 4808.3250, 8095.749, 9128.470954285714, 7338.162442352941, 6111.290805, 5601.437844444445, 5391.978071111111, 5644.2830977777785, 5629.539306666667, 5075.324903225805, 5608.0566, 4708.566724444445, 5052.368624, 4973.521582978724, 5073.001911111111, 5547.107400000001, 5405.857961290323, 5166.247415730338, 5604.942448351648, 5630.245854945054, 5226.733407058824, 5077.740969411764, 4826.124204444443, 4972.959069879518]
    y2_err = [0.08473541323298045, 0.206803, 0.241209, 0.325783, 0.4159578, 0.619693, 0.6874395866503207, 1.1692818, 2.0329, 4.1182, 7.4740, 4.0401, 7.258001450212403, 275.90079691722366, 335.00542169985516, 342.185668928879, 349.8458376726757, 336.0355392416955, 337.6325179895949, 355.0812313180567, 332.77461304084545, 352.048307354574, 341.90248118472425, 343.0431487688255, 345.34154828052624, 334.4541142528508, 340.92531726639925, 348.5171282983747, 325.30828740530734, 316.4447200820388, 331.3067240068973, 339.6628516569524, 346.77327255193165, 350.0276629785756]

    # Dataset 3: b=0.001
    y3 = [15.720679569892473, 28.7728, 32.53933, 38.67121, 48.0847, 65.48171, 72.82785376344086, 114.66770, 179.4444, 352.2539, 1467.1381, 5017.1862, 3237.963455, 1823.2732850000002, 2637.1861400000003, 1715.8343, 2026.5120, 1137.1679, 1945.6276, 1937.7196, 1596.2502, 2473.1680, 1988.6485, 2147.0743, 2961.8689, 2271.5070, 1929.2264, 1606.9699, 2648.3153, 1702.2428, 1935.4504, 2063.4440, 1727.5901, 2047.8770]
    y3_err = [0.08479804257949665, 0.21509, 0.26862, 0.289917, 0.41514, 0.65665, 0.7228088430257644, 1.209442, 2.0336, 4.4897, 21.0895, 170.4678, 303.26200472884955, 369.2404273138905, 365.4875863938588, 374.6054, 373.3554, 381.3670, 380.3008, 377.7174, 379.9338, 375.0293, 376.8473, 373.1786, 367.1076, 382.6425, 383.6268, 388.3524, 368.5916, 380.0359, 375.3544, 375.3650, 372.2609, 370.8920]

    # Dataset 4: b=0.0005
    y4 = [7.7451, 14.683220, 16.055955, 18.91602, 23.53986, 33.6544, 35.5426, 57.930395, 89.3564, 182.7226, 763.5307, 2620.0418, 1470.9197, 472.6266, 1557.0194, 1010.3156, 740.3874, 1191.7775, 1156.3880, 1127.8104, 1313.7213, 1316.2406, 1688.0742, 1148.0493, 957.5600, 930.6808, 1003.6951, 1478.3979, 662.6853, 1468.4117, 1407.8429, 1423.5662, 1807.3904, 885.1849]
    y4_err = [0.0912, 0.218457, 0.270122, 0.31421, 0.42292, 0.62369, 0.6792, 1.13514, 1.9825, 4.5686, 21.2410, 237.5818, 299.2747, 369.0469, 371.9930, 369.0915, 377.0551, 374.2065, 374.6586, 382.8237, 375.0042, 377.4513, 379.3516, 382.7934, 379.6210, 381.4431, 378.7182, 377.3910, 384.3179, 371.8375, 373.5338, 368.8810, 368.6745, 381.0934]
    """
    
    """Expectation Values of the Magnetisation for different b"""
    # Dataset 1: b=0.01
    y1 = [-205.2288, -205.2288,-861.28020, -1030.81509, -1258.2089178, -1574.067200, -2036.125212, -2766.63102, -3323.3949, -4159.0996, -5582.5426, -7302.7786, -8875.2375, -13838.8204, -18019.3970, -22043.2173, -26034.6432, -30026.7357, -34017.6027, -37987.1989, -41955.7324, -45936.9732, -49907.5674, -53901.3725, -57824.1902, -61832.8575, -65834.3661, -69826.3878, -73815.6024, -77799.2196, -81734.1429, -85762.6182, -89744.0797, -93690.5993]
    y1_err = [0.051, 0.051, 0.0796787, 0.0884969, 0.090999904, 0.09987071, 0.119190483, 0.149092667, 0.2278, 0.4637, 0.6649, 0.3863,0.3768, 2.4709, 2.5768, 3.6038, 4.6914, 5.398, 6.8905, 9.4379, 12.1261, 14.4401, 16.8662, 17.555, 21.2446, 22.3156, 23.1586, 24.2562, 25.4291, 26.8838, 30.4064, 30.0848, 31.5273, 34.1408]

    # Dataset 2: b=0.005
    y2 = [-203.88487866666665, -857.54430, -1026.3979, -1252.414487, -1565.78836, -2022.33524, -2118.861825816327,-2734.949130, -3264.5430,-4013.5415,-5309.1941,-7170.9261, -8798.682818125, -13750.917108705882, -17906.950688210523, -21936.080771276596, -25937.194481333336, -29908.026814222223, -33900.58337222222, -37881.13275, -41838.701147529406, -45796.51325, -49750.7627872, -53749.68039066666, -57758.19838933334, -61750.5099915, -65750.37803148935, -69729.69690666666, -73637.24476173913, -77578.85993044444, -81576.498478, -85599.73744257144, -89591.14283250002, -93609.77607317647]
    y2_err = [0.050935254809630084, 0.078836, 0.0841500, 0.087580307, 0.1075219, 0.120943, 0.12701805853197834, 0.1534702559, 0.1933,0.3361,0.9497,0.6680,1.0162441082774964, 3.3209489533820244, 4.7658458968974085, 6.579371267198739, 7.541997084636733, 9.900963648484877, 11.33641064490572, 12.889929990349602, 15.31256050775418, 17.65776671458938, 19.783208296478893, 21.358344622918068, 21.890730399209833, 23.277058220486882, 24.600549296929927, 26.003787450047408, 29.690467084999252, 32.06970791647609, 32.94671965784131, 33.366763108375956, 34.6613533026686, 35.29075742865984]

    # Dataset 3: b=0.001
    y3 = [-203.4492251816284, -856.4547, -1024.82570, -1250.3644, -1563.11894, -2018.05294, -2113.5536629387757, -2724.7525, -3244.1084,-3957.5938,-5038.7488,-6925.6073,-8621.473155464788, -13618.441108333333, -17792.268590107527, -21805.04175698925, -25783.7639744086, -29764.44576731183, -33759.80204903225, -37715.1469968421, -41684.42098294737, -45664.91552989474, -49615.11829913978, -53563.33059263158, -57567.49932860215, -61575.418202580644, -65518.494260645166, -69513.7300511828, -73432.4888711828, -77412.20537311828, -81346.42034580644, -85326.07704365591, -89249.43010537633, -93212.7042260215]
    y3_err = [0.04960027205177278, 0.081933, 0.084039, 0.0981879, 0.0991064, 0.1233786, 0.12914899409226266, 0.153753, 0.1939,0.2571,0.8053,5.0019, 6.223903077025688, 8.50161254071738, 9.809033979291968, 11.990038484375601, 13.990218730485873, 15.739624125701916, 17.258343133030312, 19.694992535481248, 21.691684766191564, 23.495483387656023, 25.961953267376458, 28.208848856268382, 29.635505700691294, 30.915955904191424, 33.6033133721113, 34.86350281482623, 37.8046384771575, 40.0415967642051, 42.39424740480247, 44.50146579063794, 47.22350711292453, 49.158678106146695]

    # Dataset 4: b=0.0005
    y4 = [-203.36451085591398, -856.461901, -1024.9908, -1250.4440, -1562.987, -2017.4273, -2113.517331655914, -2724.37706, -3243.7591,-3955.5806,-5022.2177,-6886.3678,-8603.066489436618, -13608.031460963857, -17783.781131182797, -21779.934889347827, -25765.39987543478, -29728.41099333333, -33695.616402365595, -37688.832111397845, -41628.20384129032, -45607.96192709677, -49596.27333397849, -53558.13304774193, -57500.93110301075, -61484.25624666667, -65434.72117763441, -69403.08762258064, -73395.88285612903, -77282.85373053764, -81261.0518544086, -85182.09831204302, -89177.8640260215, -93207.27341053763]
    y4_err = [0.050652149466343936, 0.0794506,  0.082653,  0.093873665, 0.1051532,  0.124359, 0.123129301312049, 0.156785, 0.1803,0.2663,0.5855,4.7008, 6.669813361934372, 8.779217990153736, 10.076230320653822, 12.790915072300304, 15.178942374401966, 17.49608043995081, 19.84805769589702, 21.61591964796352, 24.67813191381175, 26.454611826487767, 28.430538451704408, 30.77973926262959, 33.61351027391872, 35.65233012777676, 38.08752446933077, 40.55010968204552, 42.182066073659435, 45.73794816957652, 47.6969789048736, 50.78328678662141, 52.75907107200181, 53.54289285730968]
    
    # Plot each dataset with error bars
    plt.errorbar(x, y1, yerr=y1_err, fmt='o-', capsize=4, label='b=0.01', color='blue')
    plt.errorbar(x, y2, yerr=y2_err, fmt='s--', capsize=4, label='b=0.005', color='green')
    plt.errorbar(x, y3, yerr=y3_err, fmt='^-.', capsize=4, label='b=0.001', color='purple')
    plt.errorbar(x, y4, yerr=y4_err, fmt='d:', capsize=4, label='b=0.0005', color='orange')

    # Plot formatting
    plt.title('Magnetisation with Error Bars for different values of b and beta')
    plt.xlabel('kT/J')
    plt.ylabel('Expectation Value')
    plt.legend()
    plt.grid(True)

    # Show plot
    plt.show()

task4()

final_plot()

################################ Histograms for Probability Distributions ##########################

def load_data(file):
    data = []
    with open(file, "r") as f:
        for i, line in enumerate(f):
            if (i%1002) in [0,1]:
                continue
            data.append(float(line.strip()))
    return np.array(data)

dist1 = load_data('data/energy/energydata.csv')
dist2 = load_data('data/magnetisation/magnetisationdata.csv')

n_bins = 30

fix, axs = plt.subplots(1,2,sharey=True,tight_layout=True)

axs[0].hist(dist1, bins=n_bins, density=True, color='blue')
axs[0].set_title("Energy Probability Distribution")
axs[0].set_xlabel("Energy")
axs[0].set_ylabel("Probability Density")

axs[1].hist(dist2, bins=n_bins, density=True, color='red')
axs[1].set_title("Magnetisation Probability Distribution")
axs[1].set_xlabel("Magnetisation")

plt.show()