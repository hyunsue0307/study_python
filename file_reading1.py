# f=open('score.txt','r') # f변수 이름

# lines=f.readlines()
# a=[]
# print(lines) #> list 로 받음.
# for line in lines:
#     a.append(line.strip()) #strip = 좌우공백 없애기
# for i in a:
#     if int(i)>50:
#         print(i)
# f.close() #코드 닫는 습관


# # 암기
# f=open('score.txt','r') 
# lines=f.readlines()

# for line in lines:
#     print(line.strip())

# f.close() #코드 닫는 습관


# ### write
# f=open('20251020.txt','w')

# a=[100,20,30,80,40]
# for i in a:
#     if i > 50 :
#         f.write(str(i)+'\n') #write, 즉 쓸 떄는 문자(str)로 써야함.

# f.close()

f=open('star.txt','w') # r = 읽기, w = 쓰기, a = 추가

# for i in range(1,6):
#     if i %2 ==0:
#         f.write('*'*i + '\n')
        
#     else:
#         f.write( str(i)*i + '\n')
        
f.close() # 무조건 닫는 습관 기르자

# 파일 이름 동일 시덮어쓰기 돼버림.

# ## 예외처리 (시험에는 안나옴.)
# import os
# name= 'scor.txt'

# if os.path.exists(name):
#     f=open(name,'r') 
#     lines=f.readlines()

#     for line in lines:
#         print(line.strip())

#     f.close() #코드 닫는 습관



# readlines

# f = open('score.txt','r')

# lines= f.readlines() 

# for line in lines:
#     print(line.strip())

# f.close()

# # readline 쓰고 싶다면 : 문제에서 readline으로 고정돼있을 때

# f = open('score.txt','r')
# while True:
#     lines= f.readline() 
#     if lines=='': break
#     print(lines.strip())
    

# f.close()


# f = open('score.txt','r')

# lines= f.readlines() 
# sum=0
# for line in lines:
#     sum+=line.
#     print(line.strip())

# f.close()


# f = open('score.txt','r')

# lines= f.readlines() 
# sum=0
# cnt=0
# for line in lines:
#     sum+=int(line.strip())
#     cnt+=1
# print(sum/cnt)

# f.close()

# f=open('phone.txt','w')
# x = 'phone number'
# y = '010 - 4811 - 3959'
# f.write(x+'\n')
# f.write(y)

# f.close()

# f = open('yyy.txt','a')
# for i in range(50):
#     f.write('%d 번째 메롱.\n'%(i))
# f.close()


# 파일 닫기를 신경쓰고 싶지 않을 때.

# with open('score.txt','r') as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line.strip())


# f = open('score.txt','r')
# lines= f.readlines() 
# for line in lines:
#     print(line.strip())
# f.close()

#1
# f=open('input.txt','r')

# lines=f.readlines()
# cnt=0
# for line in lines:
#     cnt+=1
# print('%d 줄'%cnt)

# f.close()

#2
f=open('input2.txt','r')
lines=f.readlines()
cnt=0
target='python'
for line in lines:
    if line.strip() == target: #line은 \n을 포함. 따라서 비교가 안됨.
        cnt+=1
print(cnt)
f.close()

#3
# with open('input2.txt','r') as f :
#     lines=f.readlines()
# with open('output.txt','w') as g:
#     cnt=0
#     for line in lines:
#         result=('%d : %s' %(cnt,line)) + '\n'
#         # line 은 문자열임. 정수 아님. ,write 할 때 \n(한 줄 띔.)
#         g.write(result)
#         cnt+=1

# #4
# with open('star1.txt','w') as f:
#     for i in range(1,6):
#         if i%2==1:
#             f.write(('*'*i)+'\n')
#         else:
#             f.write((str(i)*i) +'\n')

# #5
# capital = {"대한민국": "서울", "미국": "워싱턴", "프랑스": "파리", "영국":"런던", "스위스":"베른", "베트남":"하노이","덴마크":"코펜하겐"}
# with open('capital.txt','w') as f:
#     for i in capital:
#         if len(i) == 3:
#             result=('%s 의 수도는 %s 입니다.'%(i,capital[i]) +'\n') #capital[i] < 딕셔너리의 value 값
#             f.write(result)

#6☆
# f=open('score.txt','r')
# sum=0
# average=0.0
# cnt=0
# while True:
#     line=f.readline()
#     sum+=int(line.strip())
#     cnt+=1
#     if line=='':break #순서가 이러면 빈 줄을 int()로 바꾸려해 문제가 발생함.
# average=(sum/cnt)
# f.close()


f=open('score.txt','r')
sum=0
average=0.0
cnt=0
while True:
    line=f.readline()
    if line=='':break
    sum+=int(line.strip())
    cnt+=1 
average=(sum/cnt)
print(average)
f.close()

with open('score.txt','r') as f:
    lines=f.readlines()
    sum=0
    average=0.0
    cnt=0
    for line in lines:
        sum+=int(line.strip()) ###strip 너무 중요.
        cnt+=1
average=(sum/cnt) #한 번만 계산하면 됨. 그러니 밖으로
print(average)

#7
with open('name.txt','r') as f:
    res=[]
    lines=f.readlines()
    for line in lines:
        parts=line.strip().split() #리스트임.
        if len(parts)>=2:#재료가 2개 이상.(문자열이니까 '')
            name=parts[1]
            if len(name)==4:
                res.append(name)
print(res)


f= open('name.txt','r')
lines=f.readlines()
res=[]
for line in lines:
    parts=line.strip().split()
    if len(parts)>=2:
        name=parts[1]
        if len(name)==4:
            res.append(name)
print(res)
f.close()

#8
with open('midterm.txt','r') as f:
    lines=f.readlines()
    # header=lines[0].strip().split(',') #첫 줄 과목 이름 추출
    # Korean_index=header.index('Korean') #'Korean' 이 몇번째 열인지 찾기
    total=0
    average=0.0
    cnt=0
    for line in lines[1:]:
        parts=line.strip().split(',')
        if len(parts)>0: # 파일에 빈 줄이 있을 수 있음.미리 방지.
            total+=int(parts[0])
            cnt+=1
average=(total/cnt) if cnt >0 else 0
print(average)

