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
			index = zerolistmaker(24)
			bad_drivetime_male = zerolistmaker(24)
			bad_drivetime_female = zerolistmaker(24)
			good_drivetime_male = zerolistmaker(24)
			good_drivetime_female = zerolistmaker(24)
			drivetime_male = zerolistmaker(24)
			drivetime_female = zerolistmaker(24)
			bad_trip_male = zerolistmaker(24)
			bad_trip_female = zerolistmaker(24)
			good_trip_male = zerolistmaker(24)
			good_trip_female = zerolistmaker(24)
			trip_male = zerolistmaker(24)
			trip_female = zerolistmaker(24)
			sumindexs = []
			drivetimes_male = []
			drivetimes_female = []
			trips_male = []
			trips_female = []
			n_good = 0
			n_bad = 0
			if value.split(',')[0] == '1': # citi-bike data
				if value.split(',')[-1] == '1': #male
					drivetime_male[hr] += float(value.split(',')[1])
					trip_male[hr] += 1
				elif value.split(',')[-1] == '2':
					drivetime_female[hr] += float(value.split(',')[1])
					trip_female[hr] += 1
			else:
				index[hr] = float(value.split(',')[1])
		else:
			if current_month == monthtime:
				if current_date == date:
					if value.split(',')[0] == '1':
						if value.split(',')[-1] == '1': #male
							drivetime_male[hr] += float(value.split(',')[1])
							trip_male[hr] += 1
						elif value.split(',')[-1] == '2':
							drivetime_female[hr] += float(value.split(',')[1])
							trip_female[hr] += 1
					else:
						index[hr] = float(value.split(',')[1])
				else:
					for i in xrange(24):
						if trip_male[i] != 0:
							drivetime_male[i] /= trip_male[i]
						if trip_female[i] != 0:
							drivetime_female[i] /= trip_female[i]
					drivetimes_male.append(drivetime_male)
					trips_male.append(trip_male)
					sumindexs.append(sum(index))
					drivetimes_female.append(drivetime_female)
					trips_female.append(trip_female)
					drivetime_male = zerolistmaker(24)
					trip_male = zerolistmaker(24)
					drivetime_female = zerolistmaker(24)
					trip_female = zerolistmaker(24)
					index = zerolistmaker(24)
					if value.split(',')[0] == '1': # citi-bike data
						if value.split(',')[-1] == '1': #male
							drivetime_male[hr] += float(value.split(',')[1])
							trip_male[hr] += 1
						elif value.split(',')[-1] == '2':
							drivetime_female[hr] += float(value.split(',')[1])
							trip_female[hr] += 1
					else:
						index[hr] = float(value.split(',')[1])
					current_date = date
			else:
				# find the top-50 percent
				for i in xrange(24):
					if trip_male[i] != 0:
						drivetime_male[i] /= trip_male[i]
					if trip_female[i] != 0:
						drivetime_female[i] /= trip_female[i]
				drivetimes_male.append(drivetime_male)
				trips_male.append(trip_male)
				sumindexs.append(sum(index))
				drivetimes_female.append(drivetime_female)
				trips_female.append(trip_female)
				sortindex = sorted(sumindexs, reverse = True)
				length = sumindexs.__len__()
				a = int(length*3/float(10))
				thresholda = sortindex[a]
				thresholdb = sortindex[length - a]
				for i in xrange(length):
					if sumindexs[i] >= thresholda: # bad weather
						n_bad += 1
						for j in xrange(24):
							bad_drivetime_male[j] += drivetimes_male[i][j]
							bad_trip_male[j] += trips_male[i][j]
							bad_drivetime_female[j] += drivetimes_female[i][j]
							bad_trip_female[j] += trips_female[i][j]
					elif sumindexs[i] <= thresholdb:
						n_good += 1
						for j in xrange(24):
							good_drivetime_male[j] += drivetimes_male[i][j]
							good_trip_male[j] += trips_male[i][j]
							good_drivetime_female[j] += drivetimes_female[i][j]
							good_trip_female[j] += trips_female[i][j]
				for i in xrange(24):
					bad_drivetime_male[i] /= float(n_bad)
					bad_trip_male[i] /= float(n_bad)
					good_drivetime_male[i] /=  float(n_good)
					good_trip_male[i] /= float(n_good)
					bad_drivetime_female[i] /= float(n_bad)
					bad_trip_female[i] /= float(n_bad)
					good_drivetime_female[i] /=  float(n_good)
					good_trip_female[i] /= float(n_good)
				# print good weather
				print "%s\t0;" % current_month,
				for i in xrange(23):
					print "%s," % str(good_drivetime_male[i]),
				print "%s;" % str(good_drivetime_male[-1]),
				for i in xrange(23):
					print "%s," % str(good_drivetime_female[i]),
				print "%s;" % str(good_drivetime_female[-1]),
				for i in xrange(23):
					print "%s," % str(good_trip_male[i]),
				print "%s;" % str(good_trip_male[-1]),
				for i in xrange(23):
					print "%s," % str(good_trip_female[i]),
				print "%s;" % str(good_trip_female[-1])
				# print bad weather
				print "%s\t1;" % current_month,
				for i in xrange(23):
					print "%s," % str(bad_drivetime_male[i]),
				print "%s;" % str(bad_drivetime_male[-1]),
				for i in xrange(23):
					print "%s," % str(bad_drivetime_female[i]),
				print "%s;" % str(bad_drivetime_female[-1]),
				for i in xrange(23):
					print "%s," % str(bad_trip_male[i]),
				print "%s;" % str(bad_trip_male[-1]),
				for i in xrange(23):
					print "%s," % str(bad_trip_female[i]),
				print "%s;" % str(bad_trip_female[-1])
				current_month = monthtime
				current_date = date
				current_hr = hr
				index = zerolistmaker(24)
				bad_drivetime_male = zerolistmaker(24)
				bad_drivetime_female = zerolistmaker(24)
				good_drivetime_male = zerolistmaker(24)
				good_drivetime_female = zerolistmaker(24)
				drivetime_male = zerolistmaker(24)
				drivetime_female = zerolistmaker(24)
				bad_trip_male = zerolistmaker(24)
				bad_trip_female = zerolistmaker(24)
				good_trip_male = zerolistmaker(24)
				good_trip_female = zerolistmaker(24)
				trip_male = zerolistmaker(24)
				trip_female = zerolistmaker(24)
				sumindexs = []
				drivetimes_male = []
				drivetimes_female = []
				trips_male = []
				trips_female = []
				n_good = 0
				n_bad = 0
				if value.split(',')[0] == '1': # citi-bike data
					if value.split(',')[-1] == '1': #male
						drivetime_male[hr] += float(value.split(',')[1])
						trip_male[hr] += 1
					elif value.split(',')[-1] == '2':
						drivetime_female[hr] += float(value.split(',')[1])
						trip_female[hr] += 1
				else:
					index[hr] = float(value.split(',')[1])
# find the top-50 percent
for i in xrange(24):
	if trip_male[i] != 0:
		drivetime_male[i] /= trip_male[i]
	if trip_female[i] != 0:
		drivetime_female[i] /= trip_female[i]
drivetimes_male.append(drivetime_male)
trips_male.append(trip_male)
sumindexs.append(sum(index))
drivetimes_female.append(drivetime_female)
trips_female.append(trip_female)
sortindex = sorted(sumindexs, reverse = True)
length = sumindexs.__len__()
a = int(length*3/float(10))
thresholda = sortindex[a]
thresholdb = sortindex[length - a]
for i in xrange(length):
	if sumindexs[i] >= thresholda: # bad weather
		n_bad += 1
		for j in xrange(24):
			bad_drivetime_male[j] += drivetimes_male[i][j]
			bad_trip_male[j] += trips_male[i][j]
			bad_drivetime_female[j] += drivetimes_female[i][j]
			bad_trip_female[j] += trips_female[i][j]
	elif sumindexs[i] <= thresholdb:
		n_good += 1
		for j in xrange(24):
			good_drivetime_male[j] += drivetimes_male[i][j]
			good_trip_male[j] += trips_male[i][j]
			good_drivetime_female[j] += drivetimes_female[i][j]
			good_trip_female[j] += trips_female[i][j]
for i in xrange(24):
	bad_drivetime_male[i] /= float(n_bad)
	bad_trip_male[i] /= float(n_bad)
	good_drivetime_male[i] /=  float(n_good)
	good_trip_male[i] /= float(n_good)
	bad_drivetime_female[i] /= float(n_bad)
	bad_trip_female[i] /= float(n_bad)
	good_drivetime_female[i] /=  float(n_good)
	good_trip_female[i] /= float(n_good)
# print good weather
print "%s\t0;" % current_month,
for i in xrange(23):
	print "%s," % str(good_drivetime_male[i]),
print "%s;" % str(good_drivetime_male[-1]),
for i in xrange(23):
	print "%s," % str(good_drivetime_female[i]),
print "%s;" % str(good_drivetime_female[-1]),
for i in xrange(23):
	print "%s," % str(good_trip_male[i]),
print "%s;" % str(good_trip_male[-1]),
for i in xrange(23):
	print "%s," % str(good_trip_female[i]),
print "%s;" % str(good_trip_female[-1])
# print bad weather
print "%s\t1;" % current_month,
for i in xrange(23):
	print "%s," % str(bad_drivetime_male[i]),
print "%s;" % str(bad_drivetime_male[-1]),
for i in xrange(23):
	print "%s," % str(bad_drivetime_female[i]),
print "%s;" % str(bad_drivetime_female[-1]),
for i in xrange(23):
	print "%s," % str(bad_trip_male[i]),
print "%s;" % str(bad_trip_male[-1]),
for i in xrange(23):
	print "%s," % str(bad_trip_female[i]),
print "%s;" % str(bad_trip_female[-1])