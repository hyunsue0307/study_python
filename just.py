# import final
# import numpy as np
# import pandas as pd

# from final import duhagi as dg


import numpy as np

a=[1,2,3]
b=[0,5,2]

c=np.array(a) # c 언어로 만들어진 numpy.array
d=np.array(b)

print(c+d)
print(c*d)
print(a[1])
print(c[2]) #numpy.array 속도가 더 빠름.


a = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]])
b=np.array([[4.,19,8],[16,3,5]])
c=np.array([1,2,3])
d=np.array([1,2,5.2,3], dtype=float)
print(d)
# 방법 2개
e=[1,2,3]

f=np.array(e)
print(e)


print(a.shape) #(3,3,3) (겹,3행,3열)
print(b.shape) #(2,3) (2행 3열)
print(c.shape) #(3,) (1차원,옆으로 3)

print(a.size)# 몇개 인가
print(c.size)
print(c.ndim) #ndim > 몇차원인가
print(b.dtype)#
print(b)#소수점 붙이면 다 점이 붙음.
print(type(c))

print(b[0,1])
print(b[ : , 1]) #1이 두번 째
print(b[ 1 , :])





####################
import numpy as np
a= [1,2,3,4]
b=[10,20,30,40]

arr1=np.array(a) 
arr2=np.array(b) 

print(a+b) # [1, 2, 3, 4, 10, 20, 30, 40]
print(arr1+arr2) #[11 22 33 44]
print(arr1-arr2) #[ -9 -18 -27 -36]
print(arr1*arr2) #[ 10  40  90 160]
print(arr1/arr2) #[0.1 0.1 0.1 0.1]


######## 시험 문제 (True Falss & np.array 자유자재)

a=[9,2,3,2,5,10,6]
b=np.array(a)
print(a ==2 )#list 랑 숫자? ㅋ
print(b==2) #각 원소에게 질문
print(sum(b==2))
print(sum(b>4))

print(b[ b>4]) # 해당하는 원소값이 나옴.

########
a=[[1,2,3,4],[5,6,7,8]]
arr2= np.array(a) #똑같이 생김.
print(arr2)
arr3=np.array([[0,1,2],[3,4,5]])

a=[[1,2,3],[4,5,6]]
b=np.array(a)


print(b.shape[0])#<행
print(b.shape[1])#<열
print(a[0])

arr=np.array([0,1,2,3,4])
print(arr[2])
print(arr[-1])
print(arr[1]*arr[3])

arr=np.array([[0,1,2,3],[4,5,6,7]])
print(arr[0,:]) #[0,1,2,3]
print(arr[:,1]) #[1,5]
print(arr[1,1:]) #[5,6,7]
print(arr[:2,:2]) #[0,1
#2 전까지니까 1까지     4,5]



a=np.zeros((3,4))
print(a)
a=np.full((3,4),5)
print(a)

a=np.empty((3,4)) #쓰레기값 넣어라. #시험에 안나옴.
print(a)


a=np.arange(40) #간격을 만들어서 0부터 39까지
b=np.arange(1,41)
print(a)
print(b)


######## reshape 중요
arr3=np.array([[0,1,2],[3,4,5]])
b=arr3.reshape(3,2) #reshape 
c=arr3.reshape(1,6)

d=arr3.flatten() #1차원 만들기
e=arr3.reshape(-1,)

print(b.shape)
print(b)
print(c)

#ex
a=np.zeros(12)
b=a.reshape(4,3)
print(b)
print(a)


## 붙이고 싶을 때 concatenate
import numpy as np
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
array3 = np.concatenate([array1,array2])
print(array3)

print(np.hstack((array1,array2))) # 좌우
print(np.vstack((array1,array2))) #수직 +1 ndim 


## 42 page
a=[2,5,1,17,21]
b=np.array(a)
result=b+1
print(result)

##
import numpy as np

a = np.array([1,3,5,7,8,11])
b=a.reshape(2,3)

print(b)

## 47page
Python = np.array([90, 92, 37])
R = np.array([ 85, 88, 91])
Math = np.array([94, 91, 84])
s_python = np.sum(Python)
s_r = np.sum(R)
s_math = np.sum(Math)
m_python = np.mean(Python)
m_r = np.mean(R)
m_math = np.mean(Math)

x = np.argmax([m_python,m_r,m_math])
print(x)


###########
import numpy as np
import random
sales = [86623, 33030, 38117]
######################## 중요!!!
n_sales = np.array(sales) # np array
filter =n_sales<40000 # true 인지 False 인지
bad_sales = n_sales[filter] # 값을 알고싶다!
# = 
bad_sales = n_sales[n_sales<40000]
#########################
print(bad_sales)