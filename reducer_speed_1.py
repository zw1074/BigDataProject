#!/usr/bin/env python
import sys

keys = None

def get_average(PCP, PCP_n, i):
	if i == 2:
		if PCP_n[i] == 0:
			return 0
		else:
			a = PCP[i]/PCP_n[i]/(6.5*i**2 - 1.5*i + 1)
			# Normalize
			return a/1.78
	else:
		if PCP_n[i] == 0:
			return get_average(PCP, PCP_n, i+1)
		else:
			a = PCP[i]/PCP_n[i]/(6.5*i**2 - 1.5*i + 1)
			return a/1.78

for line in sys.stdin:
	line = line.strip()
	key, value = line.split('\t')
	value_split = value.split(',')
	if key != 'None':
		if keys == None:
			keys = key
			PCP = []
			PCP_n = []
			if value_split[0] != '*****':
				PCP.append(float(value_split[0]))
				PCP_n.append(1)
			else:
				PCP.append(0.0)
				PCP_n.append(0)
			if value_split[1] != '*****':
				PCP.append(float(value_split[1]))
				PCP_n.append(1)
			else:
				PCP.append(0.0)
				PCP_n.append(0)
			if value_split[2] != '*****':
				PCP.append(float(value_split[2]))
				PCP_n.append(1)
			else:
				PCP.append(0.0)
				PCP_n.append(0)
			# if value_split[3] != '*****':
			# 	PCP.append(float(value_split[3]))
			# 	PCP_n.append(1)
			# else:
			# 	PCP.append(0.0)
			# 	PCP_n.append(0)
			if value_split[4] != '***':
				SPD = float(value_split[4])
				SPD_n = 1
			else:
				SPD = 0
				SPD_n = 0
			if value_split[5] != '****':
				TEMP = float(value_split[5])
				TEMP_n = 1
			else:
				TEMP = 0
				TEMP_n = 0
		else:
			if key == keys:
				if value_split[0] != '*****':
					PCP[0] += float(value_split[0])
					PCP_n[0] += 1
				if value_split[1] != '*****':
					PCP[1] += float(value_split[1])
					PCP_n[1] += 1
				if value_split[2] != '*****':
					PCP[2] += float(value_split[2])
					PCP_n[2] += 1
				# if value_split[3] != '*****':
				# 	PCP[3] += float(value_split[3])
				# 	PCP_n[3] += 1
				if value_split[4] != '***':
					SPD += float(value_split[4])
					SPD_n += 1
				if value_split[5] != '****':
					TEMP += float(value_split[5])
					TEMP_n += 1
			else:
				# if PCP01_n == 0:
				# 	PCP01_a = 0
				# else:
				# 	PCP01_a = PCP01/PCP01_n
				# if PCP06_n == 0:
				# 	PCP06_a = 0
				# else:
				# 	PCP06_a = PCP06/PCP06_n/6
				# if PCP24_n == 0:
				# 	PCP24_a = 0
				# else:
				# 	PCP24_a = PCP24/PCP24_n/24
				# if PCPXX_n == 0:
				# 	PCPXX_a = 0
				# else:
				# 	PCPXX_a = PCPXX/PCPXX_n
				if SPD_n == 0:
					SPD_a = 0
				else:
					SPD_a = SPD/float(SPD_n)
				if TEMP_n == 0:
					TEMP_a = 100000000
				else:
					TEMP_a = TEMP/float(TEMP_n)
				print keys + ',' + str(get_average(PCP, PCP_n, 0) + SPD_a/float(37)) + ',' + str(TEMP_a)
				keys = key
				PCP = []
				PCP_n = []
				if value_split[0] != '*****':
					PCP.append(float(value_split[0]))
					PCP_n.append(1)
				else:
					PCP.append(0.0)
					PCP_n.append(0)
				if value_split[1] != '*****':
					PCP.append(float(value_split[1]))
					PCP_n.append(1)
				else:
					PCP.append(0.0)
					PCP_n.append(0)
				if value_split[2] != '*****':
					PCP.append(float(value_split[2]))
					PCP_n.append(1)
				else:
					PCP.append(0.0)
					PCP_n.append(0)
				# if value_split[3] != '*****':
				# 	PCP.append(float(value_split[3]))
				# 	PCP_n.append(1)
				# else:
				# 	PCP.append(0.0)
				# 	PCP_n.append(0)
				if value_split[4] != '***':
					SPD = float(value_split[4])
					SPD_n = 1
				else:
					SPD = 0
					SPD_n = 0
				if value_split[5] != '****':
					TEMP = float(value_split[5])
					TEMP_n = 1
				else:
					TEMP = 0
					TEMP_n = 0
# if PCP01_n == 0:
# 	PCP01_a = 0
# else:
# 	PCP01_a = PCP01/PCP01_n
# if PCP06_n == 0:
# 	PCP06_a = 0
# else:
# 	PCP06_a = PCP06/PCP06_n
# if PCP24_n == 0:
# 	PCP24_a = 0
# else:
# 	PCP24_a = PCP24/PCP24_n
# if PCPXX_n == 0:
# 	PCPXX_a = 0
# else:
# 	PCPXX_a = PCPXX/PCPXX_n
# print keys + '\t' + str(PCP01_a) + ',' + str(PCP06_a) + ',' + str(PCP24_a) + ',' + str(PCPXX_a)
if SPD_n == 0:
	SPD_a = 0
else:
	SPD_a = SPD/SPD_n
if TEMP_n == 0:
	TEMP_a = 100000000
else:
	TEMP_a = TEMP/float(TEMP_n)
print keys + ',' + str(get_average(PCP, PCP_n, 0) + SPD_a/float(37)) + ',' + str(TEMP_a)