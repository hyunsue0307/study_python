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