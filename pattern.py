# Program 1

# N = int(input())
# for i in range(1,N):
#     for j in range(i-1,-1,-1):print(2**j,end = " ")
#     print(end="\n")


#Program 2

# c = 1
# cl = 2
# for i in range(5):
#     for j in range(1,cl):
#         print(c, end = " ")
#         c += 1
#     print("")
#     cl += 2



#program 3

# rows = 6
# for i in range(0, rows):
#     for j in range(0, i + 1):
#         print("*", end=' ')
#     print(" ")

# print(" ")

# for i in range(rows + 1, 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print(" ")




#Program 4

# import numpy as np
# def matrixTranspose_Numpy(ls):
#     ls = (np.array(ls)).T.tolist()
#     return ls


# print(matrixTranspose_Numpy([[1,2,3],[4,5,6]]))