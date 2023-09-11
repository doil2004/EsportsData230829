import pandas as pd
from pandas import DataFrame
from pandas import Series
import matplotlib.pyplot as plt

방문수=[2,3,5,7]
체류시간=[15,18,25,35]
구매여부=[0,1,0,1]

data={'방문수':방문수,'체류시간':체류시간,'구매여부':구매여부}
df=DataFrame(data)

plt.scatter(x=df['방문수'],y=df['체류시간'],c=df['체류시간'])
plt.show()