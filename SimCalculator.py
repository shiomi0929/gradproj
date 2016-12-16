# -*- coding: utf-8 -*-

#cos類似度
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
        i = 0
        for n in v1:
            numerator += v1[i]*v2[i]
            #if n in v2:
            # numerator += v1[n] * v2[n]
            #print i, numerator, v1[i], v2[i]
            i=i+1
            
            ss1 = []
            ss2 = []
        for x in v1:
            ss1.append(x*x)
        for x in v2:
            ss2.append(x*x)

        denominator = math.sqrt(sum(ss1))*math.sqrt(sum(ss2))
        
        if denominator == 0:
            return 0
        return numerator / denominator
