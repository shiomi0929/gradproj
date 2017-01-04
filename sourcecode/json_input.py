# -*- coding: utf-8 -*-

import json
import scratch_block
input = raw_input()
x = input
f = open(x,'r')
data = json.load(f)
y = data["children"]
s = y[0][u'scripts']


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

getFirst(s,scratch_block.block)

result = scratch_block.block
#result_s = sorted(result.items(), reverse = True, key = lambda x: x[1])
#print result_s

print result.values()
#print sorted(result.values(), reverse = True)

# どのjson データにも、同じ長さのリストになる
# 同じ位置に、同じ先頭語の頻度がくる。そのため、語情報は省いてもよい。
# 省くと、次のようなリスト（ベクター）を作ることができる
# [0, 0, 3, 10, 2 ,3, 0, 0 , 2, 3 ,0 ]