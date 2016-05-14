import matplotlib.pyplot as plt
import seaborn as sns

with open("result_snow_2.txt") as fobj:
	data = fobj.readlines()

snow = []
duration = []
trip = []

for line in data:
	line = line.strip()
	key, value = line.split('\t')
	snow.append(float(key))
	duration.append(float(value.split(',')[0]))
	trip.append(float(value.split(',')[1]))

plt.figure(figsize=(20, 16)) 
ax = plt.subplot(111)
ax.plot(snow, duration, color = 'mediumpurple', label = 'Trip Duration', linewidth = 4)
ax2 = ax.twinx()
ax2.plot(snow, trip, color = 'r', label = 'Number of Trips', linewidth = 4)
ax.grid()
ax.set_xlabel("Snow Depth", fontsize = 26)
ax.set_ylabel("Trip Duration", color = 'mediumpurple', fontsize = 26)
ax2.set_ylabel("Number of Trips", color = 'r', fontsize = 26)
ax.tick_params(axis = 'both', labelsize = 16)
ax2.tick_params(axis = 'both', labelsize = 16)
ax.set_title('Number of Trips, Trip Duration vs. Snow Depth', fontsize = 32)
plt.savefig('try_snow.png')