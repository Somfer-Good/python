import numpy as np

print("Введите количесво значений первого массива")
n = int(input())
arr1 = np.arange(n)
for i in range(0, n):
    arr1[i] = int(input())
print("Введите количесво значений второго массива")
n = int(input())
arr2 = np.arange(n)
for i in range(0, n):
    arr2[i] = int(input())

arr1=np.sort(arr1)
arr2=np.sort(arr2)
for i in range(0, len(arr1)):
    for j in range(0, len(arr2)):
        if arr1[i] == arr2[j]:
            print(arr2[j],end=' ')
            arr2 = np.delete(arr2, j)
            break
