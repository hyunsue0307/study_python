
##### 1번 문제 #####😅😅😅😅😅

# num = 3/813  #str 아니고 float 임.
# res = 0
# for i in str(num):
#     if i.isdigit():
#         res+=int(i)
# print(res)

# num=4/109
# res=0
# for i in str(num):
#     if i.isdigit():
#         res+=int(i)


# print(res)
# for i in str(num):
#     if i.isdigit():
#         res+=int(i)
# print(res)
# part=str(num).split('.')[1] #split는 문자열에서만 가능한 메서드


# result=res[:,1] #1차원인데 왜 2차원 인덱싱을 사용해..


# ##### 2번 문제 #####

# name = ['hello','trip','pho','airplane','zebra']

# for i in name:
#     print('len',len(i))
# for i in name:
#     print('%s의 길이는 %d'%(i,len(i)))



# ##### 3번 문제 #####

# def draw_star(n):
#     i=1
#     while i<=n:
#         star='*'*(2*i-1)
#         space=' '*(n-i)
#         space_star=space+star
#         i+=1
#         print(space_star)
    




#     while i <= n:
#         star='*'*(2*i-1)
#         no_star=' '*(n-i)
#         result=no_star+star
#         i+=1
# #         print(result)
# draw_star(3) ## 결과 확인용
# draw_star(4) ## 결과 확인용


# ##### 4번 문제 #####😅

# student = {"Alice": 88, "Julia":68, "Bob": 95, "Tony": 97,  "David": 90}
# max_score=0
# max_name=''
# for i in student:
#     if student[i] > max_score:
#         max_score=student[i]
#         max_name=i
# print(max_name)
# print(max_score)
# max_score=0
# max_name=''

# for k,v in student.items():
#     if v>max_score: #k=str , max_score = int
#         max_score=v #> 오른쪽 값을 왼쪽에 저장! 이라고 생각하면 됨.
#         max_name=k




#         # k=max_score #이렇게 쓰면 안됨,,, 변수와 치환의 방향이 반대임.
#         # v=max_name


# print(max_name, max_score)
         


#### 5번 문제 #####
def count_space(a):
    cnt=0
    for i in a:
        if i == ' ':
            cnt+=1
    return cnt



  
sentence = 'Python is powerful and interesting for me.'
num = count_space(sentence)
print(sentence)
print('빈칸의 개수 : ', num)
  
    # cnt=0
    # for i in a:
    #     if i == ' ':
    #         cnt+=1
    # return cnt 



# # or
def count_space(a):
    cnt=a.count(' ')
    return cnt 

sentence = 'Python is powerful and interesting for me.'
num = count_space(sentence)
print(sentence)
print('빈칸의 개수 : ', num)


##### 6번 문제 #####

scores = [91,74,82,98,56,49,26,87,93,55]
high=[]
for i in scores:
    if i >=80:
        high.append(i)


print(high)




# ##### 7번 문제 #####😅

def extract_even_index_letters(x):
    b=[]
    for i in x:
        b.append(i[0])
    return b
        

input_data = ["apple", "blue", "captain", "dry"]
result = extract_even_index_letters(input_data)
print(result)




    # b=[]
    # for i in x:
    #     res=i[0]
    #     b.append(res)
    # return b #return 은 함수 실행을 즉시 종료시킨다.

# ##### 8번 문제 #####😅

sentence = "Python is fun but sometimes annoying and slow"
banned_words = ["annoying", "slow"]

a='***'
re=sentence.split()
b=[]
for i in re:
    if i in banned_words:
        b.append(a)
    else:
        b.append(i)

result=' '.join(b)
print(result)
# re=sentence.split()
# a='***'
# b=[]
# for i in re:
#     if i in banned_words:
#         b.append(a)
#     else:
#         b.append(i)
# res=' '.join(b)

        
# #or
# sentence = "Python is fun but sometimes annoying and slow"
# banned_words = ["annoying", "slow"]

# replace_='***'
# for word in banned_words:
#     sentence=sentence.replace(word,replace_)
# print(sentence)
# ### coding here ###




# ##### 9번 문제 #####😅
##while문 안에서 업데이트가 없어서 num 값이 바뀌지 않아.
answer = 25

num = int(input('0부터 50사이 숫자 입력:'))
## coding here ###
i=0

while True:
    i+=1
    if num > 25:
        print('up')
    elif num<25:
        print('down')
    else:
        print('correct')
        break
    num = int(input('0부터 50사이 숫자 입력:'))
    
#continue 쓰면 그 반복문으로 돌아가는 거임.