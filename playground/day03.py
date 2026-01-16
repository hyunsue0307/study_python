# # Single Receipt Purchase Composition Analysis



# items=[{'name':'황금밥알','category':'식료품','price':3400,'수량':1},
#        {'name':'우삼겹김치볶음밥','category':'식료품','price':2740,'수량':1},
#        {'name':'다이아몬드 리페어','category':'화장품','price':39850,'수량':1},
#        {'name':'컵누들','category':'간식','price':920,'수량':4},
#        {'name':'몬스터크랩','category':'식료품','price':3230,'수량':2},
#        {'name':'고메칠리감바스피자','category':'간식','price':5120,'수량':1},
#        {'name':'오동통모둠어묵','category':'식료품','price':6020,'수량':1},
#        {'name':'노엣지피자','category':'간식','price':2890,'수량':1},
#        {'name':'케라시스퍼퓸린스','category':'화장품','price':3540,'수량':1},
#        {'name':'고래바','category':'간식','price':1430,'수량':2},
#        {'name':'알참참동물복지유정란','category':'식료품','price':4470,'수량':1},
#        {'name':'씨네마팝콘','category':'간식','price':1040,'수량':1},
#        {'name':'새우탕컵','category':'간식','price':710,'수량':1},
#        {'name':'VT 리들샷','category':'화장품','price':8900,'수량':1},
#        ]

# # project 목표 : 카테고리별로 돈이 어디에서 얼마나 쓰였는지 분석하기

# total=0

# for item in items:
#     plu=item['수량'] #수량반영
#     price=item['price']
#     total+=price*plu




# print('총지출:',total,'원')

# categ_sum={}

# for item in items:
#     category=item['category']
#     price=item['price']
#     plu=item['수량']
#     cost=price*plu

#     if category not in categ_sum:
#         categ_sum[category]=0
#     categ_sum[category]+=cost

# print('\n카테고리별 지출:')
# for category,cost in categ_sum.items():
#     ratio = cost/total * 100
#     print(f"-{category}:{cost}원 ({ratio:.1f}%)")






#by me

items=[{'name':'황금밥알','category':'식료품','price':3400,'수량':1},
       {'name':'우삼겹김치볶음밥','category':'식료품','price':2740,'수량':2},
       {'name':'다이아몬드 리페어','category':'화장품','price':39850,'수량':1},
       {'name':'컵누들','category':'간식','price':920,'수량':5},
       {'name':'몬스터크랩','category':'식료품','price':3230,'수량':2},
       {'name':'고메칠리감바스피자','category':'간식','price':5120,'수량':1},
       {'name':'오동통모둠어묵','category':'식료품','price':6020,'수량':1},
       {'name':'노엣지피자','category':'간식','price':2890,'수량':1},
       {'name':'케라시스퍼퓸린스','category':'화장품','price':3540,'수량':1},
       {'name':'고래바','category':'간식','price':1430,'수량':2},
       {'name':'알참참동물복지유정란','category':'식료품','price':4470,'수량':1},
       {'name':'씨네마팝콘','category':'간식','price':1040,'수량':2},
       {'name':'새우탕컵','category':'간식','price':710,'수량':3},
       {'name':'VT 리들샷','category':'화장품','price':8900,'수량':2},
       {'name':'명란돌자반','category':'식료품','price':1930,'수량':2},
       {'name':'참숯란','category':'간식','price':1450,'수량':3},
       {'name':'바르는비트','category':'세탁용품','price':2120,'수량':1},
       {'name':'르샤트라섬유유연제','category':'세탁용품','price':2870,'수량':1},
       {'name':'하겐다즈미니컵마카다미아넛','category':'간식','price':2070,'수량':1},
       {'name':'비비고메추리알장조림','category':'식료품','price':2500,'수량':1},
       {'name':'비비고소고기장조림','category':'식료품','price':2560,'수량':2},
       {'name':'페리오클라이덴미배제','category':'화장품','price':11200,'수량':1},
       {'name':'하겐다즈미니컵스트로베리','category':'간식','price':1850,'수량':1},
       {'name':'코코도르퍼퓸디퓨저','category':'화장품','price':3270,'수량':1},
       {'name':'하겐다즈스트로베리앤크림아이','category':'간식','price':1770,'수량':2},
       {'name':'오랑지나','category':'간식','price':640,'수량':1},
       ]


categ_sum={}


total=0 #누적을 해줘야함. 아니면 계속 덮여쓰기됨.


for item in items:
    category=item['category']
    price=item['price']
    qu=item['수량']
    cost=price*qu
    total+=qu*price #누적을 해줘야함. 아니면 계속 덮여쓰기됨.
    if category not in categ_sum:
        categ_sum[category]=0
    categ_sum[category]+=cost



for category,cost in categ_sum.items():
    res=cost/total*100
    print(f"{category} 총합계:{cost} ({res}%)")

print(categ_sum.keys())