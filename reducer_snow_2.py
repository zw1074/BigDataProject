#!/usr/bin/python
import sys
current_hr = None
snowdict = {}

for line in sys.stdin:
	line = line.strip()
	key, value = line.split('\t')
	month = key[:6]
	if int(month) >= 201501 and int(month) <= 201503:
		if current_hr == None:
			current_hr = key
			drivetime = 0
			trip = 0
			snow = '**'
			if value.split(',')[0] == '1':
				drivetime+=float(value.split(',')[1])
				trip += 1
			else:
				snow = value.split(',')[1]
		else:
			if current_hr == key:
				if value.split(',')[0] == '1':
					drivetime+=float(value.split(',')[1])
					trip += 1
				else:
					snow = value.split(',')[1]
			else:
				if snow != '**':
					if float(snow) > 0:
						snowdict.setdefault(float(snow), [[],[]])
						snowdict[float(snow)][0].append(drivetime/float(trip))
						snowdict[float(snow)][1].append(trip)
				current_hr = key
				drivetime = 0
				trip = 0
				snow = '**'
				if value.split(',')[0] == '1':
					drivetime+=float(value.split(',')[1])
					trip += 1
				else:
					snow = value.split(',')[1]
if float(snow) > 0:
	snowdict.setdefault(float(snow), [[],[]])
	snowdict[float(snow)][0].append(drivetime/float(trip))
	snowdict[float(snow)][1].append(trip)

# sort
for key in snowdict.keys():
	if snowdict[key][0].__len__() == 0:
		drivetime = 0
	else:
		drivetime = sum(snowdict[key][0])/float(snowdict[key][0].__len__())
	if snowdict[key][1].__len__() == 0:
		trip = 0
	else:
		trip = sum(snowdict[key][1])/float(snowdict[key][1].__len__())
	print "%s\t%s,%s" % (str(key), str(drivetime), str(trip))