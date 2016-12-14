# -*- coding: utf-8 -*-

#import numpy as np


import json
import scratch_block
import urllib2
import csv

f = open('data.csv', 'ab')
csvWriter = csv.writer(f)

input1 = raw_input() 
url1 = 'http://projects.scratch.mit.edu/internalapi/project/'+input1+'/get/'
r1 = urllib2.urlopen(url1)
root1 = json.loads(r1.read())
y1 = root1["children"]

count = 0
for i in range(len(y1)):
    if 'objName' in y1[i]:
        count += 1
print count

"""
#count = len(a1)
listData = []
listData.append(count)
csvWriter.writerow(listData)

f.close()
"""

"""
x1 = a1[0][u'objName']
x2 = a1[1][u'objName']
x3 = a1[2][u'objName']
x4 = a1[3][u'objName']
x5 = a1[4][u'objName']
x6 = a1[5][u'objName']
x7 = a1[6][u'objName']
"""

"""
print x2
print x3
print x4
print x5
print x6
print x7
"""
