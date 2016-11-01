import json
x = "crabsam.json"
f = open(x,'r')
data = json.load(f)
y = data["children"]
s = y[0][u'scripts']
print s

def map2(f,L):
    if isinstance(L, list):
        if L == []:
                return []
        else:
                return [map2(f,L[0])] + map2(f,L[1:])
    else:
        return f(L)
        
t = map2(lambda x: x, s)
print t

def printFirst(L):
    if isinstance(L, list):
            first = L[1]
            if isinstance(first, str):
                print first
            for e in L:
                printFirst(e)

def getFirst(L, dict):
        if isinstance(L,list):
            first = L[1]
            if isinstance(first, str):
                if first in dict:
                        dict[first] += 1
                else:
                        dict[first] = 1
            for e in L:
                getFirst(e, dict)
                
printFirst(t)
dictOne = {}
getFirst(t, dictOne)
print dictOne