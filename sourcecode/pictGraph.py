# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot') 
font = {'family' : 'meiryo'}
#matplotlib.rc('font', **font)


df = pd.read_csv('result_pong1.csv')

fig, axes = plt.subplots(figsize=(14, 10), sharey=True)
df.plot.scatter(x='cos', y='block')

plt.show()

