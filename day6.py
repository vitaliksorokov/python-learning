n = 17  # целое число, тип данных - int
print()
num = int(input())  # строка преобразовывается в целое число, тип данных - int
print(
    num,
    ".",
    "(В тип данных int должно быть указано ЦЕЛОЕ число, чтобы не было ошибки!)",
)
print()
a = 13
b = 7
# действия с целыми числами
total = a + b
diff = a - b
prod = a * b
div1 = a / b
div2 = a // b
mod = a % b
exp = a**b

print(a, "+", b, "=", total)  # сложение
print(a, "-", b, "=", diff)  # вычитание
print(a, "*", b, "=", prod)  # умножене
print(a, "/", b, "=", div1)  # деление
print(a, "//", b, "=", div2)  # целочисленное деления (без остатка)
print(a, "%", b, "=", mod)  # деление и вывод остатка
print(a, "**", b, "=", exp)  # возведение в степень
print()
print(
    "Особенность Python - неограниченность размера числа! Также числа можно разделять при помощи _"
)
atom = 10**80  # количество атомов во вселенной
print("Количество атомов =", atom)
print()
e = 2.71828  # число с плавающей точкой, тип данных - float
n = float(
    input()
)  # строка преобразовывается в число с плавающей точкой, тип данных - float
print(
    n,
    "При работе с числами с плавающими точками точно также используют операторы +, -, *, /, //, %, **",
)
print()
num = -16.67
num1 = int(num)  # преобразование числа с плавающей точкой в целое, тип данных - int
print(
    num1,
    "Если используем преобразование float в int - число будет округляться в сторону нуля!",
)
print()
a, b, c = (
    max(3, 8, -29, 67),
    min(-67, 91, 52, 290),
    abs(-0.67),
)  # функции максимум (max), минимум (min) и модуль (abs)
print(a, b, c)
a, b = float(input()), float(input())  # задача на площадь прямоугольного треугольника
print((1 / 2) * (a * b))
print()
a = float(input())  # задача на обратные числа
if not (a == 0):
    A = a**-1
    print(A)
else:
    print("Обратного числа не существует")
print()
a = float(input())  # задача на нахождение первой цифры после точки
A = int((a - int(a)) / 0.1)
print(A)
print()
a, b, c, d, e = (
    int(input()),
    int(input()),
    int(input()),
    int(input()),
    int(input()),
)  # задача на наибольшее и наименьше число из 5 чисел
print(
    "Наименьшее число = ",
    min(a, b, c, d, e),
    "\n",
    "Наибольшее число = ",
    max(a, b, c, d, e),
    sep="",
)
print()
a, b, c, d, e = (
    float(input()),
    float(input()),
    float(input()),
    float(input()),
    float(input()),
)  # задача на сумму модулей 5 чисел
print(abs(a) + abs(b) + abs(c) + abs(d) + abs(e))
print()
n = int(input())
digit1 = n % 10
digit2 = n // 10 % 10
digit3 = n // 100 % 10

if digit1 == digit2 + digit3 or digit2 == digit1 + digit3 or digit3 == digit1 + digit2:
    print("Число интересное")
else:
    print("Число неинтересное")
