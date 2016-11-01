# -*- coding: utf-8 -*-
def printFirst(L):
    if isinstance(L, list):
        first = L[0]
        if isinstance(first, str):
            print first ###
        for e in L:
            printFirst(e)
        
def getFirst(L, dict):
    if isinstance(L, list):
        first = L[0]
        if isinstance(first,str):
            if first in dict:
                dict[first] += 1
            else:
                dict[first] = 1
        for e in L:
            getFirst(e,dict) ##  map を使ってもできる
           
          
                                            
jsonE = [[20, 63, [["whenGreenFlag"], ["doForever", [["forward:", 10], ["bounceOffEdge"]]]]],
				[38, 206, [["whenClicked"], ["say:duration:elapsed:from:", "Hello!", 2]]],				
				[38, 206, [["whenClicked"], ["say:duration:elapsed:from:", "Hello!", 2]]]
				]

printFirst(jsonE)

dictOne = {}
getFirst(jsonE,dictOne)
print dictOne

listOne = dictOne.keys();
listOne.sort();
print listOne

newList =[]
for e in listOne:
    newList.append( [e, dictOne[e]])
print newList

newList =[]
for e in listOne:
    newList.append( dictOne[e])
print newList


    
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







