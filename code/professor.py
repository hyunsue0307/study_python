# a=[1,2,3,4]

# print(1,2,3,sep='/')
# print('aaa',end=',')
# print(12)

# # # 3, 6, 9 게임

# # number=int(input('게임 최대 숫자를 입력해 주세요:'))
# # count=0
# # # str=[3,6,9] #이건 숫자임.
# # for i in range(1,number+1):
# #     str_i=str(i)
# #     for j in str_i:
# #         if j in ['3','6','9']:
# #             count+=1

# # print(count)



# # number=int(input('게임 최대 숫자를 입력해 주세요:'))
# # count=0
# # #91234
# # for i in range(1,number+1):
# #     for j in str(i):
# #         if j == '3' or j == '6' or j=='9':
# #             count+=1

# # print(count)

# #
# name=['hello','trip','pho','airplane','zebra']

# for i in name:
#     if len(i) == 3:
#         print(i)


# # for i in student:
# #     print(i,student[i])
# # for k,v in student.itmes():
# #     print(k,v)

# a='jds,fjlkj,jjjjaaa,aaa'
# b=[]
# d=a.split(',') #제자리 정렬임. 
# print(d)
# for i in d:
#     if i not in b:
#         b.append(i)


# c=','.join(b)
# print(c)


## 객체지향 >> 
# 1. 생성자 있는지 확인
# 2. 생성자 수에 맞게 만들기
# 3. self 빼먹지 말기
# 4. 호출 시 () 안에 뭐 넣지 않음.

## 함수
# 함수에서 return 있으면 a= 으로 밑에서 받아줘야 함.

#상속
# class Human:

# class Peaple(Human):


# import numpy as np
# arr=np.array([[12,45,78,34],
#               [56,89,23,67]])
# mean_vaule=np.mean(arr)
# print('평균: %.2f'%mean_vaule)

# greater_than_mean = arr[arr>mean_vaule] ##중요!!!!!
# print('평균보다 큰 값들:',greater_than_mean)


#예제1

# import numpy as np
# arr = np.array([[11, 25, 32, 19],
#                 [43, 8, 27, 50]])
# avg=np.mean(arr)
# result=arr[arr<avg]
# print(result)


# #예제2 
# arr = np.array([[21, 55, 30, 44],
#                 [60, 47, 10, 38]])
# max_arr=np.max(arr) #np.~()이면 괄호 안에 들어가야함.
# result=arr[arr==max_arr]
# print(arr[arr<result])

# #예제3
# arr = np.array([[12, 17, 28, 35],
#                 [44, 51, 62, 73]])
# result=arr[arr%2==0] ######
# print(result)

# #예제4
# arr = np.array([[5, 15, 25, 55],
#                 [60, 35, 45, 8]])
# result=arr[(arr>10)&(arr<50)] #and == &
# print(result)

#예제5
# import numpy as np

# arrays = [
#     np.array([[12, 45, 78, 34], [56, 89, 23, 67]]),
#     np.array([[21, 55, 30, 44], [60, 47, 10, 38]]),
#     np.array([[5, 15, 25, 55], [60, 35, 45, 8]])
# ]

# for i in arrays:
#     result=np.mean(i)
#     print(i[i>result])

# #예제6

# import numpy as np

# def filter_array(arr,condition='',threshold=0):
#     if condition=='up':
#         return arr[arr>threshold[1]]
#     elif condition=='down':
#         return arr[arr<threshold[0]]
#     elif condition=='between':
#         return arr[(arr>threshold[0])&(arr<threshold[1])]
#     else:
#         return arr

# arr = np.array([[11, 25, 32, 19],
#                 [43, 8, 27, 50]])

# result = filter_array(arr, condition='between', threshold=(10, 40))
# print("10보다 크고 40보다 작은 값들:", result)

# #예제 7
# import numpy as np
# with open('sample_data.txt','r') as f:
#     lines=f.readlines()
#     x=[]
#     for line in lines:
#         line=line.strip().split()
#         for j in line:
#             x.append(int(j))#### 중요!!!

# arr=np.array(x)
# avg=np.mean(arr)
# print('file:',arr)
# print('average:',avg)
# print('up avg:',arr[arr>avg])

# #예제 8
# import numpy as np
# with open('sample_data.txt','r') as f,open('filtered.txt','w') as h:
#     lines=f.readlines()
#     all_number=[]

#     for line in lines:
#         line=line.strip().split() #이거 안하면 '12 10 13' 이면 공백도 들어가서 오류뜸.
#         for i in line:
#             all_number.append(int(i))
#     arr_all_number=np.mean(all_number)

#     for line in lines:
#         line=line.strip().split()
#         new=[]
#         for i in line:
#             new.append(int(i))
#             avg=np.mean(new)
#         if avg>=arr_all_number:
#             res=' '.join(map(str,new)) # join 은 문자열 메서드
#             h.write(res+'\n')
#     print(avg)
    


# #예제9

# import numpy as np

# with open('sample_data.txt','r') as f:
#     lines=f.readlines()
#     all_number=[]
#     per_line_data=[]

#     for line in lines:
#         line=line.strip().split()
#         mid=[]
#         for j in line:
#             all_number.append(int(j))
#             mid.append(int(j))
#         per_line_data.append(mid) #2차원이더라도 ped_line 을 numpy 로 처리하니까 괜찮음.
        
#     all_avg=np.mean(all_number)

#     # per_line_data=np.array(per_line_data)
#     for row in per_line_data:
#         row_avg=np.mean(row)
#         if row_avg>=all_avg:
#             print('해당 줄 평균',row_avg)
#             print('해당 줄 데이터',row)

#     print(all_avg)
   




import numpy as np
with open('sample_data.txt','r') as f,open('filter_1.txt','w') as h:
    lines=f.readlines() # 하나의 리스트로
    all_avg=[]
    part=[]
    for line in lines:
        line=line.strip().split()
        row=[]
        for j in line:
            row.append(int(j))
            all_avg.append(int(j))
        part.append(row)
        
    arr_all_avg=np.mean(all_avg)
    print(arr_all_avg)

    for row in part:
        np_avg=np.mean(row)
        if np_avg>arr_all_avg:
            re=' '.join(str(x) for x in row)
            h.write(re+'\n')
        
