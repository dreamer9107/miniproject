import datetime
import FinanceDataReader
import sys
import io
from pandas import Series,DataFrame

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


#조회 시작 날짜
start=datetime.datetime(2020,2,19)
#조회 마감 날짜
end=datetime.datetime(2020,3,4)

# #한국 거래소 상장 종목 전체
# df_krx=FinanceDataReader.StockListing('KRX')
#
# #리스트 10개 출력
# print(df_krx.head(10))
#
# #출력
# print(df_krx.index)
# print(df_krx['Symbol'])
# print(df_krx.iloc[0])
# print(df_krx.describe())

# #미국 APPLE 금융 정보 호출
# df_app=FinanceDataReader.DataReader('AAPL',start,end)
# print(df_app.head(10))
# print(df_app.loc['2020-02-19'])
# print(df_app.describe())


#아마존 금융 정보 호출
df_am=FinanceDataReader.DataReader('AMZN',start,end)
print(df_am.head(10))
print(df_am.loc['2020-02-28'])
print(df_am.describe())


#구글 금융 정보 호출
df_gg=FinanceDataReader.DataReader('VXGOG',start,end)
print(df_gg.head(10))
print(df_gg.loc['2020-03-03'])
print(df_gg.describe())
