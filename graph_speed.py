#!/usr/bin/python
import matplotlib.pyplot as plt
def data_graph(data_parse, month):
	plt.figure(figsize=(20, 16)) 
	ax = plt.subplot(211)
	ax.plot(range(24), data_parse[month]['0']['index'], color = 'b', ls = '--', label = 'Good Weather Index', linewidth = 2)
	ax.plot(range(24), data_parse[month]['1']['index'], color = 'r', ls = '--', label = 'Bad Weather Index', linewidth = 2)
	ax2 = ax.twinx()
	ax2.plot(range(24), data_parse[month]['0']['drivetime'], color = 'b', label = 'Trip Duration (Good Weather)', linewidth = 2)
	ax2.plot(range(24), data_parse[month]['1']['drivetime'], color = 'r', label = 'Trip Duration (Bad Weather)', linewidth = 2)
	ax.legend(loc=1)
	ax2.legend(loc=2)
	ax.grid()
	ax.set_xlabel("Time of Day", fontsize = 16)
	ax.set_ylabel("Index", fontsize = 16)
	ax2.set_ylabel("Trip Duration", fontsize = 16)
	ax.set_title('Index and Citibike Trip Duration on Weekdays in ' + month, fontsize = 26)
	ax3 = plt.subplot(212)
	ax3.plot(range(24), data_parse[month]['0']['index'], color = 'b', ls = '--', label = 'Good Weather Index', linewidth = 2)
	ax3.plot(range(24), data_parse[month]['1']['index'], color = 'r', ls = '--', label = 'Bad Weather Index', linewidth = 2)
	ax4 = ax3.twinx()
	ax4.plot(range(24), data_parse[month]['0']['trip'], color = 'b', label = 'Number of Trips (Good Weather)', linewidth = 2)
	ax4.plot(range(24), data_parse[month]['1']['trip'], color = 'r', label = 'Number of Trips (Bad Weather)', linewidth = 2)
	ax3.legend(loc=1)
	ax4.legend(loc=2)
	ax3.grid()
	ax3.set_xlabel("Time of Day", fontsize = 16)
	ax3.set_ylabel("Index", fontsize = 16)
	ax4.set_ylabel("Number of Trips", fontsize = 16)
	ax3.set_title('Index and Citibike Number of Trips on Weekdays in ' + month, fontsize = 26)
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
	plt.savefig('try.png')

# with open('result_speed_2.txt') as fobj:
# 	data_init = fobj.readlines()
# good = []
# bad = []
# data_parse = {}
# for line in data_init:
# 	line = line.strip()
# 	key, value = line.split('\t')
# 	if float(value.split(',')[0]) != 0:
# 		good.append((float(key), float(float(value.split(',')[1])/float(value.split(',')[0])), float(float(value.split(',')[2])/float(value.split(',')[0]))))
# 	if float(value.split(',')[3]) != 0:
# 		bad.append((float(key), float(float(value.split(',')[4])/float(value.split(',')[3])), float(float(value.split(',')[5])/float(value.split(',')[3]))))
# # sort
# good = sorted(good, key=lambda x:x[0])
# bad = sorted(bad, key=lambda x:x[0])
# good_temp = [i[0] for i in good]
# good_drivetime = [i[1] for i in good]
# good_trip = [i[2] for i in good]
# bad_temp = [i[0] for i in bad]
# bad_drivetime = [i[1] for i in bad]
# bad_trip = [i[2] for i in bad]

# plt.figure(figsize=(20, 16)) 
# ax = plt.subplot(211)
# ax.plot(good_temp, good_drivetime, color = 'b', label = 'Duration (Good Weather)', linewidth = 2)
# ax.plot(bad_temp, bad_drivetime, color = 'r', label = 'Duration (Bad Weather)', linewidth = 2)
# ax.legend(loc=1)
# ax.grid()
# ax.set_xlabel("Temperature", fontsize = 24)
# ax.set_ylabel("Trip Duration", fontsize = 24)
# ax.set_title('Citibike Trip Duration vs. Temperature on Weekdays', fontsize = 36)
# ax2 = plt.subplot(212)
# ax2.plot(good_temp, good_trip, color = 'b', label = 'Number of Trips (Good Weather)', linewidth = 2)
# ax2.plot(bad_temp, bad_trip, color = 'r', label = 'Number of Trips (Bad Weather)', linewidth = 2)
# ax2.legend(loc=1)
# ax2.grid()
# ax2.set_xlabel("Temperature", fontsize = 24)
# ax2.set_ylabel("Number of Trips", fontsize = 24)
# ax2.set_title('Citibike Number of Trips vs. Temperature on Weekdays', fontsize = 36)
# plt.savefig('try_speed.png')

with open('result_speed_2_all.txt') as fobj:
	data_init = fobj.readlines()
good = []
bad = []
data_parse = {}
for line in data_init:
	line = line.strip()
	key, value = line.split('\t')
	if float(value.split(',')[0]) != 0:
		good.append((float(key), float(float(value.split(',')[1])/float(value.split(',')[0]))))
	if float(value.split(',')[2]) != 0:
		bad.append((float(key), float(float(value.split(',')[3])/float(value.split(',')[2]))))
# sort
good = sorted(good, key=lambda x:x[0])
bad = sorted(bad, key=lambda x:x[0])
good_temp = [i[0] for i in good]
good_trip = [i[1] for i in good]
bad_temp = [i[0] for i in bad]
bad_trip = [i[1] for i in bad]

plt.figure(figsize=(20, 16)) 
# ax = plt.subplot(211)
# ax.plot(good_temp, good_drivetime, color = 'b', label = 'Duration (Good Weather)', linewidth = 2)
# ax.plot(bad_temp, bad_drivetime, color = 'r', label = 'Duration (Bad Weather)', linewidth = 2)
# ax.legend(loc=1)
# ax.grid()
# ax.set_xlabel("Temperature", fontsize = 16)
# ax.set_ylabel("Trip Duration", fontsize = 16)
# ax.set_title('Citibike Trip Duration vs. Temperature on Weekdays', fontsize = 26)
ax2 = plt.subplot(111)
ax2.plot(good_temp, good_trip, color = 'b', label = 'Number of Trips (Good Weather)', linewidth = 2)
ax2.plot(bad_temp, bad_trip, color = 'r', label = 'Number of Trips (Bad Weather)', linewidth = 2)
ax2.legend(loc=0)
ax2.grid()
ax2.set_xlabel("Temperature", fontsize = 24)
ax2.set_ylabel("Number of Trips", fontsize = 24)
ax2.set_title('Number of Trips vs. Temperature', fontsize = 36)
plt.savefig('try_speed_all.png')

print("Finish loading!")