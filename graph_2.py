# -*- coding: utf-8 -*-



import pandas as pd
import numpy as np
import seaborn as sns


df = pd.read_csv('result_pong1.csv')

#散布図とヒストグラム
sns.jointplot(x='cos', y='block', kind="kde", data=df)
sns.plt.show()
