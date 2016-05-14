#!/usr/bin/env python
import re
import sys

for line in sys.stdin:
	splits = re.findall(r'[\d\.\*]+(?=\s|[A-Z])', line)
	if len(splits) <= 10:
		print 'None' + '\t' + 'None'
	else:
		key = splits[2][:-2]
		PCP = splits[-5:-1]
		SPD = splits[4]
		TEM = splits[-12]
		print key + '\t' + ','.join(PCP) + ',' + SPD + ',' + TEM