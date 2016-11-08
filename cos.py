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
result = scratch_block.block
print result.values()

getFirst(s2,scratch_block.block)
result = scratch_block.block
print result.values()
#result_s = sorted(result.items(), reverse = True, key = lambda x: x[1])
#print result_s


#print sorted(result.values(), reverse = True)

# どのjson データにも、同じ長さのリストになる
# 同じ位置に、同じ先頭語の頻度がくる。そのため、語情報は省いてもよい。
# 省くと、次のようなリスト（ベクター）を作ることができる
# [0, 0, 3, 10, 2 ,3, 0, 0 , 2, 3 ,0 ]

import numpy as np

def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

if __name__ == '__main__':
    x = np.array([1, 1, 1, 1, 1])
    y = np.array([1, 0, 1, 0, 1])
    z = np.array([0, 1, 0, 0, 0])
    
    print cos_sim(x, y)
    print cos_sim(y, z)
    print cos_sim(z, x)

