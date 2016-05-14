#!/usr/bin/python
import sys

current_month = None
tempdict = {}
# tempdict = {}

# def zerolistmaker(n):
#     listofzeros = [0] * n
#     return listofzeros

# for line in sys.stdin:
	# line = line.strip()
	# key,value = line.split('\t')
	# date = key[:6] + key[8:10]
	# hr = int(key[-2:])
	# week = int(key[6:8])
	# monthtime = key[:6]
# 	if week >= 0 and week <= 3:
# 		if hr >= 14 and hr <= 15
# 		if current_month == None:
# 			current_month = monthtime
# 			current_date = date
# 			drivetime = zerolistmaker(24)
# 			trip = zerolistmaker(24)
# 			index = zerolistmaker(24)
# 			temp = zerolistmaker(24)
# 			temps = []
# 			drivetimes = []
# 			trips = []
# 			sumindexs = []
# 			n_good = 0
# 			n_bad = 0
			# if value.split(',')[0] == '1': # citi-bike data
				# drivetime[hr] += float(value.split(',')[1])
				# trip[hr] += 1
# 			else:
# 				index[hr] = float(value.split(',')[1])
# 				temp[hr] = float(value.split(',')[2])
# 				tempdict.setdefault(float(value.split(',')[2]), [[0.0,0.0,0.0],[0.0,0.0,0.0]])
# 		else:
# 			if current_month == monthtime:
# 				if current_date == date:
# 					if value.split(',')[0] == '1': # citi-bike data
# 						drivetime[hr] += float(value.split(',')[1])
# 						trip[hr] += 1
# 					else:
# 						index[hr] = float(value.split(',')[1])
# 						temp[hr] = float(value.split(',')[2])
# 						tempdict.setdefault(float(value.split(',')[2]), [[0.0,0.0,0.0],[0.0,0.0,0.0]])
# 				else:
# 					for i in xrange(24):
# 						drivetime[i] /= trip[i]
# 					drivetimes.append(drivetime)
# 					trips.append(trip)
# 					sumindexs.append(sum(index))
# 					temps.append(temp)
# 					drivetime = zerolistmaker(24)
# 					trip = zerolistmaker(24)
# 					index = zerolistmaker(24)
# 					temp = zerolistmaker(24)
# 					if value.split(',')[0] == '1': # citi-bike data
# 						drivetime[hr] += float(value.split(',')[1])
# 						trip[hr] += 1
# 					else:
# 						index[hr] = float(value.split(',')[1])
# 						temp[hr] = float(value.split(',')[2])
# 						tempdict.setdefault(float(value.split(',')[2]), [[0.0,0.0,0.0],[0.0,0.0,0.0]])
# 					current_date = date
# 			else:
# 				for i in xrange(24):
# 					drivetime[i] /= trip[i]
# 				drivetimes.append(drivetime)
# 				trips.append(trip)
# 				sumindexs.append(sum(index))
# 				temps.append(temp)
# 				drivetime = zerolistmaker(24)
# 				trip = zerolistmaker(24)
# 				index = zerolistmaker(24)
# 				temp = zerolistmaker(24)
# 				sortindex = sorted(sumindexs, reverse = True)
# 				length = sumindexs.__len__()
# 				a = int(length*3/float(10))
# 				thresholda = sortindex[a]
# 				thresholdb = sortindex[length - a]
# 				for i in xrange(length):
# 					if sumindexs[i] >= thresholda: # bad weather
# 						for j in xrange(24):
# 							tempdict[temps[i][j]][1][0] += 1
# 							tempdict[temps[i][j]][1][1] += drivetimes[i][j]
# 							tempdict[temps[i][j]][1][2] += trips[i][j]
# 					elif sumindexs[i] <= thresholdb:
# 						for j in xrange(24):
# 							tempdict[temps[i][j]][0][0] += 1
# 							tempdict[temps[i][j]][0][1] += drivetimes[i][j]
# 							tempdict[temps[i][j]][0][2] += trips[i][j]
# 				current_month = monthtime
# 				current_date = date
# 				drivetime = zerolistmaker(24)
# 				trip = zerolistmaker(24)
# 				index = zerolistmaker(24)
# 				temp = zerolistmaker(24)
# 				temps = []
# 				drivetimes = []
# 				trips = []
# 				sumindexs = []
# 				n_good = 0
# 				n_bad = 0
# 				if value.split(',')[0] == '1': # citi-bike data
# 					drivetime[hr] += float(value.split(',')[1])
# 					trip[hr] += 1
# 				else:
# 					index[hr] = float(value.split(',')[1])
# 					temp[hr] = float(value.split(',')[2])
# 					tempdict.setdefault(float(value.split(',')[2]), [[0.0,0.0,0.0],[0.0,0.0,0.0]])
# sortindex = sorted(sumindexs, reverse = True)
# length = sumindexs.__len__()
# a = int(length*3/float(10))
# thresholda = sortindex[a]
# thresholdb = sortindex[length - a]
# for i in xrange(length):
# 	if sumindexs[i] >= thresholda: # bad weather
# 		for j in xrange(24):
# 			tempdict[temps[i][j]][1][0] += 1
# 			tempdict[temps[i][j]][1][1] += drivetimes[i][j]
# 			tempdict[temps[i][j]][1][2] += trips[i][j]
# 	elif sumindexs[i] <= thresholdb:
# 		for j in xrange(24):
# 			tempdict[temps[i][j]][0][0] += 1
# 			tempdict[temps[i][j]][0][1] += drivetimes[i][j]
# 			tempdict[temps[i][j]][0][2] += trips[i][j]

# # print result
# for key in tempdict.keys():
# 	print "%s\t%s,%s,%s,%s,%s,%s" % (str(key), str(tempdict[key][0][0]), str(tempdict[key][0][1]), str(tempdict[key][0][2]), str(tempdict[key][1][0]), str(tempdict[key][1][1]), str(tempdict[key][1][2]))

for line in sys.stdin:
	line = line.strip()
	key,value = line.split('\t')
	date = key[:6] + key[8:10]
	hr = int(key[-2:])
	week = int(key[6:8])
	monthtime = key[:6]
	if current_month == None:
		current_month = monthtime
		current_date = date
		sumindexs = []
		sumtrips = []
		maxtemps = []
		sumtrip = 0
		sumindex = 0
		maxtemp = 0
		if value.split(',')[0] == '1': # citi-bike data
			sumtrip += 1
		else:
			sumindex += float(value.split(',')[1])
			maxtemp = float(value.split(',')[2])
	else:
		if current_month == monthtime:
			if current_date == date:
				if value.split(',')[0] == '1':
					sumtrip += 1
				else:
					sumindex += float(value.split(',')[1])
					if float(value.split(',')[2]) > maxtemp:
						maxtemp = float(value.split(',')[2])
			else:
				sumindexs.append(sumindex)
				sumtrips.append(sumtrip)
				maxtemps.append(maxtemp)
				sumtrip = 0
				sumindex = 0
				maxtemp = 0
				if value.split(',')[0] == '1': # citi-bike data
					sumtrip += 1
				else:
					sumindex += float(value.split(',')[1])
					maxtemp = float(value.split(',')[2])
				current_date = date
		else:
			sumindexs.append(sumindex)
			sumtrips.append(sumtrip)
			maxtemps.append(maxtemp)
			sortindex = sorted(sumindexs, reverse = True)
			length = sumindexs.__len__()
			a = int(length*3/float(10))
			thresholda = sortindex[a]
			thresholdb = sortindex[length - a]
			for i in xrange(length):
				if sumindexs[i] >= thresholda: # bad weather
					tempdict.setdefault(maxtemps[i], [[0.0,0.0],[0.0,0.0]])
					tempdict[maxtemps[i]][1][0] += 1
					tempdict[maxtemps[i]][1][1] += sumtrips[i]
				elif sumindexs[i] <= thresholdb:
					tempdict.setdefault(maxtemps[i], [[0.0,0.0],[0.0,0.0]])
					tempdict[maxtemps[i]][0][0] += 1
					tempdict[maxtemps[i]][0][1] += sumtrips[i]
			current_month = monthtime
			current_date = date
			sumindexs = []
			sumtrips = []
			maxtemps = []
			sumtrip = 0
			sumindex = 0
			maxtemp = 0
			if value.split(',')[0] == '1': # citi-bike data
				sumtrip += 1
			else:
				sumindex += float(value.split(',')[1])
				maxtemp = float(value.split(',')[2])
sumindexs.append(sumindex)
sumtrips.append(sumtrip)
maxtemps.append(maxtemp)
sortindex = sorted(sumindexs, reverse = True)
length = sumindexs.__len__()
a = int(length*3/float(10))
thresholda = sortindex[a]
thresholdb = sortindex[length - a]
for i in xrange(length):
	if sumindexs[i] >= thresholda: # bad weather
		tempdict.setdefault(maxtemps[i], [[0.0,0.0],[0.0,0.0]])
		tempdict[maxtemps[i]][1][0] += 1
		tempdict[maxtemps[i]][1][1] += sumtrips[i]
	elif sumindexs[i] <= thresholdb:
		tempdict.setdefault(maxtemps[i], [[0.0,0.0],[0.0,0.0]])
		tempdict[maxtemps[i]][0][0] += 1
		tempdict[maxtemps[i]][0][1] += sumtrips[i]
for key in tempdict.keys():
	print "%s\t%s,%s,%s,%s" % (str(key), str(tempdict[key][0][0]), str(tempdict[key][0][1]), str(tempdict[key][1][0]), str(tempdict[key][1][1]))