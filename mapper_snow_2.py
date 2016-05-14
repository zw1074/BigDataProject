#!/usr/bin/python
import sys
import StringIO
import csv
from datetime import datetime

for line in sys.stdin:
	csv_file = StringIO.StringIO(line)
	csv_reader = csv.reader(csv_file)
	for record in csv_reader:
		if len(record) > 2:
			if record[1] != 'starttime':
				try:
					weekday = datetime.strptime(record[1], '%m/%d/%Y %H:%M').weekday()
				except ValueError:
					weekday = datetime.strptime(record[1], '%m/%d/%Y %H:%M:%S').weekday()
				date, hr = record[1].split(' ')
				mo, day, yr = date.split('/',2)
				hr = hr.split(':',1)[0]
				date = str(yr) + str(mo).zfill(2) + str(day).zfill(2) + str(hr).zfill(2)
				drive_time = record[0]
				print "%s\t1,%s,1" % (date,drive_time)
		else:
			weekday = datetime.strptime(record[0], '%Y%m%d%H').weekday()
			hr = record[0][-2:]
			yr = record[0][:4]
			mo = record[0][4:6]
			day = record[0][6:8]
			date = str(yr) + str(mo).zfill(2) + str(day).zfill(2) + str(hr).zfill(2)
			print '%s\t0,%s' % (date,record[1])