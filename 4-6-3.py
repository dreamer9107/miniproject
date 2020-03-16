import pandas
import numpy
import xlrd
import openpyxl
import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


df=pandas.DataFrame(numpy.random.randint(500,1000,size=(100,4)),columns=[2015,2016,2017,2018])
print(df)


#csv index,header(True,False)
#excel index(None),header(True,False)


#excel 쓰기
df.to_excel('D:/miniProject/section4/result4-6-3.xlsx',index=None)
print('commit')
