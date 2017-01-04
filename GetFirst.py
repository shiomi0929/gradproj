# -*- coding: utf-8 -*-

class GetFirst():
    def getFirst(L, dict):
        global count
        if isinstance(L, list)and len(L)>0 :
            first = L[0]
            if isinstance(first,unicode):
                '''
                例外ブロックの処理
                '''
                if "turnRight:" in first:
                    first = first.rstrip(":")
                if "turnLeft:" in first:
                    first = first.rstrip(":")
                if "wait:elapsed:from:" in first:
                    first = first.rstrip(":")
                        
                if first in dict:
                    dict[first] += 1
                    count += 1
            for e in L:
                getFirst(e,dict)
