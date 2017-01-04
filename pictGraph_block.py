# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


plt.style.use('ggplot') 
font = {'family' : 'meiryo'}
#matplotlib.rc('font', **font)
df = pd.read_csv('result_pong1.csv')

df.plot.scatter(x='cos', y='block')
#plt.xticks(np.arange(0,1.2,0.1))
#plt.yticks(np.arange(0,10,0.1))

#out = sns.regplot(x='cos',y='block', scatter_kws={'c':df['c'],'cmap':'jet','s':df['c']*100})

plt.show()
plt.savefig("block_graph.pdf")
