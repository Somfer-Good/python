import numpy as np

str = input()

arr = str.split(' ')
arrInt = np.arange(len(arr))
for i in range(0, len(arr)):
    arrInt[i] = int(arr[i])
arrInt.sort()
i=0
j=1
print(arrInt[i])
#while j!=len(arrInt) or arrInt[i]==arrInt[j]:


print(arrInt)
