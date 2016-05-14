#!/usr/bin/python
import sys

current_month = None

for line in sys.stdin:
	line = line.strip()
	key, value = line.split('\t')
	month = key[:6]
	date = key[6:8]
	if current_month == None:
		current_month = month
		current_date = date
		trips = []
		maxtemp = []
		trip = 0
		temp = 0
		if value.split(',')[0] == '1':
			trip += 1
		else:
			if float(value.split(',')[1]) > temp:
				temp = float(value.split(',')[1])
	else:
		if current_month == month:
			if current_date == date:
				if value.split(',')[0] == '1':
					trip += 1
				else:
					if float(value.split(',')[1]) > temp:
						temp = float(value.split(',')[1])
			else:
				trips.append(trip)
				maxtemp.append(temp)
				trip = 0
				temp = 0
				if value.split(',')[0] == '1':
					trip += 1
				else:
					if float(value.split(',')[1]) > temp:
						temp = float(value.split(',')[1])
				current_date = date
		else:
			trips.append(trip)
			maxtemp.append(temp)
			print "%s\t%s,%s" % (current_month, str(sum(trips)/float(trips.__len__())), str(sum(maxtemp)/float(maxtemp.__len__())))
			current_month = month
			current_date = date
			trips = []
			maxtemp = []
			trip = 0
			temp = 0
			if value.split(',')[0] == '1':
				trip += 1
			else:
				if float(value.split(',')[1]) > temp:
					temp = float(value.split(',')[1])
trips.append(trip)
maxtemp.append(temp)
print "%s\t%s,%s" % (current_month, str(sum(trips)/float(trips.__len__())), str(sum(maxtemp)/float(maxtemp.__len__())))