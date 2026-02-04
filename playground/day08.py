# 워밍업!
nums=[3,7,2,9]

total=0 # 초기값을 0으로 두는 것을 기본으로.
for num in nums:
    total+=num

print(total)


# max > 내장 '함수'라서 비교대상이 될 수 없음. 따라서 초기값을 업데이트 해주는게 방법이 될 수 있음.
ma=0
for num in nums:
    if num > ma:
        ma=num

print(ma)

i=0
total=0 # 위에서 total 이 이미 있기때문에 다시 0으로 갱신.
for num in nums:
    total+=num
    i+=1

print(total/i)

# len() : 여러 개의 요소를 담고 있는 자료형에 가능.
total=0
for num in nums:
    total+=num

print(total/len(nums))

# 카페주문 계산기 (함수+딕셔너리+리스트)
menu = {
    "아메리카노": 4000,
    "라떼": 4500,
    "케이크": 6000
} # 딕셔너리는 그냥 돌리면 key 값만 나옴. items() 붙여야함.

orders = [
    ("아메리카노", 2),
    ("케이크", 1)
] # 두가지를 동시에 꺼내올 수 있음. ex) for item,qty in orders


def calculate_total(menu, orders):
    total=0 # 구하는 값 > 초기값
    for item,qty in orders: 
        # 없는 order 은 조용히 무시
        if item in menu: # menu > key 값
            price=menu[item] # menu[item] > value 값
            total+=price*qty
    return total
total=calculate_total(menu,orders)
print(total)

# 예제 : 1

menu = {
    "아메리카노": 4000,
    "라떼": 4500,
    "케이크": 6000
}

orders = [
    ("라떼", 1),
    ("아메리카노", 3)
]

def calculate_total(menu,orders):
    total=0
    for item,qty in orders:
        if item in menu:
            total+=menu[item]*qty # 제발,,누적을 까먹지 말자.. 덮어쓰기 하려는 것이 아니잖냐,,
    return total

total=calculate_total(menu,orders)
print(total)


# 예제 -2: 수량이 2개 이상이면 해당 메뉴 금액의 10%

menu = {
    "아메리카노": 4000,
    "라떼": 4500,
    "케이크": 6000
}

orders = [
    ("아메리카노", 2),
    ("케이크", 1)
]

def calculate_total(menu,orders):
    total=0 # for 문 안에 들어가면 계속 0으로 업데이트 되니까 밖에서.
    for item,qty in orders:
        if item in menu:
            price=menu[item]
            if qty>=2:
                price=price*0.9
            total+=price*qty # 초기값 설정해야함.
        
    return total

total=calculate_total(menu,orders)
print(total)

# 번외 (수량까지 포함한 금액에서 할인)


menu = {
    "아메리카노": 4000,
    "라떼": 4500,
    "케이크": 6000
}

orders = [
    ("아메리카노", 2),
    ("케이크", 1)
]

def calculate_total(menu,orders):
    total=0 
    for item,qty in orders:
        if item in menu:
            price=menu[item]
            amount=price*qty
            if qty>=2:
                amount=amount*0.9
            total+=amount
            

        
    return total

total=calculate_total(menu,orders)
print(total)