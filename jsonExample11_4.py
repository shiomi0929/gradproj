# -*- coding: utf-8 -*-

import json
import scratch_block
x = "project.json"
f = open(x,'r')
data = json.load(f)
y = data["children"]
s = y[0][u'scripts']
print s


def printFirst(L):
    #print "first"
    #print L
    if isinstance(L, list):
        first = L[0]
        #print first
        if isinstance(first, unicode):
            print first ###
        for e in L:
            printFirst(e)
            if first in dict:
                dict[first] += 1
            else:
                dict[first] = 1
        for e in L:
            getFirst(e,dict) 
            
#print "end"
        
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
                                            

#printFirst(s)


#x = "scratch_block.py"
#dictOne = open(x,'r')
#dictOne = json.load(f)
#dictOne = {}


result = scratch_block.block
print sorted(result.items(), reverse = True, key = lambda x: x[1])


#listOne = dictOne.keys();
#listOne.sort();
#print listOne

#newList =[]
#for e in listOne:
#newList.append( [e, dictOne[e]])
#print newList

#newList =[]
#for e in listOne:
#newList.append( dictOne[e])
#print newList


    
# scratch block の先頭語の辞書をつくる。
# 例 {'whenclicked':0, 'move';0, ...... } 
# その辞書を使って、出現頻度をカウントする。
# 結果の辞書を、リストにし、ソートする。 
#listOne = dictOne.keys();
#listOne.sort();

# そのリストを使って、リストのリストをつくる。
#for e in listOne:
#    newList.append( [e, dictOne[e]])
#print newList
    
# どのjson データにも、同じ長さのリストになる
# 同じ位置に、同じ先頭語の頻度がくる。そのため、語情報は省いてもよい。
# 省くと、次のようなリスト（ベクター）を作ることができる
# [0, 0, 3, 10, 2 ,3, 0, 0 , 2, 3 ,0 ]







