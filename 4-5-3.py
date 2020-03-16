import pandas
import numpy

#랜덤으로 DataFrame 생성 ( 100행 4열 )

df=dataframe=pandas.DataFrame(numpy.random.randint(0,100,size=(100,4)),columns=list('ABCD'))
print(df)
print('==================================================')

df=dataframe=pandas.DataFrame(numpy.random.randint(0,100,size=(100,4)),columns=['one','two','three','four'])
print(df)
print('==================================================')

# df=dataframe=pandas.DataFrame(numpy.random.randn(100,4),columns=['one','two','three','four'])
# print(df)
# print('===================================================')

#CSV쓰기
df.to_csv('D:/miniProject/section4/result4-5-3.csv',index=False,header=False)
print('commit')
