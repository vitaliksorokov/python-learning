from math import sqrt

print(
    "Я помогу найти тебе площадь треугольника! Какой у тебя вид треугольника - равносторонний, прямоугольный, разносторонний, равнобедренный? "
)
answer = input()
if answer == "равносторонний":
    print("Введи сторону треугольника: ")
    a = float(input())
    S_1 = (a**2 * (sqrt(3))) / 4
    print("Площадь твоего треугольника = ", round(S_1, 2))
elif answer == "прямоугольный":
    print("Введи катеты: ")
    a, b = float(input()), float(input())
    S_2 = (1 / 2) * (a * b)
    print("Площадь твоего треугольника = ", S_2)
elif answer == "разносторонний":
    print("Введи 3 стороны треугольника")
    a, b, c = float(input()), float(input()), float(input())
    if a + b > c and b + c > a and a + c > b:
        p = (a + b + c) / 2
        S = sqrt((p * (p - a) * (p - b) * (p - c)))
        print("Площадь треугольника = ", round(S, 2))
    else:
        print("Такого треугольника не существует!")
elif answer == "равнобедренный":
    print("Введи основание треугольника и боковую сторону: ")
    a, b = float(input()), float(input())
    c = b
    if (a > 0 and b > 0) and 2 * b > a:
        height = sqrt(b**2 - (a / 2) ** 2)
        S_3 = (a * height) / 2
        print("Площадь твоего треугольника = ", round(S_3, 2))
    else:
        print("Такого треугольника не существует!")
