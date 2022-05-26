def isGreater(str1, str2):
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

def sort(list, f):
    for i in range(len(list) - 1):
        for j in range(len(list) - i - 1):
            if f(list[j], list[j + 1]):
                list[j], list[j + 1] = list[j + 1], list[j]

def maxNumberMadeConstructedList(list):
    sort(list, isGreater)
    list.reverse()
    str = ""
    for elm in list:
        str += elm
    return str


print("Введите количесво значений массива")
n = int(input())
arr=[]
for i in range(n):
    str=input()
    arr.append(str)
print(maxNumberMadeConstructedList(arr))
