# -*- coding: utf-8 -*-

'''
各モジュールをインポートする
jsonモジュール
urllib2モジュール
csvモジュール
'''

import json 
import urllib2 
import csv

'''
scratch_block.pyをインポートする
'''

import scratch_block 


'''
cos類似度を計算するSimCalculator.py のインポート
'''
from SimCalculator import SimCalculator


'''
事前に作成した分析対象プロジェクトをリスト化した
csvファイルの取得
'''
dataReader = csv.reader(open("pong.csv","rb"))


'''
ブロックの種類とその個数をカウントし、
scratch_block.pyに保存をする
'''

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

'''
比較対象となる元のプロジェクトのデータをURLよりプロジェクト番号をして取得
json形式のファイルを読み込み、"children"の持つリストに絞る
その中のブロックが使用されている "scripts"リストにさらに絞る
'''

url1 = 'http://projects.scratch.mit.edu/internalapi/project/'+'10000036'+'/get/'
r1 = urllib2.urlopen(url1)
root1 = json.loads(r1.read())
y1 = root1["children"]
a = "scripts"
s1 = []

'''
全体のブロック数をkeyの指定をしブロック数を数えるfor文によりscratch_block.pyの値を更新
'''

for i in range(len(y1)):
    if not a in y1[i].keys():
        continue
    s1 = s1 + y1[i][u'scripts']

'''
スプライト数が"objName"で指定されているためその個数を調べるfor文
'''

splite_count1 = 0
for i in range(len(y1)):
    if 'objName' in y1[i]:
        splite_count1 += 1
        

'''
元のプログラムの個数を求めていく
getFirstのメソッドを動かす
'''

count = 0
x = scratch_block.block
getFirst(s1,x)

'''
getFirstで集計された個数をブロックの名前順にソートをし、
ブロック名を覗くことでベクターを取得する
'''
xx = x.keys()
xx = sorted(xx)
xxx = []
for ww in xx:
    xxx.append(x[ww])
    

'''
for文でcsvファイルのURLを順番に取得し、計算を行う
'''

for row in dataReader:

    row = "".join(row)
    row = row.replace('https://scratch.mit.edu/projects/', '')
    print row


    '''
    比較をする２つ目のプロジェクトを読み込む
    以後元のプロジェクトに行った同様の処理を行う
    '''

    url2 = 'http://projects.scratch.mit.edu/internalapi/project/'+row+'get/'
    r2 = urllib2.urlopen(url2)
    root2 = json.loads(r2.read())
    y2 = root2["children"]
    s2 = []

    for i in range(len(y2)):
        if not a in y2[i].keys():
            continue
        s2 = s2 + y2[i][u'scripts']

    count = 0
    y = scratch_block.block
    
    '''
    １つ目のプロジェクトの個数がscratch_block.pyに残っているため初期化をする
    '''

    for www in y:
        y[www] = 0

    getFirst(s2,y)

    splite_count2 = 0
    for i in range(len(y2)):
        if 'objName' in y2[i]:
            splite_count2 += 1
            
    yy = y.keys()
    yy = sorted(yy)
    yyy = []
    for ww in yy:
        yyy.append(y[ww])

    '''
    １つ目、２つ目のプログラムよりcos類似度を計算するSimCalculatorの作動
    '''

    if __name__ == '__main__':
        sc = SimCalculator()
        cos = sc.sim_cos(xxx,yyy)
        print str(cos)

    '''
    分析結果を保存するcsvファイルの作成
    リストヘッダーの指定
    '''

    f = open("result_pong.csv", "w")
    writecsv = csv.writer(f)
    header = ['block', 'splite', 'cos']
    csvlist = []

    '''
    作成した結果をリスト化し、csvファイルに書き込む
    '''

    body = [count, splite_count2, cos]
    csvlist.append(body)



writecsv.writerow(header)
writecsv.writerows(csvlist)

f.close()
    
