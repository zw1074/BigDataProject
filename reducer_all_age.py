#!/usr/bin/python
import sys

current_date = None

def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros

for line in sys.stdin:
	line = line.strip()
	key,value = line.split('\t')
	date = key[:6] + key[8:10]
	hr = int(key[-2:])
	week = int(key[6:8])
	monthtime = key[:6]
	if week >= 0 and week <= 3:
		if current_date == None:
			current_date = date
			current_hr = hr
			index = zerolistmaker(24)
			bad_drivetime_young = zerolistmaker(24)
			bad_drivetime_med = zerolistmaker(24)
			bad_drivetime_old = zerolistmaker(24)
			good_drivetime_young = zerolistmaker(24)
			good_drivetime_med = zerolistmaker(24)
			good_drivetime_old = zerolistmaker(24)
			drivetime_young = zerolistmaker(24)
			drivetime_med = zerolistmaker(24)
			drivetime_old = zerolistmaker(24)
			bad_trip_young = zerolistmaker(24)
			bad_trip_med = zerolistmaker(24)
			bad_trip_old = zerolistmaker(24)
			good_trip_young = zerolistmaker(24)
			good_trip_med = zerolistmaker(24)
			good_trip_old = zerolistmaker(24)
			trip_young = zerolistmaker(24)
			trip_med = zerolistmaker(24)
			trip_old = zerolistmaker(24)
			sumindexs = []
			drivetimes_young = []
			drivetimes_med = []
			drivetimes_old = []
			trips_young = []
			trips_med = []
			trips_old = []
			n_good = 0
			n_bad = 0
			if value.split(',')[0] == '1': # citi-bike data
				if int(value.split(',')[-1]) < 25: #male
					drivetime_young[hr] += float(value.split(',')[1])
					trip_young[hr] += 1
				elif int(value.split(',')[-1]) >= 25 and int(value.split(',')[-1]) < 50:
					drivetime_med[hr] += float(value.split(',')[1])
					trip_med[hr] += 1
				else:
					drivetime_old[hr] += float(value.split(',')[1])
					trip_old[hr] += 1
			else:
				index[hr] = float(value.split(',')[1])
		else:
			if current_date == date:
				if value.split(',')[0] == '1':
					if int(value.split(',')[-1]) < 25: #male
						drivetime_young[hr] += float(value.split(',')[1])
						trip_young[hr] += 1
					elif int(value.split(',')[-1]) >= 25 and int(value.split(',')[-1]) < 50:
						drivetime_med[hr] += float(value.split(',')[1])
						trip_med[hr] += 1
					else:
						drivetime_old[hr] += float(value.split(',')[1])
						trip_old[hr] += 1
				else:
					index[hr] = float(value.split(',')[1])
			else:
				for i in xrange(24):
					if trip_young[i] != 0:
						drivetime_young[i] /= trip_young[i]
					if trip_med[i] != 0:
						drivetime_med[i] /= trip_med[i]
					if trip_old[i] != 0:
						drivetime_old[i] /= trip_old[i]
				drivetimes_young.append(drivetime_young)
				drivetimes_med.append(drivetime_med)
				drivetimes_old.append(drivetime_old)
				trips_young.append(trip_young)
				trips_med.append(trip_med)
				trips_old.append(trip_old)
				sumindexs.append(sum(index))
				drivetime_young = zerolistmaker(24)
				trip_young = zerolistmaker(24)
				drivetime_med = zerolistmaker(24)
				trip_med = zerolistmaker(24)
				drivetime_old = zerolistmaker(24)
				trip_old = zerolistmaker(24)
				index = zerolistmaker(24)
				if value.split(',')[0] == '1': # citi-bike data
					if int(value.split(',')[-1]) < 25: #male
						drivetime_young[hr] += float(value.split(',')[1])
						trip_young[hr] += 1
					elif int(value.split(',')[-1]) >= 25 and int(value.split(',')[-1]) < 50:
						drivetime_med[hr] += float(value.split(',')[1])
						trip_med[hr] += 1
					else:
						drivetime_old[hr] += float(value.split(',')[1])
						trip_old[hr] += 1
				else:
					index[hr] = float(value.split(',')[1])
				current_date = date
# find the top-50 percent
for i in xrange(24):
	if trip_young[i] != 0:
		drivetime_young[i] /= trip_young[i]
	if trip_med[i] != 0:
		drivetime_med[i] /= trip_med[i]
	if trip_old[i] != 0:
		drivetime_old[i] /= trip_old[i]
drivetimes_young.append(drivetime_young)
drivetimes_med.append(drivetime_med)
drivetimes_old.append(drivetime_old)
trips_young.append(trip_young)
trips_med.append(trip_med)
trips_old.append(trip_old)
sumindexs.append(sum(index))
sortindex = sorted(sumindexs, reverse = True)
length = sumindexs.__len__()
a = int(length*3/float(10))
thresholda = sortindex[a]
thresholdb = sortindex[length - a]
for i in xrange(length):
	if sumindexs[i] >= thresholda: # bad weather
		n_bad += 1
		for j in xrange(24):
			bad_drivetime_young[j] += drivetimes_young[i][j]
			bad_trip_young[j] += trips_young[i][j]
			bad_drivetime_med[j] += drivetimes_med[i][j]
			bad_trip_med[j] += trips_med[i][j]
			bad_drivetime_old[j] += drivetimes_old[i][j]
			bad_trip_old[j] += trips_old[i][j]
	elif sumindexs[i] <= thresholdb:
		n_good += 1
		for j in xrange(24):
			good_drivetime_young[j] += drivetimes_young[i][j]
			good_trip_young[j] += trips_young[i][j]
			good_drivetime_med[j] += drivetimes_med[i][j]
			good_trip_med[j] += trips_med[i][j]
			good_drivetime_old[j] += drivetimes_old[i][j]
			good_trip_old[j] += trips_old[i][j]
for i in xrange(24):
	bad_drivetime_young[i] /= float(n_bad)
	bad_trip_young[i] /= float(n_bad)
	good_drivetime_young[i] /=  float(n_good)
	good_trip_young[i] /= float(n_good)
	bad_drivetime_med[i] /= float(n_bad)
	bad_trip_med[i] /= float(n_bad)
	good_drivetime_med[i] /=  float(n_good)
	good_trip_med[i] /= float(n_good)
	bad_drivetime_old[i] /= float(n_bad)
	bad_trip_old[i] /= float(n_bad)
	good_drivetime_old[i] /=  float(n_good)
	good_trip_old[i] /= float(n_good)
# print good weather
print "0;",
for i in xrange(23):
	print "%s," % str(good_drivetime_young[i]),
print "%s;" % str(good_drivetime_young[-1]),
for i in xrange(23):
	print "%s," % str(good_drivetime_med[i]),
print "%s;" % str(good_drivetime_med[-1]),
for i in xrange(23):
	print "%s," % str(good_drivetime_old[i]),
print "%s;" % str(good_drivetime_old[-1]),
for i in xrange(23):
	print "%s," % str(good_trip_young[i]),
print "%s;" % str(good_trip_young[-1]),
for i in xrange(23):
	print "%s," % str(good_trip_med[i]),
print "%s;" % str(good_trip_med[-1]),
for i in xrange(23):
	print "%s," % str(good_trip_old[i]),
print "%s;" % str(good_trip_old[-1])
# print bad weather
print "1;",
for i in xrange(23):
	print "%s," % str(bad_drivetime_young[i]),
print "%s;" % str(bad_drivetime_young[-1]),
for i in xrange(23):
	print "%s," % str(bad_drivetime_med[i]),
print "%s;" % str(bad_drivetime_med[-1]),
for i in xrange(23):
	print "%s," % str(bad_drivetime_old[i]),
print "%s;" % str(bad_drivetime_old[-1]),
for i in xrange(23):
	print "%s," % str(bad_trip_young[i]),
print "%s;" % str(bad_trip_young[-1]),
for i in xrange(23):
	print "%s," % str(bad_trip_med[i]),
print "%s;" % str(bad_trip_med[-1]),
for i in xrange(23):
	print "%s," % str(bad_trip_old[i]),
print "%s;" % str(bad_trip_old[-1])