import pandas
import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


df2=pandas.read_csv('D:/miniProject/section4/csv_s2.csv',sep=';',skiprows=[0],names=["First name","Test1","Test2","Test3","Final","Grade"])
print(df2)
df2=df2.rename(index=lambda x:x+1)

df2['Grade']=df2['Grade'].str.replace('"',' ')
print(df2)

df2['AVG']=df2[["Test1","Test2","Test3","Final"]].mean(axis=1)
df2['SUM']=df2[["Test1","Test2","Test3","Final"]].sum(axis=1)
print(df2)



#csv 쓰기

df2.to_csv('D:/miniProject/section4/result_csv_s2.csv',index=False)
print("저장 완료")
