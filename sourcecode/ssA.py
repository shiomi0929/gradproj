# -*- coding: utf-8 -*-

#import numpy as np


import json
import scratch_block
import urllib2

import csv   #csvモジュールをインポートする

dataReader = csv.reader(open("id.csv","rU"))

f = open("result.csv", "w")
writecsv = csv.writer(f)
header = ['block', 'splite', 'cos']
body = []

url1 = 'http://projects.scratch.mit.edu/internalapi/project/'+'116739847'+'/get/'
r1 = urllib2.urlopen(url1)
root1 = json.loads(r1.read())
y1 = root1["children"]

#a = "scripts"

a = 'scripts'
s1 = []


#全体のブロック数の合計
for i in range(len(y1)):
    if not a in y1[i].keys():
        continue
    s1 = s1 + y1[i][u'scripts']

#スプライトの数
count1 = 0
for i in range(len(y1)):
    if 'objName' in y1[i]:
        count1 += 1


for row in dataReader:

    row = "".join(row)
    print row

    url2 = 'http://projects.scratch.mit.edu/internalapi/project/'+row+'/get/'
    r2 = urllib2.urlopen(url2)
    root2 = json.loads(r2.read())
    y2 = root2["children"]
    
    s2 = []

    #全体のブロック数の合計
    for i in range(len(y2)):
        if not a in y2[i].keys():
            continue
            s2 = s2 + y2[i][u'scripts']
            
    #スプライトの数
    count2 = 0
    for i in range(len(y2)):
        if 'objName' in y2[i]:
            count2 += 1
                    


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
        global count
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
                    count += 1
                    #else:
                    #dict[first] = 1
            for e in L:
                getFirst(e,dict)

#プログラムA
    count = 0
    x = scratch_block.block
    getFirst(s1,x)
    xx = x.keys()
    xx = sorted(xx)
    xxx = []
    for ww in xx:
        xxx.append(x[ww])

        #プログラムB
    count = 0
    y = scratch_block.block
    getFirst(s2,y)
    yy = y.keys()
    yy = sorted(yy)
    yyy = []
    for ww in yy:
        yyy.append(y[ww])



#cos類似度
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

    if __name__ == '__main__':
        sc = SimCalculator()
        cos = sc.sim_cos(xxx,yyy)
   # print "---------------------------"
  #  print "ブロック数のcos類似度 :"+str(sc.sim_cos(xxx,yyy))
    body = [count, count2, cos]


print "ブロック数 :"+ str(count)

print "スプライト数 :"+ str(count1)

writecsv.writerow(header)
writecsv.writerow(body)

f.close()
