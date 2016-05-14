#!/usr/bin/python
import matplotlib.pyplot as plt
def data_graph(data_parse, month):
	plt.figure(figsize=(20, 16)) 
	ax = plt.subplot(211)
	ax.plot(range(24), data_parse[month]['0']['drivetime_male'], color = 'b', ls = '--', label = 'Male Duration (Good Weather)', linewidth = 2)
	ax.plot(range(24), data_parse[month]['1']['drivetime_male'], color = 'r', ls = '--', label = 'Male Duration (Bad Weather)', linewidth = 2)
	ax.plot(range(24), data_parse[month]['0']['drivetime_female'], color = 'b', label = 'Female Duration (Good Weather)', linewidth = 2)
	ax.plot(range(24), data_parse[month]['1']['drivetime_female'], color = 'r', label = 'Female Duration (Bad Weather)', linewidth = 2)
	ax.legend(loc=1)
	ax.grid()
	ax.set_xlabel("Time of Day", fontsize = 16)
	ax.set_ylabel("Trip Duration", fontsize = 16)
	ax.set_title('Trip Duration on Weekdays in ' + month, fontsize = 26)
	ax2 = plt.subplot(212)
	ax2.plot(range(24), data_parse[month]['0']['trip_male'], color = 'b', ls = '--', label = 'Male Number of Trips (Good Weather)', linewidth = 2)
	ax2.plot(range(24), data_parse[month]['1']['trip_male'], color = 'r', ls = '--', label = 'Male Number of Trips (Bad Weather)', linewidth = 2)
	ax2.plot(range(24), data_parse[month]['0']['trip_female'], color = 'b', label = 'Female Number of Trips (Good Weather)', linewidth = 2)
	ax2.plot(range(24), data_parse[month]['1']['trip_female'], color = 'r', label = 'Female Number of Trips (Bad Weather)', linewidth = 2)
	ax2.legend(loc=1)
	ax2.grid()
	ax2.set_xlabel("Time of Day", fontsize = 16)
	ax2.set_ylabel("Number of Trips", fontsize = 16)
	ax2.set_title('Number of Trips on Weekdays in ' + month, fontsize = 26)
	# ax5 = plt.subplot(313)
	# ax5.plot(range(24), data_parse[month]['0']['trip'], color = 'r', label = 'good trip')
	# ax5.plot(range(24), data_parse[month]['1']['trip'], color = 'y', label = 'bad trip')
	# ax6 = ax5.twinx()
	# ax6.plot(range(24), data_parse[month]['0']['drivetime'], color = 'g', label = 'good drivetime')
	# ax6.plot(range(24), data_parse[month]['1']['drivetime'], color = 'b', label = 'bad drivetime')
	# ax5.legend(loc='best')
	# ax6.legend(loc='best')
	# ax5.grid()
	# ax5.set_xlabel("Hours")
	# ax5.set_ylabel("Trip")
	# ax6.set_ylabel("Drivetime")
	# ax5.set_title('Trip and citi bike drivetime in ' + month)
	# plt.legend(loc='best')
	plt.savefig('try_gender.png')

with open('result_gender.txt') as fobj:
	data_init = fobj.readlines()
data_parse = {}
for line in data_init:
	line = line.strip()
	key, value = line.split('\t')
	data_parse.setdefault(key, {})
	badorgood = value.split(';')
	data_parse[key].setdefault(badorgood[0], {})
	data_parse[key][badorgood[0]]['drivetime_male'] = [float(i) for i in badorgood[1].split(',')]
	data_parse[key][badorgood[0]]['drivetime_female'] = [float(i) for i in badorgood[2].split(',')]
	data_parse[key][badorgood[0]]['trip_male'] = [float(i) for i in badorgood[3].split(',')]
	data_parse[key][badorgood[0]]['trip_female'] = [float(i) for i in badorgood[4].split(',')]
print("Finish loading!")