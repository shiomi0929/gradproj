from pylab import *
import pandas

x = (0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65,	0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1.05)
y = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36)

def open_with_pandas(filename):
    df = pandas.read_csv(filename)
    data = df.values
    return data

Z = open_with_pandas('cross_1_block_nl.csv')

X, Y = meshgrid(x,y)
pcolor(X, Y, Z)
colorbar()

show()

