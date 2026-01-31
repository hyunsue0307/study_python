# Day 5 – Python Refresher  


# 총 매출
orders = [
    {"menu": "아메리카노", "price": 4000, "qty":  2},
    {"menu": "라떼", "price": 4500, "qty": 1},
    {"menu": "케이크", "price": 6000, "qty": 1}
]

total=[]

for order in orders:
    menu=order['menu']
    price=order['price']
    qty=order['qty']
    cost=price*qty
    total.append(cost)

print(type(total)) #list
print(sum(total)) # 어떻게 합치지. sum() 사용이 안됨.

## 변수명으로 사용하지 않기
# sum
# list
# dict
# max
# min

# 어떻게 합치지. sum() 사용이 안됨.
#>> sum 은 내장함수인데 변수명으로 사용해버려서 함수가 가려짐.
# 따라서 cost, amount, order_total 다른 변수명 사용.

total=0

for order in orders:
    menu=order['menu']
    price=order['price']
    qty=order['qty']
    total+=price*qty # 누적. 굳이 list 안써도 됨.

print(total)

# 가장 비싼 주문

max_cost= 0 # max_cost 위치가 잘못됨
max_menu= 0 # 숫자보다는 빈문자열 추천 ''
for order in orders:
    menu=order['menu']
    price=order['price']
    qty=order['qty']
    cost=price*qty
    if cost>max_cost:
       max_cost = cost # == 비교 / = 대입 >> 문제 1: 대입 방향이 반대
       max_menu = menu
print(max_menu,max_cost)

# 메뉴별 매출 dict

cost_dic={}
for order in orders:
    menu=order['menu']
    price=order['price']
    qty=order['qty']
    cost=price*qty
    if menu not in cost_dic:
       cost_dic[menu]=cost # key = menu, value = cost
    else:
        cost_dic[menu]+=cost

print(cost_dic)