import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors

from pylab import rcParams

rcParams['figure.dpi'] = 350
rcParams['lines.linewidth'] = 2
rcParams['axes.facecolor'] = 'white'
rcParams['patch.edgecolor'] = 'white'
rcParams['font.family'] = 'StixGeneral'

times = []
start_time, end_time = 0, 23

if start_time < end_time:
    times.extend(range(start_time, end_time))
    times.append(end_time)

#location = input("Enter your location:")
location = 'Mahurangi Harbour'

temperature = 0
water_temps = []

for i in range(24):
    temperature = np.random.randint(0, 50)
    #temperature = int(input("Temperature(℃)"))
    #print(temperature,"℃")
    water_temps.append(temperature)

pH = 0
pHs = []

for i in range(24):
    pH = np.random.randint(0, 14)
    #pH = int(input("pH:"))
    #print(pH)
    pHs.append(pH)

time = pd.DataFrame(times, columns = ['Time'])
print(time)

temperature_data = pd.DataFrame(water_temps, columns = ['Temperature'])
print(temperature_data)

pH_data = pd.DataFrame(pHs, columns = ['pH'])
print(pH_data)

oyster_data = pd.concat([time, temperature_data, pH_data], axis = 1)
print(oyster_data)

#oyster_data.to_csv("../datasets/oyster_data.csv")







