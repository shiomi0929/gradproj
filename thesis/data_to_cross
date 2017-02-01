import pandas

data = pandas.read_csv('1_block_x.csv')

crosstab = data.pivot_table(index='block', columns='cos', aggfunc=[len], fill_value=0)

crosstab.to_csv('cross_1_block_og.csv')
