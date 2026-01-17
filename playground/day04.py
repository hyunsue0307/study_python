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


dic={}
total=0

for item in items:
    category=item['category']
    price=item['price']
    qu=item['수량']
    cost=qu*price
    total+=qu*price #전체 가격은 품목과 상관없이 계속 누적
    if category not in dic:
        dic[category]=0
    dic[category]+=cost   

print(f'총지출:{total}')

for category,cost in dic.items():
    res=cost/total*100 #어떤 값에 대한 계산이면 그 값을 꺼낸 순간에 계산한다. cost 에 대한 계산은 cost 있는 문에서
    print(f"{category} : {cost} ({res}%)")


# #결과값
# 식료품 총합계:37310 (24.858418282363914%)
# 화장품 총합계:75660 (50.4097541475115%)
# 간식 총합계:32130 (21.407155706576052%)
# 세탁용품 총합계:4990 (3.3246718635485375%)



# 조건분석 > 3천원 이상 상품만 포함

item_dic={}
total=0
for item in items:
    price=item['price']
    category=item['category']
    qu=item['수량']
    if price>=3000:
        cost=qu*price
        total+=cost    #전체도 조건적용시켜야함.
        if category not in item_dic:
              item_dic[category]=0
        item_dic[category]+=cost    

        #애초에 price < 3000 이하는 포함시키지 말자. 


for category,cost in item_dic.items():
     res=cost/total*100
     print(f'{category}:{cost} ({res}%)')

##>> 결과 : 소액다품목 성격이 강함.


## top 3 품목

lis=[]

for item in items:
    price=item['price']
    qu=item['수량']
    name=item['name']
    cost=qu*price
    lis.append((name,cost))

# (a, b)를 정렬하면
# → a를 먼저 보고
# → a가 같으면 b를 본다


print(lis)


# lis.sort(key=lambda x: x[1]) # 새로운 객체에 넣지 못함.
# print(lis)

res=sorted(lis, key=lambda x: x[1],reverse=True) # 새로운 객체에 넣음.
#lis를 정렬하되 각 원소 x에서 x[1](=cost)를 기준으로 큰 순서대로 정렬해라.
print(res)


print(f'top1:{res[0]}\n top2:{res[1]}\n top3:{res[2]}')

# > 여기 어떻게 해야 이름까지 출력이 가능할까,, dic 을 쓰면 정렬에서 문제가 생기고,, 리스트로 정렬해서 쓰면 이름은 지워지고,,


# sort()는 기존에 선언한 변수를 update해주는 기능+정렬이고,
# sort() - 문법은 list.sort()이며, 내부 파라미터는 key=None과 reverse = False가 default로 설정되어 있다.
# 주의할 점은 list1 = list1.sort() 이런식으로 새로운 변수에 선언할 순 없다. 객체 자체를 변경시키는 기능이 이미 있기때문

# 새로운 객체에 정렬된 리스트를 선언하고 싶은 경우에 사용되고 이 때, sorted() 함수를 써야한다. 
# sorted()는 기존에 선언한 변수를 update하지 않고, 정렬된 결과만 보여주는 역할

