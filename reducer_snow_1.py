#!/usr/bin/env python
import sys

keys = None

for line in sys.stdin:
	line = line.strip()
	key, value = line.split('\t')
	if key != 'None':
		if keys == None:
			keys = key
			values = []
			if value != '**':
				values.append(float(value))
		else:
			if keys == key:
				if value != '**':
					values.append(float(value))
			else:
				if values.__len__() == 0:
					print '%s,%s' % (keys, str(0.0))
				else:
					print '%s,%s' % (keys, str(sum(values)/float(values.__len__())))
				keys = key
				values = []
				if value != '**':
					values.append(float(value))
if values.__len__() == 0:
	print '%s,%s' % (keys, str(0.0))
else:
	print '%s,%s' % (keys, str(sum(values)/float(values.__len__())))