import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
import pymysql

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


pH = []
db = pymysql.connect(host='20.214.188.216', port=3306, user='root', password='Wx123456.', db='aquadatabase',
                     charset='utf8')
cursor = db.cursor()

#Generates an example dataset
sql_pH = "select ph from web_ph";
cursor.execute(sql_pH)
results_pH = cursor.fetchall()

for i in results_pH:

    for p in i:
        p = float(p)
        pH.append(p)

db.commit()
cursor.close()
db.close()
print(pH)

time = pd.DataFrame(times, columns = ['Time'])
print(time)

temperature_data = pd.DataFrame(water_temps, columns = ['Temperature'])
print(temperature_data)

pH_data = pd.DataFrame(pH, columns = ['pH'])
print(pH_data)

oyster_data = pd.concat([time, temperature_data, pH_data], axis = 1)
print(oyster_data)

#oyster_data.to_csv("../datasets/oyster_data.csv")

oyster_data.plot(x = "Time", y = "Temperature")
plt.xticks(rotation=0, fontsize=15)
plt.yticks(rotation=0, fontsize=15)
plt.ylabel('Temperature')
plt.xlabel('Time(hour)')
plt.title('Hourly Temperature Of The Water in the {} Region Over A 24 Hour Period'.format(location))

oyster_data.plot(x = "Time", y = "pH")
plt.xticks(rotation=0, fontsize=15)
plt.yticks(rotation=0, fontsize=15)
plt.ylabel('pH')
plt.xlabel('Time(hour)')
plt.title('Hourly pH Of The Water in the {} Region Over A 24 Hour Period'.format(location))


bounds = [0,4,7,10,12,14]
colors = ["red", "yellow", "green", "blue", "purple"]
cmap = matplotlib.colors.ListedColormap(colors)
norm = matplotlib.colors.BoundaryNorm(bounds, len(colors))

fig, ax = plt.subplots()
sc = ax.scatter(oyster_data.Time, oyster_data.pH, c=oyster_data.pH.values, cmap=cmap, norm=norm)
ax.plot(oyster_data.Time, oyster_data.pH)
fig.colorbar(sc, spacing="proportional")
plt.xticks(rotation=0, fontsize=15)
plt.yticks(rotation=0, fontsize=15)
plt.ylabel('pH')
plt.xlabel('Time(hour)')
plt.title('Line Graph Showing the Hourly pH Of The Water in the {} Region Over A 24 Hour Period'.format(location))


bounds = [0,12,20,25,35,50]
colors = ["blue", "lightblue", "yellow", "orange", "red"]
cmap = matplotlib.colors.ListedColormap(colors)
norm = matplotlib.colors.BoundaryNorm(bounds, len(colors))

fig, ax = plt.subplots()
sc = ax.scatter(oyster_data.Time, oyster_data['Temperature'], c=oyster_data.Temperature.values, cmap=cmap, norm=norm)
ax.plot(oyster_data.Time, oyster_data.Temperature)
fig.colorbar(sc, spacing="proportional")
plt.xticks(rotation=0, fontsize=15)
plt.yticks(rotation=0, fontsize=15)
plt.ylabel('Temperature')
plt.xlabel('Time(hour)')
plt.title('Line Graph Showing the Hourly Temperature Of The Water in the {} Region Over A 24 Hour Period'.format(location))















