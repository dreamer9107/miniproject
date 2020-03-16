from bs4 import BeautifulSoup
import urllib.request as req
import os.path
import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url="https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
savename="D:/miniProject/section4/forecast.xml"

if not os.path.exists(savename):
    req.urlretrieve(url,savename)

#BeautifulSoup 로 분석

xml=open(savename,'r',encoding='utf-8').read()
soup=BeautifulSoup(xml,"html.parser")
# print(soup)
info={} # {'서울':2,7,20}
for location in soup.find_all("location") :
    city=location.find("city").string
    # print(city)
    weather=location.find_all("tmn")
    # print(weather)
    if not(city in info):
        info[city]=[] #keys 값 (중복이 없을 때만 ) (서울)
    for tmn in weather:
        info[city].append(tmn.string) # values 값 (2,7) ()키값에 해당되는)

# print(info)
# print(list(info.keys()))
# print(info.values())

with open("D:/miniProject/section4/cast.txt",'wt',encoding='utf-8') as f:
    for city in sorted(info.keys()):
        print('도시지역',city) #콘솔창에
        f.write(str(city)+'\n') #text 파일로 저장
        for tmp in info[city]:
            print('기온 : ',tmp)
            f.write('\t'+str(tmp)+'\n')
