import pandas
import xlrd
import openpyxl

#기본 읽기
df=pandas.read_excel('D:/miniProject/section4/excel_s1.xlsx')
print(df)
print('=============================================')
print(df.head(10))
print(df.tail(10))
print('===========================================')
#행, footer 스킵
df=pandas.read_excel('D:/miniProject/section4/excel_s1.xlsx',skiprows=[0],skipfooter=45)
print(df)

print('===================================================')
#헤더 정의1
df=pandas.read_excel('D:/miniProject/section4/excel_s1.xlsx',header=0)
print(df)
print(list(df))
print('===========================================')
#헤더 정의2
df=pandas.read_excel('D:/miniProject/section4/excel_s1.xlsx',header=None,skiprows=[0],names=["state",2018,2019,2020])
print(df)
print("===========================================================")

#값 치환
df=pandas.read_excel('D:/miniProject/section4/excel_s1.xlsx',header=0,na_values='....',\
converters={"2018":lambda w : w if w > 60000 else None})

print(df)
print(pandas.isnull(df))
print('------------------------------------------------------------')
#인덱스 재정의
df=pandas.read_excel('D:/miniProject/section4/excel_s1.xlsx')
print(df)
print(df.rename(index=lambda x : x+1))
