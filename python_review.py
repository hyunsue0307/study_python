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

def num_(x):
    i=0
    over_10_count=0
    while True:
        i+=1
        if i%3==0:
            continue
        if i >=10:
            over_10_count+=1
            if over_10_count == 3:
                print('Too much numbers >= 10')
                break
        if x < i :
            break
        
        print(i)

num= int(input('Enter a number:'))
num_(num)
