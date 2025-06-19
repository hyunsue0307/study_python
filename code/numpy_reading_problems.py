# #문제 1 😅😅
# bad=['annoying','slow']
# re='***'
# with open('data.txt','r') as f,open('clean_data.txt','w') as h:
#     lines=f.readlines() #list 로 반환.
#     for line in lines:
#         line=line.strip().split()
#         new1=[]
#         for word in line:
#             if word in bad:
#                 new1.append(re)
#             else:
#                 new1.append(word)
#         result=' '.join(new1)+'\n'
#         h.write(result) # write 는 문자열만 받음.

# #문제 2 
# import numpy as np
# store=[]
# max_score=0
# max_name=''

# students = {
#     "Alice": 88,
#     "Bob": 75,
#     "Charlie": 95,
#     "David": 62,
#     "Eva": 79,
#     "Frank": 54
# }

# for k,v in students.items():
#     if v>=80:
#         store.append(v)
#     if v<60:
#         print(f'{k} fail')
#     if v>max_score:
#         max_score=v
#         max_name=k

# print(max_name,max_score)

# avg=np.mean(store)
# print(avg)

# #문제 3
# # import numpy as np
# # arr=np.array([1,2,3,4])
# # total = np.sum(arr)
# # odd_arr=arr[arr%2==1]
# # odd_arr=np.sum(odd_arr)
# # print(arr)
# # print(odd_arr)
# # print(total)


# num=4/109
# s=str(num) # '0.03669724770642202...' 이런 식
# parts=s.split('.')
# print(parts)
# x=[]
# for i in parts[1]:
#     x.append(int(i)) ###매우 중요 i 는 지금 str 로 들어가고 있어.

# arr=np.array(x)
# total=np.sum(arr) # 내가 넣은 리스트 > ['1','2','53','3'] > 문자열 합산 불가.
# print(total)

# #문제 4
# i=1

# while True:
#     num=input('enter a number')

#     if not num.isdigit():
#         num=input('숫자를 입력해라')
#         continue

#     num=int(num)

#     if int(num)>23:
#         print('down')
#     elif int(num) <23:
#         print('up')
#     else:
#         print('correct')
#         break
#     i+=1


# #문제 5
# x=[]
# words = ["apple", "banana", "cherry", "date", "egg"]
# for i in words:
#     if len(i)%2==0:
#         res=i.upper()
#         x.append(res)
# print(x)


#문제 1

# class Student:
#     def __init__(self,name,score):
#         self.name=name
#         self.score=score

#     def avg_(self):
#         return 

# students = [
#     Student("Alice", 88),
#     Student("Bob", 73),
#     Student("Charlie", 91),
#     Student("David", 62),
#     Student("Eva", 95)
# ]

# # 여기에 NumPy를 사용하여 평균 점수 계산
# import numpy as np
# for student in students:
#     print(student)



# ✅ 복합문제: 클래스 + 딕셔너리 + 메서드 + NumPy

# 다음 조건을 만족하는 프로그램을 작성하시오.

# [요구 사항]
# 1. 학생 정보를 저장하는 `Student` 클래스를 정의하시오.
#    - 생성자에서는 이름을 받고, 점수를 저장할 빈 딕셔너리를 초기화.
#    - `add_score(과목, 점수)` 메서드로 점수를 추가할 수 있음.
#    - `get_average()` 메서드는 NumPy를 사용하여 평균 점수를 반환.
#    - `print_scores()` 메서드는 모든 과목 점수와 평균을 출력함.
# 2. 학생 1명을 생성하고, 다음과 같은 점수를 추가하시오:
#    - 수학: 92, 영어: 88, 과학: 79
# 3. 모든 점수를 NumPy 배열로 출력하고, 평균과 홀수 점수만 출력하시오.

# 예시 출력:
# 과목별 점수:
# 수학 92
# 영어 88
# 과학 79
# 평균: 86.33
# NumPy 배열: [92 88 79]
# 홀수 점수만: [79]
# import numpy as np

# class Student:
#     def __init__(self,name):
#         self.name=name
#         self.scores={}

#     def add_score(self,score,subject):
#         self.scores[subject]=score
#         #student1.add_score('math',99)
        
#     def get_average(self):
#         score_array=np.array(list(self.scores.values()))
#         return np.mean(score_array)
    
#     def print_scores(self):
#         print(f'{self.name}의 과목별 점수:')
#         for subject,score in self.scores.items():
#             print(subject,score)
#         print('avg: %.2f'%self.get_average())


# student1=Student("현유")
# student1.add_score(92,'수학')
# student1.add_score(88,'영어')
# student1.add_score(79,'과학')

# student1.print_scores()



#step 1
# import numpy as np
# class Student:
#     def __init__(self,name):
#         self.name=name
        
#     def introduce(self):
#         return print(f"안녕하세요, 제 이름은 {self.name}입니다.")

# student=Student('hyunyoo')
# student.introduce() #메서드

# #step 2
# class Student:
#     def __init__(self,name):
#         self.name=name
#         self.scores={}
#     def add_score(self,subject,score):
#         self.scores[subject]=score
#     def print_scores(self):
#         print(f"{self.name}의 과목별 점수")
#         for subject,score in self.scores.items():
#             print(f'{subject} : {score}')
#     def get_average(self):
#         arr=np.array(list(self.scores.values()))
#         return np.mean(arr)

# student = Student('현유')
# student.add_score('수학',99)
# student.add_score('영어',98)
# student.print_scores()
# print('평균', student.get_average())


# import numpy as np

# class Student:
#     def __init__(self,name):
#         self.name=name
#         self.scores={}
        
#     def add_score(self,subject,score):
#         self.scores[subject]=score

#     def get_average(self):
#         arr=np.array(list(self.scores.values()))
#         return (np.mean(arr))

#     def print_scores(self):
#         for subject,score in self.scores.items():
#             print(f"{subject} {score}")

# student1=Student('현유')
# student1.add_score('수학',90)
# student1.add_score('영어',80)
# student1.add_score('과학',70)
# res= student1.get_average()
# student1.print_scores()
# print('평균:',res)

####
import numpy as np

# a=[1,2,3]
# b=[0,5,2]

# arr_a=np.array(a)
# arr_b=np.array(b)
# print(arr_a+arr_b)
# print(arr_a*arr_b)

# import numpy as np

# arr = np.array([
#     [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
#     [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
#     [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# ])

# # arr 배열의 차원 수(ndim), 모양(shape), 총 원소 개수(size)를 각각 출력하세요.
# print(arr.shape) # 3,3,3
# print(arr.size)  #27개
# print(arr.ndim) #3차원


# import numpy as np

# matrix = np.array([[4., 19, 8], [16, 3, 5]])
# print(matrix[0,1])
# print(matrix[:,1])
# print(matrix[1,:])
# matrix에서 첫 번째 행 두 번째 열 원소를 출력하세요.
# matrix에서 두 번째 열 전체를 출력하세요.
# matrix에서 두 번째 행 전체를 출력하세요.

# import numpy as np

# data = np.array([9, 2, 3, 2, 5, 10, 6])
# print(data==2) #false, true
# print(sum(data==2)) #원소 개수
# print(data[data>4]) #data[data<2000] => 해당 값

# data 배열에서 값이 2인 원소 개수를 출력하세요.
# data 배열에서 값이 4보다 큰 원소들만 추출하여 출력하세요.

# import numpy as np

# arr = np.array([[0, 1, 2], [3, 4, 5]])

# # arr를 3행 2열로 모양을 바꾼 배열을 출력하세요.
# # arr를 1차원 배열로 평탄화(flatten)하여 출력하세요.
# nw_arr=arr.flatten()
# print(nw_arr)
# print(arr.reshape(3,2))

# import numpy as np

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])

# # arr1과 arr2를 이어 붙여 1차원 배열로 출력하세요.
# # arr1과 arr2를 좌우로 붙여 출력하세요.
# # arr1과 arr2를 위아래로 붙여 출력하세요.
# renew=np.concatenate([arr2,arr1]) #######
# print(renew)

# print(np.hstack((arr1,arr1)))
# print(np.vstack((arr1,arr2)))


# import numpy as np

# sales = [86623, 33030, 38117]
# arr_sales=np.array(sales)
# print(arr_sales[arr_sales<40000])

# sales 리스트를 numpy 배열로 변환 후, 4만 미만의 값들만 출력하세요.


# import numpy as np

# arr = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])

# # 첫 번째 행의 합을 출력하세요.
# # 두 번째 열의 합을 출력하세요.
# # 전체 원소의 합을 출력하세요.

# arr1=arr[0,:]
# print(np.sum(arr1))
# arr2=arr[:,1]
# print(np.sum(arr2))
# print(np.sum(arr))

# bad=['annoying','slow']
# a="***"
# with open('data.txt','r') as f, open('clean_data.txt','w') as h:
#     lines=f.readlines()

#     for line in lines:
#         line=line.strip().split() #for 문으로 하나씩 끌고 와야 strip,split 쓸수있음.
#         new=[]
#         for word in line:
#             if word in bad:
#                 new.append(a)
#             else:
#                 new.append(word)
#         new_line=' '.join(new)
#         h.write(new_line +'\n')


f=open('chat_log.txt','r')
g=open('bad_words.txt','r')
h=open('clean_chat.txt','w')
lines=f.readlines()
lines1=g.readlines()
bad_word=[]
cnt=0
for line in lines1:
    words1=line.strip().split()
    for word in words1:
        bad_word.append(word)
for line in lines:
    words=line.strip().split()
    new=[]
    print(len(words))
    for word in words:
        if word in bad_word:
            new.append("___")
        else:
            new.append(word)
    new_line=" ".join(new)
    h.write(new_line + '\n')





f.close()
g.close()
h.close()