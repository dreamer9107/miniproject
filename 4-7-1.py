from pandas import Series

#series 선언
series1=Series([92600,92400,92100,94300,92300])
#출력
print(series1)
#총개수
print('count',series1.count())
#요약
print(series1.describe())
#인턴스 접근
print(series1[0])

#series2 선언
series2=Series([92600,92400,92100,94300,92300],index=['2018-02-19','2019-11-16','2020-06-08','2018-03-19','2018-04-19'])
print(series2)

for date in series2.index:
    print('date  : ',date)

    print('values: ',series2[date])

for price in series2.values:
    print(price)


#series3 선언
series_g1 = Series([10,20,30], index=['n1','n2','n3'])
series_g2 = Series([10,20,30], index=['n2','n1','n3'])

#series 병합 & 계산
sum=series_g1+series_g2
mul=series_g1*series_g2
cul=(series_g1*series_g2)*0.5

#출력
print("====sum====")
print(sum)
print("====mul====")
print(mul)
print("====cul====")
print(cul)
