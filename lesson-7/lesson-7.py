from os import system

import numpy as np
import matplotlib.pyplot as plt


def menu():
    print('Вариант №17')
    print('1. График 4.1')
    print('2. График 4.2')
    print('3. График 4.3')
    print('4. График 4.4')
    print('5. Выход')


def schedule1():
    for i in X:
        Y.append(pow(abs(i - 1), 2 / 3) - pow(abs(i), 2 / 3))


def schedule2():
    for i in X:
        Y.append((2 * i * i - 7) / (pow((3 * i * i - 2), 1 / 2)))


def schedule3():
    for i in X:
        if i < 0:
            Y.append(abs(i) / (1 + i * i))
            continue
        Y.append(pow(1+i, 1 / 2))


def schedule4():
    for i in X:
        Y.append(pow(((1+(i*i/16))*25),1/2))
        Y1.append(-pow(((1+(i*i/16))*25),1/2))


while (True):
    system("clear")
    menu()
    print('Выберите график:', end='')
    select = int(input())
    plt.grid()
    plt.xlabel("x")
    plt.ylabel("y")
    X = np.linspace(-5, 5, num=256, endpoint=True)
    Y = []
    if select == 1:
        schedule1()
        plt.plot(X, Y, color='red', label="4.1")
    elif select == 2:
        schedule2()
        plt.plot(X, Y, color='red', label="4.2")
    elif select == 3:
        schedule3()
        plt.plot(X, Y, color='red', label="4.3")
    elif select == 4:
        Y1 = []
        X = np.linspace(-10, 10, num=1024, endpoint=True)
        schedule4()
        plt.yticks(np.linspace(-12, 12, num=25))
        plt.plot(X, Y, color='red', label="4.4")
        plt.plot(X, Y1, color='red')
    elif select == 5:
        break
    plt.legend(loc='upper left', frameon=False)
    plt.show()
