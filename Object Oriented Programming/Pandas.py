import pandas as pd

stock_list=pd.read_csv('stocks.list.csv',index_col=0)

print(stock_list)
print(" ")

print(stock_list['ISIN'])

print(stock_list[['ISIN','TOTALTRADES']])