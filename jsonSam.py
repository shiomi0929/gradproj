import json
x = "crabsam.json"
f = open(x,'r')
data = json.load(f)
y = data["children"]
s = y[0][u'scripts']
print s

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
            getFirst(e,dict) 
                
printFirst(s)
dictOne = {}
getFirst(s, dictOne)
print dictOne