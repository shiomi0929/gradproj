# -*- coding: utf-8 -*-

#import numpy as np


import json
import scratch_block
#プログラム1
input1 = raw_input()
x1 = input1
f1 = open(x1,'r')
data = json.load(f1)
y1 = data["children"]
s1 = y1[0][u'scripts']

#プログラム2
input2 = raw_input()
x2 = input2
f2 = open(x2,'r')
data = json.load(f2)
y2 = data["children"]
s2 = y2[0][u'scripts']


def printFirst(L):
    if isinstance(L, list):
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
    if isinstance(L, list):
        first = L[0]
        if isinstance(first,unicode):
            if first in dict:
                dict[first] += 1
            else:
                dict[first] = 1
        for e in L:
            getFirst(e,dict)

getFirst(s1,scratch_block.block)
x = scratch_block.block
#print result.values()

getFirst(s2,scratch_block.block)
y = scratch_block.block
#print result.values()
#result_s = sorted(result.items(), reverse = True, key = lambda x: x[1])
#print result_s
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
        for n in v1:
            if n in v2:
                numerator += v1[n] * v2[n]

        denominator = self._absolute(v1) * self._absolute(v2)

        if denominator == 0:
            return 0
        return numerator / denominator

if __name__ == '__main__':
    sc = SimCalculator()
    print(str(sc.sim_cos(x,y)))
