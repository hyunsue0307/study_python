# simple menu order program

menu_nu=int(input('메뉴 번호를 입력하시오.:'))
menu_qt=int(input('메뉴 수량을 입력하시오.:'))

if menu_nu==1:
    menu_nu=4000
elif menu_nu==2:
    menu_nu=4500
else:
    menu_nu=6000


# 함수는 값을 저장하는 곳이 아니라 값이 들어올 자리를 미리 만들어두는 구조

def calculate(x,y):
    total=x*y
    return total

result=calculate(menu_nu,menu_qt)
print(f" 총 금액 : {result}")




# day07-2 : 할인 적용 총 금액 계산

def calculate(x,y): # x,y 를 명시하는것이 함수의 역할을 설명
    total=x*y
    if total >= 10000:
        result=total*0.1
    else:
        result=0
    return total-result

result=calculate(menu_nu,menu_qt) # 실행부는 항상 아래
print(f" 총 금액 : {result}")