


# 1. 아메리카노 (4000)
# 2. 라떼 (4500)
# 3. 케이크 (6000)


menu_nu=int(input('메뉴 번호를 입력하세요: '))
menu_qty=int(input('수량을 입력하세요: '))

if menu_nu==1:  # 이 문제의 본질 (중요 개념) / “범위 판단” x /“정확한 값 매칭” o
    menu_nu=4000
elif menu_nu==2:
    menu_nu=4500
else:
    menu_nu=6000


def calculate():
    total=menu_qty*menu_nu
    return total 

print(calculate())