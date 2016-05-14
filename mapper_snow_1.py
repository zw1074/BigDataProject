#!/usr/bin/python
import sys
import re

for line in sys.stdin:
	splits = re.findall(r'[\d\.\*]+(?=\s|[A-Z])', line)
	if len(splits) <= 10:
		print 'None' + '\t' + 'None'
	else:
		key = splits[2][:-2]
		SD = splits[-1]
		print key + '\t' + SD
	