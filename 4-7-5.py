import matplotlib.pyplot as plt

#fig 객체 생성
fig=plt.figure()


#서브 슬롯 생성(2행 1열)
ax1=fig.add_subplot(2,1,1)
ax2=fig.add_subplot(2,1,2)


#x축 생성
x=range(0,100)

#y축1 생성 (제곱)
y1=[v*v for v in x]

#y축2 생성 v*v*2
y2=[v*v*2 for v in x]

#멀티 라인(1행 1열)
ax1.plot(x,y1,'b',y2,'r--')
#멀티 라인(2행 2열)
ax2.bar(x,y1)
#출력
plt.show()
