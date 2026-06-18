for i in range(
    10
):  # цикл - способ быстро повторять одни и те же действия, i - переменная цикла
    print("Python!")  # блок кода цикла (тело цикла)
    print("Как дела?")
for i in range(5):
    num = int(input())
    print("Квадрат твоего числа равен ", num * num)
print("Цикл завершён")
print()
for i in range(6):  # Задача на символы
    print("A" * 3)
for i in range(5):
    print("B" * 4)
print("E")
for i in range(9):
    print("T" * 5)
print("G")
print()
text, n = input(), int(input())  # задача на повторение текста на n количество раз
for i in range(n):
    print(text)
print()
n = int(input())  # задача на прямоугольник
for i in range(n):
    print("*" * 19)
print()
for i in range(5):
    print(i)
print(
    """Когда цикл начинает работу - i равен 0 и каждое повторение прибавляет 1! 
      К нему можно присоединять строки (через запятую) или добавлять/отнимать другие числа"""
)
for i in range(5):
    print(i + 1, "-- Привет!")
print(
    'Если переменная цикла не используется в блоке кода, то в названии переменной ставим "_"!'
)
print()
n = int(input())  # задача на квадрат текущего числа
for i in range(n + 1):
    print("Квадрат числа", i, "равен", i * i)
print()
n = int(input())  # задача на треугольник
for i in range(n):
    print("*" * (n - i))
m, p, n = int(input()), int(input()), int(input())  # задача на сложный процент
for i in range(n):
    print(i + 1, round(m * ((1 + (p / 100)) ** i, 2)))
