# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot') 
font = {'family' : 'meiryo'}


df = pd.read_csv('result_pong1.csv')

df.plot.scatter(x='cos', y='splite')

plt.show()
plt.savefig("splite_graph.png")

