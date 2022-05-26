import numpy as np

str = input()

arr = str.split(' ')
arrInt = np.arange(len(arr))
for i in range(0, len(arr)):
    arrInt[i] = int(arr[i])
arrInt=np.sort(arrInt)
i = 0
j = 1
flag=False
while j != len(arrInt):
    if arrInt[i] == arrInt[j]:
        flag=True
        arrInt = np.delete(arrInt, j)
    else:
        if flag:
            print(arrInt[i], end=' ')
        flag = False
        i = j
        j += 1
