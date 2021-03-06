# -*- coding: utf-8 -*-

#import numpy as np


import json
import scratch_block
import urllib2


import csv   #csvモジュールをインポートする

###
dataReader = csv.reader(open("id.csv","rU"))

f = open("result.csv", "w")
writecsv = csv.writer(f)
header = ['block', 'splite', 'cos']
csvlist = []
###


from SimCalculator import SimCalculator



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

        
    ###
url1 = 'http://projects.scratch.mit.edu/internalapi/project/'+'116739847'+'/get/'
r1 = urllib2.urlopen(url1)
root1 = json.loads(r1.read())
y1 = root1["children"]


a = "scripts"
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
        ###

#プログラムA
count = 0
x = scratch_block.block
getFirst(s1,x)

print "プログラムA"
print "ブロック数 :"+ str(count)
print "スプライト数 :"+ str(count1)


xx = x.keys()
xx = sorted(xx)
xxx = []
for ww in xx:
    xxx.append(x[ww])
    



for row in dataReader:

    row = "".join(row)
    row = row.replace('https://scratch.mit.edu/projects/', '')
    print row


###
    url2 = 'http://projects.scratch.mit.edu/internalapi/project/'+row+'get/'
    r2 = urllib2.urlopen(url2)
    root2 = json.loads(r2.read())
    y2 = root2["children"]

    s2 = []

    #全体のブロック数の合計
    for i in range(len(y2)):
        if not a in y2[i].keys():
            continue
        s2 = s2 + y2[i][u'scripts']

    #プログラムB
    count = 0
    y = scratch_block.block
    for www in y:
        y[www] = 0

    getFirst(s2,y)

    #スプライトの数
    count2 = 0
    for i in range(len(y2)):
        if 'objName' in y2[i]:
            count2 += 1
    ###

    yy = y.keys()
    yy = sorted(yy)
    yyy = []
    for ww in yy:
        yyy.append(y[ww])


    if __name__ == '__main__':
        sc = SimCalculator()
        cos = sc.sim_cos(xxx,yyy)
        print str(cos)

    body = [count, count2, cos]
    csvlist.append(body)

writecsv.writerow(header)
writecsv.writerows(csvlist)

f.close()
    
