import numpy as np

print('Введие размер матрицы ')
n=int(input())
print(n)
m=int(input())
matrix=np.arange(m*n).reshape(n,m)
print('Введите матрицу ')
for i in range (0,n):
    for j in range(0,m):
        tmp=int(input())
        print(tmp)
        matrix[i][j]=tmp

sum=np.arange(m)
for j in range (0,m):
    tmpSum=0
    for i in range(0,n):
        tmpSum+=matrix[i][j]
    sum[j]=tmpSum

print(matrix)
print()
print(sum)
print()
for i in range(n-1):
    for j in range(m-i-1):
        if sum[j] > sum[j+1]:
            sum[j], sum[j+1] = sum[j+1], sum[j]
            for k in range(0, n):
                matrix[k][j], matrix[k][j+1] = matrix[k][j+1], matrix[k][j]


print(matrix)
print()
print(sum)