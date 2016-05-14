#!/usr/bin/python
import matplotlib.pyplot as plt
import seaborn as sns
def data_graph(data_parse, month):
	plt.figure(figsize=(20, 16)) 
	# ax = plt.subplot(211)
	# ax.plot(range(24), data_parse[month]['0']['drivetime_young'], color = 'b', ls = '--', label = 'Group1 Duration (Good Weather)')
	# ax.plot(range(24), data_parse[month]['1']['drivetime_young'], color = 'r', ls = '--', label = 'Group1 Duration (Bad Weather)')
	# ax.plot(range(24), data_parse[month]['0']['drivetime_med'], color = 'b', ls = '-.', label = 'Group2 Duration (Good Weather)')
	# ax.plot(range(24), data_parse[month]['1']['drivetime_med'], color = 'r', ls = '-.', label = 'Group2 Duration (Bad Weather)')
	# ax.plot(range(24), data_parse[month]['0']['drivetime_old'], color = 'b', label = 'Group3 Duration (Good Weather)')
	# ax.plot(range(24), data_parse[month]['1']['drivetime_old'], color = 'r', label = 'Group3 Duration (Bad Weather)')
	# ax.legend(loc=1)
	# ax.grid()
	# ax.set_xlabel("Time of Day", fontsize = 16)
	# ax.set_ylabel("Trip Duration", fontsize = 16)
	# ax.set_title('Citibike Trip Duration on Weekdays in ' + month, fontsize = 26)
	ax2 = plt.subplot(111)
	ax2.plot(range(24), data_parse[month]['0']['trip_young'], color = 'mediumpurple', ls = '--', label = 'Group1 Number of Trips (Good Weather)', linewidth = 4)
	ax2.plot(range(24), data_parse[month]['1']['trip_young'], color = 'r', ls = '--', label = 'Group1 Number of Trips (Bad Weather)', linewidth = 4)
	ax2.plot(range(24), data_parse[month]['0']['trip_med'], color = 'mediumpurple', ls = '-.', label = 'Group2 Number of Trips (Good Weather)', linewidth = 4)
	ax2.plot(range(24), data_parse[month]['1']['trip_med'], color = 'r', ls = '-.', label = 'Group2 Number of Trips (Bad Weather)', linewidth = 4)
	ax2.plot(range(24), data_parse[month]['0']['trip_old'], color = 'mediumpurple', label = 'Group3 Number of Trips (Good Weather)', linewidth = 4)
	ax2.plot(range(24), data_parse[month]['1']['trip_old'], color = 'r', label = 'Group3 Number of Trips (Bad Weather)', linewidth = 4)
	ax2.legend(loc=1)
	ax2.grid()
	ax2.set_xlabel("Time of Day", fontsize = 26)
	ax2.set_ylabel("Number of Trips", fontsize = 26)
	ax2.set_title('Number of Trips on Weekdays in ' + month, fontsize = 36)
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
	plt.savefig('try_age.png')

with open('result_age.txt') as fobj:
	data_init = fobj.readlines()
data_parse = {}
for line in data_init:
	line = line.strip()
	key, value = line.split('\t')
	data_parse.setdefault(key, {})
	badorgood = value.split(';')
	data_parse[key].setdefault(badorgood[0], {})
	data_parse[key][badorgood[0]]['drivetime_young'] = [float(i) for i in badorgood[1].split(',')]
	data_parse[key][badorgood[0]]['drivetime_med'] = [float(i) for i in badorgood[2].split(',')]
	data_parse[key][badorgood[0]]['drivetime_old'] = [float(i) for i in badorgood[3].split(',')]
	data_parse[key][badorgood[0]]['trip_young'] = [float(i) for i in badorgood[4].split(',')]
	data_parse[key][badorgood[0]]['trip_med'] = [float(i) for i in badorgood[5].split(',')]
	data_parse[key][badorgood[0]]['trip_old'] = [float(i) for i in badorgood[6].split(',')]
print("Finish loading!")