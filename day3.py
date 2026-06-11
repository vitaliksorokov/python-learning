answer = input("Где мы работаем? ")  # if
if answer == "Python":  # условие 'если'
    print("Правильно! Мы работаем в Python!")
    print("Happy Pythoning!")  # блок команд (строки с отступом)
else:  # условие 'иначе'
    print("Неа, мы работаем не в", answer, "а в Python!")
print()

print('"="(присвоение) не равно "=="!(проверка)')
print()
num1, num2 = int(input("Введите число 1 ")), int(input("Введите число 2 "))
if num1 < num2:  # операторы сравнения >, <, ==, !=
    print(num1, "меньше", num2)
else:
    print(num1, "больше", num2)

if num1 == num2:
    print(num1, "равно", num2)
if num1 != num2:
    print(num1, "не равно", num2)
print()

age = int(input("Сколько вам лет? "))
if 3 <= age <= 6:  # цепочки сравнений
    print("Вы ребёнок")
if 6 <= age <= 13:
    print("Вы ребёнок-школьник")
if 13 <= age < 18:
    print("Вы подросток")
if 18 <= age:
    print("Вы взрослый!")
print()
# задачки
num = int(input())
first_digit = num // 10
second_digit = num % 10
if second_digit == first_digit:
    print("ДА")
else:
    print("НЕТ")
if num >= 100:
    print("Число не двухзначное!")
print()

num, num1, num2 = int(input()), int(input()), int(input())
counter = 0
if num % 2 == 0:
    counter = counter + 1
if num1 % 2 == 0:
    counter = counter + 1
if num2 % 2 == 0:
    counter = counter + 1

print("Из 3 чисел чётных:", counter)
print()

language = "English"

if language != "English" != "Español":
    print("Язык по умолчанию не является ни английским, ни испанским")

if language != "English" != "Русский":
    print(
        "Язык по умолчанию не является ни английским, ни русским"
    )  # тут будут выводиться оба сообщения, если хотя бы одно условие будет верным
