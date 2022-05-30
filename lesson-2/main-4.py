def Creteria(str1, str2):
    minLength = min(len(str1),len(str2))
    for i in range(minLength):
        if str1[i] > str2[i]:
            return True
        if str1[i] < str2[i]:
            return False
    if len(str1) == len(str2):
        return True
    str = str1 if minLength != len(str1) else str2
    if str[minLength - 1] < str[minLength]:
        return minLength != len(str1)
    else:
        return minLength == len(str1)


def sort(arr, f):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if f(arr[j], arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Введите количесво значений массива")
n = int(input())
arr=[]
for i in range(n):
    str=input()
    arr.append(str)
sort(arr, Creteria)
arr.reverse()
str = ""
for i in arr:
    str+=i
print(str)

