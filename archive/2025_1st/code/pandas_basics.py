#1-pandas 기초 - Series&DataFrame 만들기
#series : 숫자 목록에 이름이 붙은 1차원 벡터
#dataframe : 여러개의 series 를 열로 모은 2차원 테이블

import pandas as pd
#값
s1=pd.Series([100,200,300])
print('기본 series:\n', s1)

#값+인덱스
s2=pd.Series([90,80,70], index=['국어','영어','수학'])
print('\n과목 점수 Series:\n',s2) #\n 한칸 띄어서

#2-dataframe 생성하기
import pandas as pd

data={'name':['hyunyoo','minji','kim'],'age':[21,21,23],'gender':['w','w','m']}

df=pd.DataFrame(data)

print(df)

import matplotlib.pyplot as plt

df['age'].plot(kind='bar')
plt.title('age spread')
plt.xlabel('human index')
plt.ylabel('age')
plt.show()

#3-pandas dataframe + matplotlib 시각화 확장

import pandas as pd
import matplotlib.pyplot as plt

data = {'name':['minji','hyunyoo','minsu'],'math':[90,80,100],'eng':[88,65,90]}

df=pd.DataFrame(data)
df.set_index('name', inplace=True) 
#inplace=True 원본 데이터프레임에 바로 적용한다는 뜻.

df.plot(kind='bar') #df.plot 은 pandas 에서 그래프 쉽게 그리도록 도와주는 메서드임.
plt.title('grade') #제목
plt.xlabel('name') #x축
plt.ylabel('score') #y축
plt.show() #화면 출력,호출