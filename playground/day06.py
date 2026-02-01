


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

calculate() # calculate() → 어떤 숫자 하나를 만들어냄 > 그냥 공중에 버린상태
print(calculate()) # calculate 실행 // return total → 값 하나 반환 // print(그 값) → 화면에 출력


## 보통 이렇게 쓰임 > 변수에 담기.

result = calculate()
print(result)

## return 에 대한 정리!!
# return은 값을 함수 밖으로 전달
# print는 사람에게 보여주기 위한 출력
