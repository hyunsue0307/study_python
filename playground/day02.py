# orders = [{'menu':'아메리카노','time':'morning'},
#          {'menu':'아메리카노','time':'afernoon'},
#          {"menu": "라떼", "time": "afternoon"}, 
#          {"menu": "아메리카노", "time": "afternoon"}, 
#          {"menu": "카푸치노", "time": "morning"}, 
#          {"menu": "아메리카노", "time": "morning"}]

# menu_count={}

# for order in orders:
#     menu=order['menu']
#     if menu in menu_count:
#         menu_count[menu]+=1
#     else:
#         menu_count[menu]=1

# print('메뉴별 판매량:')
# for menu, count in menu_count.items():
#     print(menu,count)


# # 딕셔너리는 순서 개념이 없음. key에 해당하는 value 값을 꺼내라
# menu_count={}
# menu_count['아메리카노']=1
# print(menu_count)



# orders = [{'menu':'아메리카노','time':'morning'},
#          {'menu':'아메리카노','time':'afternoon'},
#          {"menu": "라떼", "time": "afternoon"}, 
#          {"menu": "아메리카노", "time": "afternoon"}, 
#          {"menu": "카푸치노", "time": "morning"}, 
#          {"menu": "아메리카노", "time": "morning"},
#          {"menu": "라떼", "time": "morning"}]

# menu_count1={}

# for order in orders:
#     menu=order['menu']
#     time=order['time']
#     if menu not in menu_count1:
#         menu_count1[menu] = {
#             'morning':0,
#             'afternoon':0
#             }
               
#     menu_count1[menu][time]+=1

# print(menu_count1)




orders = [{'menu':'아메리카노','time':'morning'},
         {'menu':'아메리카노','time':'afternoon'},
         {"menu": "라떼", "time": "afternoon"}, 
         {"menu": "아메리카노", "time": "afternoon"}, 
         {"menu": "카푸치노", "time": "morning"}, 
         {"menu": "아메리카노", "time": "morning"},
         {"menu": "라떼", "time": "morning"}]

menu_count={}

for order in orders:
    menu=order['menu']
    time=order['time']
    if menu not in menu_count:
        menu_count[menu]={
            'morning':0,
            'afternoon':0
        }
    menu_count[menu][time]+=1

for menu, times in menu_count.items():
    morning=times['morning']
    afternoon=times['afternoon']
    print(f'{menu}- 오전 :{morning}잔, 오후 :{afternoon}잔')

# 무엇으로 1차 분류할 것인가
# 2차로 무엇을 나눌 것인가


