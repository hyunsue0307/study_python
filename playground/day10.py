## day09 > day10 : result > action


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

open_time=[]
middle_time=[]

for record in records:
    if record['time']=='오픈':
        open_time.append(record)
    elif record['time']=='미들':
        middle_time.append(record)

def lis(time):
    x=[] 
    total=0
    for i in time:
        menu=i['menu']
        qty=i['qty']
        total+=qty
        pair=(menu,qty) 
        x.append(pair)
    resort=sorted(x,key=lambda x:x[1],reverse=True)
    top_3=resort[0:3]
    rat=[]
    for menu,qty in top_3: # 언패킹 > 두개 꺼낼 수 있음.
        rat.append(qty/total)
    return top_3,rat # return a,b 는 두개 각각 주는게 아니라 '튜플'로 묶어서 하나로 줌.
    # return x, y = retrun (x,y)


# 언패킹 > 변수 이름붙이기
open_top3=lis(open_time) 
open_menus, open_ratios = open_top3

middle_top3=lis(middle_time)
middle_menus, middle_ratios = middle_top3


for i in range(3):
    menu,qty=open_menus[i] # 언패킹!!
    print(f"{i+1}위 메뉴: {menu}\n수량: {qty}잔\n비중: {open_ratios[i]*100:.1f}% ") 
    # 언패킹 사용 + 비율을 보기 좋게 *100


for i in range(3):
    menu,qty=middle_menus[i] 
    print(f"{i+1}위 메뉴: {menu}\n수량: {qty}잔\n비중: {middle_ratios[i]*100:.1f}% ") 
