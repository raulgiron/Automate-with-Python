import pandas as pd


df = pd.read_excel('/Users/raulgiron/Desktop/AutomateWithPython/supermarket_sales.xlsx')
df = df[['Gender', 'Product line', 'Total']]
# print(df)

pivot_table = df.pivot_table(index='Gender', columns='Product line', values='Total', aggfunc='sum')
# print(pivot_table)

pivot_table.to_excel('/Users/raulgiron/Desktop/AutomateWithPython/pivot_table_supermarket_sales.xlsx', 'Report', startrow=4)
