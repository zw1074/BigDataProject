#!/usr/bin/python
import sys

current_month = None

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
		if current_month == None:
			current_month = monthtime
			current_date = date
			current_hr = hr
			bad_index = zerolistmaker(24)
			good_index = zerolistmaker(24)
			index = zerolistmaker(24)
			bad_drivetime = zerolistmaker(24)
			good_drivetime = zerolistmaker(24)
			drivetime = zerolistmaker(24)
			bad_trip = zerolistmaker(24)
			good_trip = zerolistmaker(24)
			trip = zerolistmaker(24)
			sumindexs = []
			drivetimes = []
			indexs = []
			trips = []
			n_good = 0
			n_bad = 0
			if value.split(',')[0] == '1': # citi-bike data
				drivetime[hr] += float(value.split(',')[1])
				trip[hr] += 1
			else:
				index[hr] = float(value.split(',')[1])
		else:
			if current_month == monthtime:
				if current_date == date:
					if value.split(',')[0] == '1': # citi-bike data
						drivetime[hr] += float(value.split(',')[1])
						trip[hr] += 1
					else:
						index[hr] = float(value.split(',')[1])
				else:
					for i in xrange(24):
						drivetime[i] /= trip[i]
					drivetimes.append(drivetime)
					trips.append(trip)
					sumindexs.append(sum(index))
					indexs.append(index)
					drivetime = zerolistmaker(24)
					trip = zerolistmaker(24)
					index = zerolistmaker(24)
					if value.split(',')[0] == '1': # citi-bike data
						drivetime[hr] += float(value.split(',')[1])
						trip[hr] += 1
					else:
						index[hr] = float(value.split(',')[1])
					current_date = date
			else:
				for i in xrange(24):
					drivetime[i] /= trip[i]
				drivetimes.append(drivetime)
				trips.append(trip)
				sumindexs.append(sum(index))
				indexs.append(index)
				# find the top-50 percent
				sortindex = sorted(sumindexs, reverse = True)
				length = indexs.__len__()
				a = int(length*3/float(10))
				thresholda = sortindex[a]
				thresholdb = sortindex[length - a]
				for i in xrange(length):
					if sumindexs[i] >= thresholda: # bad weather
						n_bad += 1
						for j in xrange(24):
							bad_drivetime[j] += drivetimes[i][j]
							bad_trip[j] += trips[i][j]
							bad_index[j] += indexs[i][j]
					elif sumindexs[i] <= thresholdb:
						n_good += 1
						for j in xrange(24):
							good_drivetime[j] += drivetimes[i][j]
							good_trip[j] += trips[i][j]
							good_index[j] += indexs[i][j]
				for i in xrange(24):
					bad_drivetime[i] /= float(n_bad)
					bad_trip[i] /= float(n_bad)
					bad_index[i] /= float(n_bad)
					good_drivetime[i] /=  float(n_good)
					good_trip[i] /= float(n_good)
					good_index[i] /= float(n_good)
				# print good weather
				print "%s\t0;" % current_month,
				for i in xrange(23):
					print "%s," % str(good_index[i]),
				print "%s;" % str(good_index[-1]),
				for i in xrange(23):
					print "%s," % str(good_drivetime[i]),
				print "%s;" % str(good_drivetime[-1]),
				for i in xrange(23):
					print "%s," % str(good_trip[i]),
				print "%s;" % str(good_trip[-1])
				# print bad weather
				print "%s\t1;" % current_month,
				for i in xrange(23):
					print "%s," % str(bad_index[i]),
				print "%s;" % str(bad_index[-1]),
				for i in xrange(23):
					print "%s," % str(bad_drivetime[i]),
				print "%s;" % str(bad_drivetime[-1]),
				for i in xrange(23):
					print "%s," % str(bad_trip[i]),
				print "%s;" % str(bad_trip[-1])
				current_month = monthtime
				current_date = date
				current_hr = hr
				bad_index = zerolistmaker(24)
				good_index = zerolistmaker(24)
				index = zerolistmaker(24)
				bad_drivetime = zerolistmaker(24)
				good_drivetime = zerolistmaker(24)
				drivetime = zerolistmaker(24)
				bad_trip = zerolistmaker(24)
				good_trip = zerolistmaker(24)
				trip = zerolistmaker(24)
				sumindexs = []
				drivetimes = []
				indexs = []
				trips = []
				n_good = 0
				n_bad = 0
				if value.split(',')[0] == '1': # citi-bike data
					drivetime[hr] += float(value.split(',')[1])
					trip[hr] += 1
				else:
					index[hr] = float(value.split(',')[1])
# find the top-50 percent
for i in xrange(24):
	drivetime[i] /= trip[i]
drivetimes.append(drivetime)
trips.append(trip)
sumindexs.append(sum(index))
indexs.append(index)
sortindex = sorted(sumindexs, reverse = True)
length = indexs.__len__()
a = int(length*3/float(10))
thresholda = sortindex[a]
thresholdb = sortindex[length - a]
for i in xrange(length):
	if sumindexs[i] >= thresholda: # bad weather
		n_bad += 1
		for j in xrange(24):
			bad_drivetime[j] += drivetimes[i][j]
			bad_trip[j] += trips[i][j]
			bad_index[j] += indexs[i][j]
	elif sumindexs[i] <= thresholdb:
		n_good += 1
		for j in xrange(24):
			good_drivetime[j] += drivetimes[i][j]
			good_trip[j] += trips[i][j]
			good_index[j] += indexs[i][j]
for i in xrange(24):
	bad_drivetime[i] /= float(n_bad)
	bad_trip[i] /= float(n_bad)
	bad_index[i] /= float(n_bad)
	good_drivetime[i] /=  float(n_good)
	good_trip[i] /= float(n_good)
	good_index[i] /= float(n_good)
# print good weather
print "%s\t0;" % current_month,
for i in xrange(23):
	print "%s," % str(good_index[i]),
print "%s;" % str(good_index[-1]),
for i in xrange(23):
	print "%s," % str(good_drivetime[i]),
print "%s;" % str(good_drivetime[-1]),
for i in xrange(23):
	print "%s," % str(good_trip[i]),
print "%s;" % str(good_trip[-1])
# print bad weather
print "%s\t1;" % current_month,
for i in xrange(23):
	print "%s," % str(bad_index[i]),
print "%s;" % str(bad_index[-1]),
for i in xrange(23):
	print "%s," % str(bad_drivetime[i]),
print "%s;" % str(bad_drivetime[-1]),
for i in xrange(23):
	print "%s," % str(bad_trip[i]),
print "%s;" % str(bad_trip[-1])