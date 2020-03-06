#loading the data in jupitor notebook
import pandas as pd
df=pd.read_csv('Desktop/kyphosis.csv')
index_df=df.index
size_df=df.size
df.shape#rows and columns in a tuple format here it is(81,4)
df.isnull()#it displays false(if there is no null) other wise it displays(True)
df.isnull().sum()#it gives sum of the nulls present in the respective fields
df['Number'].isnull().sum()#it gives sum of nulls present in the respective columns here it is Number,Age,etc
df.replace('absent','NO')#here it replaces the ansent value with no in main csv file