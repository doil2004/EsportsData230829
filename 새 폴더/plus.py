import pandas as pd
from pandas import DataFrame
from pandas import Series
import matplotlib.pyplot as plt

# 딕셔너리
pd.set_option('display.max_rows', 181)
csv_data_df = pd.read_csv('stactOfChampion.csv')

print(csv_data_df)

df=DataFrame(csv_data_df)

plt.scatter(x=df['KDA'],y=df['GOLD%'])
plt.show()