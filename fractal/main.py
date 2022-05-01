import random
from os import system

import matplotlib.pyplot as plt

A = {
    1: [[0, 0.24], [0, 0.305]],
    2: [[0.72, 0.034], [-0.025, 0.742]],
    3: [[0.158, -0.128], [0.355, 0.367]],
    4: [[0.339, 0.369], [0.223, -0.076]]
}

b = {
    1: [0, 0],
    2: [0.206, 0.254],
    3: [0.138, 0.175],
    4: [0.68, 0.083]
}


def printA():
    for key, value in A.items():
        print(key, '.', value)


def printb():
    for key, value in b.items():
        print(key, '.', value)


def menu():
    print('1. Играть')
    print('2. Сохранить картинкой')
    print('3. Изменить параметры')
    print('4. Изменения масштаба')
    print('5. Выход')


def dopMenu():
    print('Изменение чего?')
    print('1. Матриц А')
    print('2. Векторов b')


def choice():
    print('Где меняем? :', end='')
    return int(input())


def game():
    for i in range(1, 10000):
        x = random.random() * 10000
        y = random.random() * 10000
        X.append(x)
        Y.append(y)
        p = random.random() * 100
        if p == 1:
            x = A[1][0][0] * x + A[1][0][1] * y + b[1][0]
            y = A[1][1][0] * x + A[1][1][1] * y + b[1][1]
        elif 1 < p <= 72:
            x = A[2][0][0] * x + A[2][0][1] * y + b[2][0]
            y = A[2][1][0] * x + A[2][1][1] * y + b[2][1]
        elif 72 < p <= 86:
            x = A[3][0][0] * x + A[3][0][1] * y + b[3][0]
            y = A[3][1][0] * x + A[3][1][1] * y + b[3][1]
        else:
            x = A[4][0][0] * x + A[4][0][1] * y + b[4][0]
            y = A[4][1][0] * x + A[4][1][1] * y + b[4][1]
        X.append(x)
        Y.append(y)


def saveImage(x1, y1, x2, y2):
    plt.grid()
    plt.plot(X, Y, color='red')
    if flagScaling:
        plt.xlim(x1, x2)
        plt.ylim(y1, y2)
    plt.savefig('image.jpg')


def changeOptions(dopSelect):
    if dopSelect == 1:
        printA()
        ch = choice()
        if 1 <= ch <= 4:
            print('Введите значения :', end='')
            str = input()
            arr = str.split(' ')
            if len(arr) == 4:
                A[ch] = [[int(arr[0]), int(arr[1])], [int(arr[2]), int(arr[3])]]
                print('Параметры успешно изменены')
                printA()
            else:
                print('Некорректное количество значений')
                return
        else:
            print('Некорректный пункт меню')

    elif dopSelect == 2:
        printb()
        ch = choice()
        if 1 <= ch <= 4:
            print('Введите значения :', end='')
            str = input()
            arr = str.split(' ')
            if len(arr) == 2:
                b[ch] = [int(arr[0]), int(arr[1])]
                print('Параметры успешно изменены')
                printb()
            else:
                print('Некорректное количество значений')
                return
        else:
            print('Некорректный пункт меню')
    else:
        print('Некорректный пункт меню')
        return


def scaling(scX1, scY1, scX2, scY2):
    plt.grid()
    plt.plot(X, Y, color='red')
    plt.xlim(scX1, scX2)
    plt.ylim(scY1, scY2)
    plt.show()


X = []
Y = []
x1 = 0
x2 = 0
y1 = 0
y2 = 0
flagGame = False
exit = True
flagScaling = False
while (exit):
    print('Для продожений нажмите Enter')
    input()
    system('clear')
    menu()
    print('Выберете действие:', end='')
    select = int(input())
    if select == 1:
        X = []
        Y = []
        game()
        plt.grid()
        plt.plot(X, Y, color='red')
        plt.show()
        flagGame = True
    elif select == 2:
        if not flagGame:
            print('Сначала сыграйте')
            continue
        saveImage(x1, y1, x2, y2)
    elif select == 3:
        dopMenu()
        print('Выберете действие:', end='')
        dopSelect = int(input())
        changeOptions(dopSelect)
    elif select == 4:
        if not flagGame:
            print('Сначала сыграйте')
            continue
        print('Введите область по X: ', end='')
        strx = input()
        x1 = int(strx.split(' ')[0])
        x2 = int(strx.split(' ')[1])
        print('Введите область по Y: ', end='')
        strx = input()
        y1 = int(strx.split(' ')[0])
        y2 = int(strx.split(' ')[1])
        scaling(x1, y1, x2, y2)
        flagScaling = True
    elif select == 5:
        exit = False
    else:
        print("Некорректный пункт меню")
