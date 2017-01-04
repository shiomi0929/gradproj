# -*- coding: utf-8 -*-

import json #jsonモジュールのインポート
import scratch_block #scratchブロックの辞書のインポート
import urllib2 #urllib2モジュールのインポート

#cos類似度計算ファイルのインポート
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

#元のファイルの読み込み
url1 = 'http://projects.scratch.mit.edu/internalapi/project/'+'10000036'+'/get/'
r1 = urllib2.urlopen(url1)
root1 = json.loads(r1.read())
y1 = root1["children"]
a = "scripts"
s1 = []

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
    
#SimCalculatorを使って計算
if __name__ == '__main__':
    sc = SimCalculator()
    cos = sc.sim_cos(xxx,yyy)
    print str(cos)
    
