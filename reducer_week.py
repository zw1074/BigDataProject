#!/usr/bin/python
import sys

current_key = None

for line in sys.stdin:
	line = line.strip()
	key, value = line.split('\t')
	week = key[6:8]
	day = key[8:10]
	keyweek = key[:8]
	if current_key == None:
		current_key = key
		current_week = week
		current_day = day
		current_date = key[:6] + day
		days = []
		latlon = []
		latlon_day = []
		max_indexs = []
		maxindex = 0
		if value.split(',')[0] == '1': # citi-bike date
			latlon_day.append([value.split(',')[1], value.split(',')[2]])
		else:
			ind = float(value.split(',')[1])
			if ind > maxindex:
				maxindex = ind
	else:
		if current_key == key:
			if value.split(',')[0] == '1': # citi-bike date
				latlon_day.append([value.split(',')[1], value.split(',')[2]])
			else:
				ind = float(value.split(',')[1])
				if ind > maxindex:
					maxindex = ind
		else:
			if current_week == week:
				if current_day == day:
					if value.split(',')[0] == '1': # citi-bike date
						latlon_day.append([value.split(',')[1], value.split(',')[2]])
					else:
						ind = float(value.split(',')[1])
						if ind > maxindex:
							maxindex = ind
					current_key = key
				else:
					latlon.append(latlon_day)
					max_indexs.append(maxindex)
					days.append(current_date)
					latlon_day = []
					maxindex = 0
					if value.split(',')[0] == '1':
						latlon_day.append([value.split(',')[1], value.split(',')[2]])
					else:
						ind = float(value.split(',')[1])
						if ind > maxindex:
							maxindex = ind
					current_date = key[:6] + day
					current_key = key
					current_day = day
			else:
				latlon.append(latlon_day)
				max_indexs.append(maxindex)
				days.append(current_date)
				if max(max_indexs) >= 0.5:
					indx = [k for k,v in enumerate(max_indexs) if v >= 0.42]
					indx_not = [k for k,v in enumerate(max_indexs) if v < 0.243 and v > 0.16]
					for i in indx:
						print "%s,%s,%.4f\t1 " % (days[i], current_week, max_indexs[i]),
						for j in latlon[i][:-1]:
							print "%s,%s " % (j[0], j[1]),
						print "%s,%s" % (latlon[i][-1][0], latlon[i][-1][1]) 
					for i in indx_not:
						print "%s,%s,%.4f\t0 " % (days[i], current_week, max_indexs[i]),
						for j in latlon[i][:-1]:
							print "%s,%s " % (j[0], j[1]),
						print "%s,%s" % (latlon[i][-1][0], latlon[i][-1][1]) 
				current_key = key
				current_week = week
				current_day = day
				current_date = key[:6] + day
				latlon = []
				days = []
				latlon_day = []
				max_indexs = []
				maxindex = 0
				if value.split(',')[0] == '1': # citi-bike date
					latlon_day.append([value.split(',')[1], value.split(',')[2]])
				else:
					ind = float(value.split(',')[1])
					if ind > maxindex:
						maxindex = ind
latlon.append(latlon_day)
max_indexs.append(maxindex)
days.append(current_date)
if max(max_indexs) >= 0.5:
	indx = [k for k,v in enumerate(max_indexs) if v >= 0.42]
	indx_not = [k for k,v in enumerate(max_indexs) if v < 0.243 and v > 0.16]
	if len(indx) == 0:
		print "None\t1"
	else:
		for i in indx:
			print "%s,%s,%.4f\t1 " % (days[i], current_week, max_indexs[i]),
			for j in latlon[i][:-1]:
				print "%s,%s " % (j[0], j[1]),
			print "%s,%s" % (latlon[i][-1][0], latlon[i][-1][1]) 
	if len(indx_not) == 0:
		print "None\t0"
	else:
		for i in indx_not:
			print "%s,%s,%.4f\t0 " % (days[i], current_week, max_indexs[i]),
			for j in latlon[i][:-1]:
				print "%s,%s " % (j[0], j[1]),
			print "%s,%s" % (latlon[i][-1][0], latlon[i][-1][1])