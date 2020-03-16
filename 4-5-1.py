import pandas as pd
import csv


#기본읽기

df=pd.read_csv('D:/miniProject/section4/csv_s1.csv')
print(df)
print("=========================================")

df=pd.read_csv('D:/miniProject/section4/csv_s1.csv',skiprows=[0])
print(df)
print("=========================================")

df=pd.read_csv('D:/miniProject/section4/csv_s1.csv',skiprows=[0],header=None)
print(df)
print("=========================================")

df=pd.read_csv('D:/miniProject/section4/csv_s1.csv',skiprows=[0],header=None,names=["month",2018,2019,2020])
print(df)
print("=========================================")

df=pd.read_csv('D:/miniProject/section4/csv_s1.csv',skiprows=[0],header=None,names=["month",2018,2019,2020]\
,index_col=[0])
print(df)
print("=========================================")

df=pd.read_csv('D:/miniProject/section4/csv_s1.csv',skiprows=[0],header=None,names=["month",2018,2019,2020]\
,na_values=["JAN"])
print(df)
print(pd.isnull(df))
print("=========================================")

df=pd.read_csv('D:/miniProject/section4/csv_s1.csv',skiprows=[0],header=None,names=["month",2018,2019,2020]\
)
print(df)
print(df.index)
print(df.index.values)
print(df.index.values.tolist())
print(df.rename(index=lambda x:x+1))
print(df.rename(index=lambda x:x+1).index)

#=========================================================================2

df2=pd.read_csv('D:/miniProject/section4/csv_s2.csv',sep=';')
print(df2)
print('==========================================================')
df2=pd.read_csv('D:/miniProject/section4/csv_s2.csv',sep=';',index_col=[0])
print(df2)
print('==========================================================')
df2=pd.read_csv('D:/miniProject/section4/csv_s2.csv',sep=';',index_col=[0],skiprows=[0])
print(df2)
print('==========================================================')
df2=pd.read_csv('D:/miniProject/section4/csv_s2.csv',sep=';',skiprows=[0],names=["First name","Test1","Test2","Test3","Final3","Grade"])
print(df2)
print('==========================================================')

#원본 colums 변경
print(df2['Grade'])
df2['Grade']=df2['Grade'].str.replace('"',' ')
print(df2)
print('==========================================================')

df2['Grade']=df2['Grade'].str.replace('C+','A++')
print(df2)
print('==========================================================')

#평균 컬럼 추가
df2['AVG']=df2[['Test1','Test2','Test3','Final3']].mean(axis=1)
print(df2)

#합계 컬럼 추가
df2['SUM']=df2[['Test1','Test2','Test3','Final3']].sum(axis=1)
print(df2)
