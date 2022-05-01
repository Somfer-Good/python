from os import system


def loadFromFile(file, peoples):
    try:
        list = file.readlines()
        if len(list) != 0:
            for string in list:
                tmp = string.split(" ")
                peoples.append(
                    {
                        "surname": tmp[0],
                        "name": tmp[1],
                        "age": int(tmp[2]),
                        "index": int(tmp[3])
                    }
                )
    except:
        return False
    return True


def inputPeople(file, peoples):
    people = input().split(" ")
    file.write(people[0] + ' ' + people[1] + ' ' + str(people[2]) + ' ' + str(peoples[-1]["index"] + 1) + '\n')
    peoples.append(
        {
            "surname": people[0],
            "name": people[1],
            "age": int(people[2]),
            "index": int(peoples[-1]["index"] + 1)
        }
    )


def printPeople(peoples):
    print("Введите номер человека: ", end='')
    index = int(input())
    for people in peoples:
        if people["index"] == index:
            print(people["surname"], people["name"] + ",", people["age"])
            return
    print("Такого номера в списке нет")


def printPeopleOnAge(peoples):
    print("Введите возраст человека: ", end='')
    age = int(input())
    cnt = 0
    for people in peoples:
        if people["age"] == age:
            print(people["surname"], people["name"] + ",", people["age"])
            cnt += 1
    if cnt == 0:
        print("Такого возраста в списке нет")


def printPeoples(peoples):
    i = 1
    for people in peoples:
        print(i, end='')
        print(".", people["surname"], people["name"] + ",", people["age"])
        i += 1


def deletePeople(peoples):
    print("Введите номер человека: ", end='')
    index = int(input())
    size = len(peoples)
    for people in peoples:
        if people["index"] == index:
            peoples.remove(people)
    if (len(peoples) == size):
        print("Такого номера в списке нет")
        return
    file = open('peoples.txt', 'w', encoding='utf-8')
    for people in peoples:
        file.write(
            people["surname"] + ' ' + people["name"] + " " + str(people["age"]) + " " + str(people["index"]) + '\n')
    file.close()
    file = open('peoples.txt', 'r+', encoding='utf-8')


def menu():
    print("1. Добавить нового человека")
    print("2. Вывод ФИ и возраста человека")
    print("3. Вывод всех людей по заданному возрасту")
    print("4. Распечатать людей")
    print("5. Удалить человека по номеру")
    print("6. Выход")


def students_add(student: list):
    print(student)


exit = True
peoples = []
file = open('peoples.txt', 'r+', encoding='utf-8')
if not loadFromFile(file, peoples):
    print("Error file!")
    exit = False
while (exit):
    system("clear")
    menu()
    print("Выберете команду:", end=' '),
    selectMenu = int(input())
    if selectMenu == 1:
        inputPeople(file, peoples)
    elif selectMenu == 2:
        printPeople(peoples)
    elif selectMenu == 3:
        printPeopleOnAge(peoples)
    elif selectMenu == 4:
        printPeoples(peoples)
    elif selectMenu == 5:
        deletePeople(peoples)
    elif selectMenu == 6:
        break
    elif selectMenu > 6 or selectMenu < 1:
        print("Неверная команда")
    print("Для продолжения нажмите enter")
    input()
