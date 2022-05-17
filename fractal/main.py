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
    3: [0, 0],
    4: [0, 0]
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
    X.clear()
    Y.clear()
    X1.clear()
    Y1.clear()
    x = random.random()
    y = random.random()
    X.append(x)
    Y.append(y)
    for i in range(1, 10000):
        p = random.randint(1, 100)
        if p == 1:
            x1 = A[1][0][0] * x + A[1][0][1] * y + b[1][0]
            y1 = A[1][1][0] * x + A[1][1][1] * y + b[1][0]
        elif 1 < p <= 72:
            x1 = A[2][0][0] * x + A[2][0][1] * y + b[2][0]
            y1 = A[2][1][0] * x + A[2][1][1] * y + b[2][1]
        elif 72 < p <= 86:
            x1 = A[3][0][0] * x + A[3][0][1] * y + b[3][0]
            y1 = A[3][1][0] * x + A[3][1][1] * y + b[3][0]
        else:
            x1 = A[4][0][0] * x + A[4][0][1] * y + b[4][0]
            y1 = A[4][1][0] * x + A[4][1][1] * y + b[4][0]
        X.append(x1)
        Y.append(y1)
        x = x1
        y = y1


def saveImage(x1, y1, x2, y2):
    plt.grid()
    ax.scatter(X, Y, c='r', s=1)
    ax.scatter(X1, Y1, c='b', s=1)
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
                A[ch] = [[float(arr[0]), float(arr[1])], [float(arr[2]), float(arr[3])]]
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
                b[ch] = [float(arr[0]), float(arr[1])]
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
    ax.scatter(X, Y, c='r', s=2)
    ax.scatter(X1, Y1, c='b', s=2)
    plt.xlim(scX1, scX2)
    plt.ylim(scY1, scY2)
    plt.show()


X = []
Y = []
X1 = []
Y1 = []
x1 = 0
x2 = 0
y1 = 0
y2 = 0
flagGame = False
exit = True
flagScaling = False
flagNew = True
while (exit):
    fig, ax = plt.subplots()
    fig.set_figwidth(8)
    fig.set_figheight(8)
    print('Для продожений нажмите Enter')
    input()
    system('clear')
    menu()
    print('Выберете действие:', end='')
    select = int(input())
    if select == 1:
        if flagNew:
            game()
        flagNew = False
        plt.grid()
        ax.scatter(X, Y, c='r', s=1)
        ax.scatter(X1, Y1, c='b', s=1)
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
        flagNew = True
    elif select == 4:
        if not flagGame:
            print('Сначала сыграйте')
            continue
        print('Введите область по X: ', end='')
        strx = input()
        arrX = strx.split(' ')
        if len(arrX) == 2:
            x1 = float(arrX[0])
            x2 = float(arrX[1])
        else:
            print('Неверное количество значений')
            continue
        print('Введите область по Y: ', end='')
        stry = input()
        arrY = stry.split(' ')
        if len(arrY) == 2:
            y1 = float(arrY[0])
            y2 = float(arrY[1])
        else:
            print('Неверное количество значений')
            continue
        scaling(x1, y1, x2, y2)
        flagScaling = True
    elif select == 5:
        exit = False
    else:
        print("Некорректный пункт меню")
