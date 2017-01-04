#coding:utf-8
import csv
import json
import urllib2

dataReader = csv.reader(open("id.csv","rU"))

f = open("result.csv", "w")
writecsv = csv.writer(f)
header = ['block', 'splite', 'cos']
body = []

url1 = 'http://projects.scratch.mit.edu/internalapi/project/'+'116739847'+'/get/'
r1 = urllib2.urlopen(url1)
root1 = json.loads(r1.read())
y1 = root1["children"]
print url1

##

x = 0
y = 0
z = 0

for row in dataReader:

    row = "".join(row)
    print row
    
    """
    url2 = 'http://projects.scratch.mit.edu/internalapi/project/'+row+'/get/'
    r2 = urllib2.urlopen(url2)
    root2 = json.loads(r2.read())
    y2 = root2["children"]
    """

    count = x
    count2 = y
    cos = z

    x += 1
    y += 1
    z += 1

    body = [count, count2, cos]
##

writecsv.writerow(header)
writecsv.writerow(body)

f.close()

