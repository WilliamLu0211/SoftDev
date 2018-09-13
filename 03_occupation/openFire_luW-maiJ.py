# openFire - William Lu, Jiajie Mai
# SoftDev1 pd7
# K06 -- StI/O: Divine your Destiny!
# 2018-09-14

import random, csv

source = open('occupations.csv', 'rU')
reader = csv.reader(source)
reader.next()

dict = {}
for line in reader:
	#print(line, '\n')
	dict[line[0]] = float(line[1])
dict.pop('Total')
#print(dict)

def getKey(dict):
	result = random.random() * 100
	sum = 0
	for key in dict:
		sum += dict[key]
		if sum >= result:
			return key

print(getKey(dict))