import math  # модуль math - нужно ввести, чтобы открыть функции библиотеки math

A = float(input())
a = math.sqrt(int(A))  # квадратный корень из числа
b = math.ceil(float(A))  # округление в большую сторону
c = math.floor(float(A))  # округление в меньшую сторону
print(a, b, c)
print("""Если мы  не хотим писать название модуля math и точку"
    - в начале нужно написать from math import .., .. "
    (вставь нужные функции или * для импорта всех функций)""")
print()
print(
    int(A), round(A), round(A, 1)
)  # встроенные функции - int(округлить в меньшую сторону), round(округлить до целого числа), round(A, n)(округлить число до n знаков после точки)
print()
R = float(input())  # задача на площадь круга и длину окружности
S = math.pi * R**2
C = 2 * math.pi * R
print(S, "\n", C, sep="")
print()
x = float(input())  # задача на сумму пола и потолка числа
x_1, x_2 = math.floor(x), math.ceil(x)
print(x_1 + x_2)
print()
x_1, y_1, x_2, y_2 = (
    float(input()),
    float(input()),
    float(input()),
    float(input()),
)  # задача на евклидово расстояние
p = math.sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)
print(p)
print()
a, b, c, d = (
    int(input()),
    int(input()),
    int(input()),
    int(input()),
)  # задача на манхэттенское расстояние
M = abs(a - c) + abs(b - d)
print(M)
print()
x = float(input())  # задача на сложение тригонометрических функций
r = math.radians(x)
print(math.sin(r) + math.cos(r) + (math.tan(r) ** 2))
print()
n, a = int(input()), float(input())
S = (n * a**2) / (4 * math.tan(math.pi / n))
print(S)
print()
a, b = float(input()), float(input())  # задача на средние числа из 2 чисел
S = (a + b) / 2
S_1 = math.sqrt(a * b)
S_2 = (2 * a * b) / (a + b)
S_3 = math.sqrt((a**2 + b**2) / 2)
print(S, "\n", S_1, "\n", S_2, "\n", S_3, sep="")
print()
a, b, c = (
    float(input()),
    float(input()),
    float(input()),
)  # задача на квадратное уравнение
D = b**2 - 4 * a * c
if D < 0:
    print("Нет корней")
elif D == 0:
    x = -b / (2 * a)
    print(x)
elif D > 0:
    x_1 = (-b + math.sqrt(D)) / (2 * a)
    x_2 = (-b - math.sqrt(D)) / (2 * a)
    X, Y = max(x_1, x_2), min(x_1, x_2)
    print(Y, "\n", X, sep="")
