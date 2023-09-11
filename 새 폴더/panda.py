import pandas as pd
# 딕셔너리
pd.set_option('display.max_rows', 181)
csv_data_df = pd.read_csv('stactOfChampion.csv')

print(csv_data_df)