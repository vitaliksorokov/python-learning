grade = int(
    input("Введите вашу оценку: ")
)  # используем elif, чтобы программа искала условие из предложенных, пока его не найдёт или не воспользуется else (необязательно)
if grade >= 10:
    print("По пятибальной шкале:", 5)
elif grade >= 7:
    print("По пятибальной шкале:", 4)
elif grade >= 4:
    print("По пятибальной шкале:", 3)
elif grade >= 2:
    print("По пятибальной шкале:", 2)
else:
    print("Вы не аттестованы!")
print()
x = int(input())
y = int(input())
# это задача про координатную четверть, но укорочена при помощи вложенного оператора - мы вставляем условия if и else внутри другого if
if x > 0:
    if y > 0:
        print("Первая четверть")
    else:
        print("Четвертая четверть")
else:
    if y > 0:
        print("Вторая четверть")
    else:
        print("Третья четверть")
print()
print("Условие elif является подвидом вложенного оператора")
print()
a, b, c = int(input()), int(input()), int(input())
if a == b:
    if b == c:
        print("Одинаковых чисел:", 3)
    else:
        print("Одинаковых чисел:", 2)
else:
    if a == c:
        print("Одинаковых чисел:", 2)
    else:
        if b == c:
            print("Одинаковых чисел:", 2)
        else:
            print("Нет одинаковых чисел")
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
