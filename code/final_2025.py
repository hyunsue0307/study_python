#문제 1
# with open('result.txt' , 'w') as f:
#     for i in range(5):
#         name=input('이름을 입력하세요:')
#         score=int(input('점수를 입력하세요:'))
#         if score >=60:
#             result=('%s : %d - pass'%(name,score))
#         else:
#             result=('%s : %d - fail'%(name,score))

#         f.write(result + '\n') # 문자열로 반복해야함. (하나만 받을 수 있음. '\n')


#2번


# class Student:
#     def __init__(self,name,score):
#         self.name=name
#         self.score=score

#     def is_pass(self):
#         return self.score >= 60
    
# with open('scores.txt','w') as f:
#     for i in range(5):
#         name= input('이름')
#         score=input('점수')
#         result=(name,score)

#         f.write(name + ' ' + score +'\n')

# with open('scores.txt','r') as g, open('result.txt','w') as f:
#     lines=g.readlines()
#     for line in lines:
#         name, score = line.strip().split()
#         line=line.strip()##########
#         if int(score) >= 60 :
#             result=(line + '- pass')
#         else:
#             result=(line + '- fail')
#         f.write(result + '\n')




############### 문제 1
# with open('student.txt','w') as f :
#     for i in range(3):
#         name=input('name')
#         score=input('score')
#         f.write(name +' ' + score + '\n') # 줄 건너뛰기 해주기

# ############# 문제 2
# with open ('student.txt','r') as g:
#     lines=g.readlines() #list 로 반환. 따라서 lines 에 strip 못 씀.
#     for line in lines:
#         if line.strip()==' ':
#             continue
#         parts=line.strip().split()
#         if int(parts[1]) >= 70:
#             result=parts[0] + '- 합격'
#         else:
#             result=parts[0]+'- 불합격'
#         print(result)
############ 문제 3
# with open('student.txt','r') as h,open('result.txt','w') as k:
#     lines=h.readlines()
#     for line in lines:
#         name, score = line.strip().split() # list에서 나온건 str
#         if int(score) >= 70:
#             result=f"{name} {score} - 합격\n"
#         else:
#             result=f"{name} {score} - 불합격\n"
#         k.write(result)

# #
# with open('scores1.txt','r') as f ,open('pass.txt','w') as h:
#     lines=f.readlines() #< ( ) 써야됨.
#     for line in lines:
#         parts=line.strip().split()
#         if int(parts[1]) >=60:
#             result=f"{parts[0]} : {parts[1]}"
#             h.write(result +'\n') # 무언갈 쓸 때는 줄바꿈.
#         else:
#             pass

# #
# new=[]
# students = ['홍길동-85', '김철수-45', '이영희-72', '박민수-90']
# for i in students:
#     re=i.split('-') # 문자열에서만 쓰임. 따라서 student 를 문자열로 바꿔.
#     if int(re[1]) >= 70:
#         new.append(re[0])

# # print(new.sort())#< 제자리 정렬만 함.
# new.sort()
# print(new)
# # or
# print(sorted(new))


# ######틀린 예시!!!!!!
# result=new.sort()
# print(result) 

# #
# with open('student.txt','r') as f,open('result.txt','w') as h:
#     lines=f.readlines()
#     for line in lines:
#         name,score=line.strip().split()
#         if int(score)>=70:
#             result=f"{name} {score} -합격\n"
#             h.write(result) # if 안에다가 넣으면 elsd 안써도 됨.

#
# class Student:
#     def __init__(self,name,score):
#         self.name=name
#         ####### 매우 중요 !!!!!!!
#         self.score=int(score) # 문자열로 들어오니까 여기서 int로 변환
#     def is_passed(self):
#         return self.score>=70 #true False 반영함.

# with open('student.txt','r') as f,open('result.txt','w') as h:
#     lines=f.readlines()
#     for line in lines:
#         name,score=line.strip().split()
#         student = Student(name,score)
#         if student.is_passed():
#             result=f"{name} {score} -합격\n"
#             h.write(result)

# class Student:
#     def __init__(self,name,score): #매개변수,,,,,
#         self.name=name
#         self.score=int(score)
#     def is_passed(self):
#         return self.score>=70
    
# with open('student.txt','r') as f,open('pass.txt','w') as h,open('fail.txt','w') as k:
#     lines=f.readlines()
#     for line in lines:
#         name,score=line.strip().split()
#         student=Student(name,score)
#         if student.is_passed():
#             result=f"{name} {score} - 합격\n"
#             h.write(result)
#         else:
#             result=f"{name} {score} - 불합격\n"
#             k.write(result)

# 문제: 학생 목록이 담긴 student.txt 파일을 읽어서, 
# 각 학년별(1학년, 2학년) 평균 점수를 계산하시오.
# 그리고 평균 점수를 result.txt 파일에 기록하시오.

####### 모르겠음;
# 조건:
# - Student 클래스를 사용하세요.
# - 클래스에는 학년, 이름, 점수 정보를 포함하세요.
# class Student:
#     def __init__(self,x,y,z):
#         self.grade=int(x)
#         self.name=y
#         self.score=int(z)
#     def ave(self):
#         if self.grade == 1:

# b=[]
# with open('student.txt','r') as f, open('result.txt','w') as h:
#     lines=f.readlines()
#     for line in lines:
#         x,y,z=line.strip().split()
#         student=Student(x,y,z)
#         b.append(student)

# score_dict={}
# for student in b:
#     if student.grade not in score_dict:
#         score_dict[student.grade] = [] #value 값 모으기
#         score_dict[student.grade].append(student.score)

import numpy as np
b=[]
scores=[75,42,89,55,60,90,33,70]
arr=np.array(scores)

filtered=arr[(arr>=50)&(arr<80)]

average=filtered.mean()
print('')