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
if 6 < age <= 13:
    print("Вы ребёнок-школьник")
if 13 < age < 18:
    print("Вы подросток")
if 18 <= age:
    print("Вы взрослый!")
print()
# задачки
num = int(input())  # состоит ли число из 2 одинаковых цифр (двухзначное)
first_digit = num // 10
second_digit = num % 10
if second_digit == first_digit:
    print("ДА")
else:
    print("НЕТ")
if num >= 100:
    print("Число не двухзначное!")
print()

num, num1, num2 = (
    int(input()),
    int(input()),
    int(input()),
)  # сколько чисел из 3 являются чётными
counter = 0
if num % 2 == 0:
    counter = counter + 1
if num1 % 2 == 0:
    counter = counter + 1
if num2 % 2 == 0:
    counter = counter + 1

print("Из 3 чисел чётных:", counter)
print()

password1 = input()  # напишите и подтвердите пароль
password2 = input()
if password2 == password1:
    print("Пароль принят")
else:
    print("Пароль не принят")
print()

num1, num2, num3 = int(input()), int(input()), int(input())
d = num2 - num1
if num2 == (num1 + d) and num3 == (num2 + d):
    print("YES")
else:
    print("NO")
print()

a, b, c, d = (
    int(input()),
    int(input()),
    int(input()),
    int(input()),
)  # выберите из 4 чисел самое маленькое (без повторов)

if a < b:
    min_ab = a
else:
    min_ab = b

if c < d:
    min_cd = c
else:
    min_cd = d

if min_ab < min_cd:
    min_abcd = min_ab
else:
    min_abcd = min_cd

print(min_abcd)
print()

num = int(input())
a, b, c, d = (num // 1000) % 10, (num // 100) % 10, (num // 10) % 10, num % 10
if a + d == b - c:
    print("ДА")
else:
    print("НЕТ")
print()

language = "English"

if language != "English" != "Español":
    print("Язык по умолчанию не является ни английским, ни испанским")

if language != "English" != "Русский":
    print(
        "Язык по умолчанию не является ни английским, ни русским"
    )  # тут будут выводиться оба сообщения, если два условия будет верным (если вместо language вставим English, ничего не будет, если другой язык - будет)
print()
