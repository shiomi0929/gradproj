# -*- coding: utf-8 -*-

#import numpy as np


import json
import scratch_block
import urllib2
import csv

f = open('cos.csv', 'ab')
csvWriter = csv.writer(f)

def printFirst(L):
    if isinstance(L, list)and len(L)>0 :
        first = L[0]
        if isinstance(first, unicode):
            for e in L:
                printFirst(e)
            if first in dict:
                dict[first] += 1
            else:
                dict[first] = 1
        for e in L:
            getFirst(e,dict)

def getFirst(L, dict):
    if isinstance(L, list)and len(L)>0 :
        first = L[0]
        if isinstance(first,unicode):
            if "turnRight:" in first:
                first = first.rstrip(":")
            if "turnLeft:" in first:
                first = first.rstrip(":")
            if "wait:elapsed:from:" in first:
                first = first.rstrip(":")
                        
            if first in dict:
                dict[first] += 1
                #else:
                #dict[first] = 1
        for e in L:
            getFirst(e,dict)

input1 = raw_input() 
#csvWriter.writerow(input1)
url1 = 'http://projects.scratch.mit.edu/internalapi/project/'+input1+'/get/'
r1 = urllib2.urlopen(url1)
root1 = json.loads(r1.read())
y1 = root1["children"]

x = scratch_block.block
for i in range(len(y1)):
    s1 = y1[0][u'scripts']
    getFirst(s1,x)

#print x


#x = {}


#print result.values()

nn = 0
xx = x.keys()
xx = sorted(xx)
xxx = []
for ww in xx:
    #print nn, ww, x[ww]
    xxx.append(x[ww])
    nn = nn+1
#print xxx
#print "*****"
#y = {}

input2 = raw_input() 
#csvWriter.writerow(input2)
url2 = 'http://projects.scratch.mit.edu/internalapi/project/'+input2+'/get/'
r2 = urllib2.urlopen(url2)
root2 = json.loads(r2.read())
y2 = root2["children"]

y = scratch_block.block

for i in range(len(y2)):
    s2 = y2[0][u'scripts']
    getFirst(s2,y)

#print y

#for www in y:
#    y[www]=0

#print result.values()
#result_s = sorted(result.items(), reverse = True, key = lambda x: x[1])
#print result_s
nn = 0
yy = y.keys()
yy = sorted(yy)
yyy = []
for ww in yy:
    #print nn, ww, y[ww]
    yyy.append(y[ww])
    #nn = nn+1
#print yyy

import math


class SimCalculator():
    def _absolute(self, vector):
        # ベクトルvの長さつまり絶対値を返す
        squared_distance = sum([vector[n] ** 2 for n in vector])
        distance = math.sqrt(squared_distance)
        return distance

    def sim_cos(self, v1, v2):
        numerator = 0
        # v1とv2で共通するkeyがあったとき、その値の積を加算していく。2つのベクトルの内積になる。
        i = 0
        for n in v1:
            numerator += v1[i]*v2[i]
            #if n in v2:
            # numerator += v1[n] * v2[n]
            #print i, numerator, v1[i], v2[i]
            i=i+1

        ss1 = []
        ss2 = []
        for x in v1:
            ss1.append(x*x)
        for x in v2:
            ss2.append(x*x)

        denominator = math.sqrt(sum(ss1))*math.sqrt(sum(ss2))

        if denominator == 0:
            return 0
        return numerator / denominator

list = []

if __name__ == '__main__':
    sc = SimCalculator()
    answer = str(sc.sim_cos(xxx,yyy))
    list = [input1, input2, answer]
    print answer
csvWriter.writerow(list)

