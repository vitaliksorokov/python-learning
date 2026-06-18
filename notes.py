age = int(input("Введите возраст "))
if 18 > age:
    print("Паспорт не положен!")
else:
    print("Вот ваш паспорт!")
print()
(
    a,
    b,
    c,
    d,
) = (
    int(input()),
    int(input()),
    int(input()),
    int(input()),
)
if a < b:
    max_ab = b
    min_ab = a
else:
    max_ab = a
    min_ab = b
if c < d:
    max_cd = d
    min_cd = c
else:
    max_cd = c
    min_cd = d
if max_ab < max_cd:
    max_abcd = max_cd
else:
    max_abcd = max_ab

if min_ab < min_cd:
    min_abcd = min_ab
else:
    min_abcd = min_cd

print(max_abcd + min_abcd)
print()
a = int(input())
if -1 < a < 17:
    print("Принадлежит")
else:
    print("Не принадлежит")
print()
a = int(input())
if 1000 <= a <= 9999:
    if a % 7 == 0 or a % 17 == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
print()
a, b, c = int(input()), int(input()), int(input())
if (a + b > c) and (a + c > b) and (b + c > a):
    print("YES")
else:
    print("NO")
print()
x, y, x_1, y_1 = (
    int(input()),
    int(input()),
    int(input()),
    int(input()),
)  # задача на шахматы (гнусная ладья)
if 1 <= x <= 8 and 1 <= y <= 8 and (y_1 == y or x_1 == x):
    print("YES")
else:
    print("NO")
print()
x, y, x_1, y_1 = (
    int(input()),
    int(input()),
    int(input()),
    int(input()),
)  # задача на шахматы (вонючий король)
if (x_1 == x + 1 or x_1 == x - 1 or x_1 == x) and (
    y_1 == y + 1 or y_1 == y - 1 or y_1 == y
):
    print("YES")
else:
    print("NO")
print()
x, y, x_1, y_1 = (
    int(input()),
    int(input()),
    int(input()),
    int(input()),
)  # задача на шахматы (гадкий слон)
if (x + y == x_1 + y_1) or (x - y == x_1 - y_1):
    print("YES")
else:
    print("NO")
print()
x, y, x_1, y_1 = (
    int(input()),
    int(input()),
    int(input()),
    int(input()),
)  # задача на шахматы (нечестивый конь)
if (abs(x - x_1) == 1 and abs(y - y_1) == 2) or (
    abs(x - x_1) == 2 and abs(y - y_1) == 1
):
    print("YES")
else:
    print("NO")
print()
x, y, x_1, y_1 = (
    int(input()),
    int(input()),
    int(input()),
    int(input()),
)  # задача на шахматы (ужасный ферзь)
if (abs(x - x_1) == abs(y - y_1)) or (y == y_1) or (x == x_1):
    print("YES")
else:
    print("NO")
print()
a, b, c = int(input()), int(input()), int(input())  # задача на треугольники
if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print("Равносторонний")
    elif a == b or a == c or b == c:
        print("Равнобедренный")
    else:
        print("Разносторонний")
else:
    print("Такого треугольника не существует")
print()
a, b, c = (
    int(input()),
    int(input()),
    str(input()),
)  # простой калькулятор (плюс-минус, умножение-деление на 2 числа)
if not (c != "/" and c != "*" and c != "-" and c != "+"):
    if c == "+":
        print(a + b)
    elif c == "-":
        print(a - b)
    elif c == "*":
        print(a * b)
    elif c == "/":
        if b != 0:
            print(a / b)
        else:
            print("На ноль делить нельзя!")
else:
    print("Неверная операция")
print()
colour1, colour2 = str(input()), str(input())  # смешивание цветов
if (colour1 == "красный" or colour1 == "синий" or colour1 == "желтый") and (
    colour2 == "красный" or colour2 == "синий" or colour2 == "желтый"
):
    if colour1 == colour2:
        print(colour1)
    else:
        if (colour1 == "красный" and colour2 == "синий") or (
            colour2 == "красный" and colour1 == "синий"
        ):
            print("фиолетовый")
        elif (colour1 == "красный" and colour2 == "желтый") or (
            colour2 == "красный" and colour1 == "желтый"
        ):
            print("оранжевый")
        elif (colour1 == "желтый" and colour2 == "синий") or (
            colour2 == "желтый" and colour1 == "синий"
        ):
            print("зеленый")
else:
    print("ошибка цвета")
print()
a = int(input())  # цвет колеса рулетки
if 0 <= a <= 36:
    if a == 0:
        print("зеленый")
    else:
        if 1 <= a <= 10:
            if a % 2 == 0:
                print("черный")
            else:
                print("красный")
        elif 11 <= a <= 18:
            if a % 2 == 0:
                print("красный")
            else:
                print("черный")
        elif 19 <= a <= 28:
            if a % 2 == 0:
                print("черный")
            else:
                print("красный")
        elif 29 <= a <= 36:
            if a % 2 == 0:
                print("красный")
            else:
                print("черный")
else:
    print("ошибка ввода")
print()
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if (a < b) and (c < d):  # пересечение отрезков
    if b == c:  # b == c
        print(b)
    elif a == d:  # a == d
        print(a)
    elif a <= c <= d and d < b:  # a <= c <= d, d < b
        print(c, d)
    elif c <= a <= d and b < d:  # c <= a <= d, b < d
        print(a, b)
    elif a <= c <= b and d >= b:  # a <= c <= b, d >= b
        print(c, b)
    elif c <= a <= d and b >= d:  # c <= a <= d, b >= d
        print(a, d)
    else:
        print("пустое множество")
else:
    print("ошибка")
