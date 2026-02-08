## 단계 0 > 분석 목적 : 시간대 마다 (오픈 / 미들) 가격 상관없이 어느 메뉴가 수량이 제일 많이 나갔는가?
## 시간대 오픈/미들 에서의 1,2,3 등을 구하기

# 메뉴 - o
# 시간대 : 9~12(오픈) / 12~17(미들) - o
# 수량 - o

# 포장 vs 매장 - ^ (데이터 많아지면 추가)
# hot vs ice - ^ (계절분석에 용이)
# big vs 초대용량 - ^ (옵션처리도 나중 추가)

# 베이커리 vs 음료 vs 혼합 - x (불필요)

# # 스키마:

# 시간대 나누기
# 각 시간대 안에서 판매수량 구하기
# 수량 기준 내림차순 정렬
# top 3 메뉴 뽑기

records=[
    {'time':'오픈','menu':'아메리카노','qty':18},
    {'time':'오픈','menu':'유자티','qty':2},
    {'time':'오픈','menu':'로얄밀크티','qty':1},
    {'time':'오픈','menu':'카라멜라떼','qty':1},
    {'time':'오픈','menu':'바닐라라떼','qty':2},
    {'time':'오픈','menu':'베이글','qty':1},
    {'time':'오픈','menu':'아이스티','qty':3},
    {'time':'오픈','menu':'카푸치노','qty':1},
    {'time':'오픈','menu':'소금식빵','qty':1},
    {'time':'오픈','menu':'도넛','qty':1},
    {'time':'오픈','menu':'옥수수빵','qty':1},

    {'time':'미들','menu':'아메리카노','qty':44},
    {'time':'미들','menu':'유자티','qty':3},
    {'time':'미들','menu':'밀크티','qty':2},
    {'time':'미들','menu':'바닐라라떼','qty':5},
    {'time':'미들','menu':'아이스티','qty':8},
    {'time':'미들','menu':'소금식빵','qty':4},

    {'time':'미들','menu':'말차라떼','qty':5},
    {'time':'미들','menu':'카페라떼','qty':6},
    {'time':'미들','menu':'딸기라떼','qty':4},
    {'time':'미들','menu':'쿠키','qty':1},
    {'time':'미들','menu':'저칼로리탄산','qty':2},
    {'time':'미들','menu':'마카롱','qty':1},
    {'time':'미들','menu':'꺠찰빵','qty':2},
    {'time':'미들','menu':'오믈렛','qty':3},
    {'time':'미들','menu':'망고라떼','qty':1},
    {'time':'미들','menu':'케이크','qty':6},
    {'time':'미들','menu':'돌체라떼','qty':1},
    {'time':'미들','menu':'크로칸슈','qty':1},
    {'time':'미들','menu':'블루베리','qty':1},

]

# 시간대별로 보고싶은거니까 시간대별로 다시 넣기

open_time=[]
middle_time=[]

for record in records:
    if record['time']=='오픈':
        open_time.append(record)
    elif record['time']=='미들':
        middle_time.append(record)

# print(open_time)

# 뭔가 튜플로 바꾸면 (메뉴,수량) 해서출력할 수 있을 것 같은데 튜플을 어떻게 만들지


def lis(time):
    x=[] #변수명 pairs 로 추천! 변수명 잘 짓는게 의외로 중요함.
    for i in time:
        menu=i['menu']
        qty=i['qty']
        pair=(menu,qty) # 튜플 만들기 짱 쉽다!!
        x.append(pair)
    resort=sorted(x,key=lambda x:x[1],reverse=True)
    top_3=resort[0:3]
    return top_3


open_top3=lis(open_time)
middle_top3=lis(middle_time)


print(open_top3)
print(middle_top3)

# resort=sorted(x,key=lambda x:x[1],reverse=True)
# print(resort[0:3]) # 끝은 포함 안됨. 0,1,2 출력하려면 [0:3]








# range > 함수임. (0,~) 함수 전달 인자

# for i in middle_time:
#     menu=i['menu']
#     qty=i['qty']
#     if menu not in top_model:
#         top_model.append(menu,qty)
