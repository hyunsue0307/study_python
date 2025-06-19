# password= 'data'
# answer = input('비밀번호:')
# if password == answer :
#     print('correct')

# num =int(input('number:')) # input => str 받음.
# if num % 2==0:
#     print('짝수')
# else:
#     print('홀수')

# math = 83
# science = 90

# if math >80 and science >=90:
#     print('True') 
# # 비교연산자는 결과값이 아니라 비교에서 bool 형이 나옴.

# num = int(input('number'))
# if num % 5 == 0 and num % 7 == 0:
#     print('multiple of 35')
# else:
#     print('Not a multiple of 35')

# > pass 가 아무 일도 하지 않음.
#정답
# num = int(input('number'))
# if num%2==0 :
#     print('It is an even number.')
# else :
#     pass

# num=int(input('Enter a number:'))
# if num > 0 :
#     print('It is a positive number.')
# else:
#     print('It is not a positive number.')


# num=int(input('Enter a number:'))
# if num ==0 :
#     print('Zero')
# elif num %2==0:
#     print('Even number')
# else:
#     print('Odd number')

# num=int(input('Enter a number:'))
# if num >=90 :
#     print('A')
# elif num >=80:
#     print('B')
# elif num >=70:
#     print('C')
# elif num >=60:
#     print('D')
# elif num >=0:
#     print('F')
# else:
#     print('Invalid score')



# year=int(input('Enter a year:'))
# month = int(input('Enter a month:'))

# day=30
# def get_days(x,y):
#     if y == 2 :
#         if (x %4==0 and x %100 !=0) or x %400 ==0 :        
#             return 29
#         else:
#             return 28
#     elif y in [1,3,5,7,8,10,12] :
#         return 31
#     elif y in [4,6,9,11] :
#         return 30
#     else :
#         return None
    
# day = get_days(year,month)

# if day is None:
#     print('Invalid month')
# else :
#     print('Month %d in %d has %d days.'% (year,month,day))

# # 내 코드
# num= int(input('Enter a number:'))

# def output_even(x):
#     for i in range(0,x+1) :
#         if i % 2==0:
#             print(i)
#             if i == 8:
#                 break
       
        
# hop=output_even(num)

# #답 추천
# num= int(input('Enter a number:'))

# def output_even(x):
#     for i in range(0,x+1) :
#         if i==10:
#             break
#         if i %2 != 0 :
#             continue
#         print(i)
            
# output_even(num)

#2nd

# def num_(x):
#     i=0
#     over_10_count=0
#     while True:
#         i+=1
#         if i%3==0:
#             continue
#         if i >=10:
#             over_10_count+=1
#             if over_10_count == 3:
#                 print('Too much numbers >= 10')
#                 break
#         if x < i :
#             break
        
#         print(i)

# num= int(input('Enter a number:'))
# num_(num)


# nums=[3, 10, 15, 22, 45, 48, 51, 60, 30, 55, 2, 9]
# def print_special_numbers(nums, limit):
#     cnt=0
#     for i in nums:
#         if i % 5==0:
#             continue #continue를 만나면 그 아래 코드(cnt += 1)는 절대 실행 안됨.
#         if i >50 :
#             break
#         print(i)
#         cnt+=1
#         if cnt == limit :
#             break
# print_special_numbers(nums,5)


# nums=[3, 10, 15, 22, 45, 48, 51, 60, 30, 55, 2, 9]
# def print_special_numbers(nums, limit):
#     result=[]
#     for i in nums:
#         if i % 5==0:
#             continue #continue를 만나면 그 아래 코드(cnt += 1)는 절대 실행 안됨.
#         if i >50 :
#             break #break 은 강제 종료
#         result.append(i)
#         if len(result) == limit :
#             break
#     print(result)
# print_special_numbers(nums,5)

# nums=[3, 10, 15, 22, 45, 48, 51, 60, 30, 55, 2, 9]
# def print_special_numbers(nums, limit):
#     result=[]
#     for i in nums  :
#         if i % 5==0 or i >50:
#             continue #continue를 만나면 그 아래 코드(cnt += 1)는 절대 실행 안됨.
#                     #break 은 강제 종료이므로 같이 continue 문 안에
#         result.append(i)
#         if len(result) == limit :
#             break
#     print(result)
# print_special_numbers(nums,5)

# students = [
#     {'name': 'Alice', 'score': 85},
#     {'name': 'Bob', 'score': 59},
#     {'name': 'Charlie', 'score': 77},
#     {'name': 'David', 'score': 90},
#     {'name': 'Eve', 'score': 45},
#     {'name': 'Frank', 'score': 66},
#     {'name': 'Grace', 'score': 49},
#     {'name': 'Helen', 'score': 70}
# ]
# result=[]
# for i in students:
#     if i['score']> 60:
#             result.append((i['name'],i['score'])) #묶어줘야 하나로 들어감.

# print(result)


# students = [
#     {'name': 'Alice', 'score': 85, 'attended': True},
#     {'name': 'Bob', 'score': 59, 'attended': True},
#     {'name': 'Charlie', 'score': 77, 'attended': False},
#     {'name': 'David', 'score': 90, 'attended': True},
#     {'name': 'Eve', 'score': 45, 'attended': True},
#     {'name': 'Frank', 'score': 66, 'attended': True},
#     {'name': 'Grace', 'score': 49, 'attended': False},
#     {'name': 'Helen', 'score': 70, 'attended': True}
# ]
# passed=[]
# for i in students:
#       if i['attended'] == True and i['score']>=60:
#             passed.append((i['name'],i['score']))
# print(passed)

# students = [
#     {'name': 'Alice', 'attended': True, 'late': False, 'score': 85},
#     {'name': 'Bob', 'attended': True, 'late': True, 'score': 82},
#     {'name': 'Charlie', 'attended': False, 'late': False, 'score': 88},
#     {'name': 'David', 'attended': True, 'late': False, 'score': 65},
#     {'name': 'Eve', 'attended': True, 'late': False, 'score': 90},
#     {'name': 'Frank', 'attended': True, 'late': False, 'score': 72},
#     {'name': 'Grace', 'attended': True, 'late': True, 'score': 95},
# ]

#올바르지 않은 코드
# result=[]
# for i in students:
#     if i['attended'] == True and i['late']==False and i['score']>=70:
#         result.append((i['name'],i['score']))
# print(result.sort())
###

#list.sort() > 제자리 정렬, 내부 순서는 바뀌지만 반환 되는 것은 없음. > 따라서 print(list.sort()) 값 반환 안함.

# 1 방법
#ressult.sort()
#print(result) < 재정렬된 result 를 출력함. 원본 변경 o

# 2 방법
#print(sorted(result)) < sorted : 재정렬 출력. 원본 변경 x

# nums = [3, 1, 2]

# a = nums.sort()
# print(a)       # None
# print(nums)    # [1, 2, 3]



# #올바른 코드
# result=[]
# for i in students:
#     if i['attended'] == True and i['late']==False and i['score']>=70:
#         result.append((i['name'],i['score']))
# print(sorted(result))

#나의 답안
# students = [
#     {'name': 'Alice', 'attended': True, 'late': False, 'score': 85},
#     {'name': 'Bob', 'attended': True, 'late': True, 'score': 82},
#     {'name': 'Charlie', 'attended': False, 'late': False, 'score': 88},
#     {'name': 'David', 'attended': True, 'late': False, 'score': 65},
#     {'name': 'Eve', 'attended': True, 'late': False, 'score': 90},
#     {'name': 'Frank', 'attended': True, 'late': False, 'score': 72},
#     {'name': 'Grace', 'attended': True, 'late': True, 'score': 95},
# ]
# result=[]
# for i in students:
#     if i['attended'] == False:
#         continue
#     if i['late'] == True :
#         res = i['score'] - 5
#     else:
#         res=i['score']
#     if res >= 70 :
#         result.append((i['name'],res))
# result.sort(reverse=True)
# print(result) # list 니까

# # '어떤' 기준으로 정렬할 때,

# result = [  ('Eve', 90),
#     ('Frank', 72),
#     ('Bob', 82) ]
# result.sort(key=lambda x:x[1],reverse=True)


students = [
    {'name': 'Alice', 'attended': True, 'late': False, 'score': 85, 'homework_submitted': True},
    {'name': 'Bob', 'attended': True, 'late': True, 'score': 87, 'homework_submitted': False},
    {'name': 'Charlie', 'attended': False, 'late': False, 'score': 90, 'homework_submitted': True},
    {'name': 'David', 'attended': True, 'late': False, 'score': 78, 'homework_submitted': False},
    {'name': 'Eve', 'attended': True, 'late': True, 'score': 84, 'homework_submitted': True},
    {'name': 'Frank', 'attended': True, 'late': False, 'score': 81, 'homework_submitted': True},
    {'name': 'Grace', 'attended': True, 'late': True, 'score': 92, 'homework_submitted': True},
]
result=[]
for i in students:
    if i['attended'] == False:
        continue
    res = i['score']
    if i['late'] == True:
        res-=5
        if res < 0 :
            res=0
    if i['homework_submitted'] == False:
        res-=10 # res 덮여씌어짐.
        if res < 0 :
            res=0
    if res >= 60:
        result.append((i['name'],res,'pass'))
    else:
        result.append((i['name'],res,'fail'))

result.sort(key=lambda x:x[1],reverse=True)
print(result)

