print("Использование циклов в разных сценариях: ")
print("Подсчёт количества:")
counter1 = 0  # при помощи цикла мы можем сделать подсчёт количество чисел, используя переменные counter в качестве счётчика
counter2 = 0
for _ in range(5):
    num = int(input())
    if num > 5:
        counter1 = counter1 + 1
    elif num == 0:
        counter2 = counter2 + 1
print("Кол-во чисел больше 5:", counter1)
print("Кол-во нулей:", counter2)
if counter1 > 2:
    print("Вы прошли уровень!")
else:
    print("Увы, вы не прошли уровень! Попробуйте ещё раз")
print()
print("Вычисление:")
total = 0  # при помощи цикла мы можем сделать вычисления суммы, разницы, произведения и деления нужных чисел, используя переменные total в качестве счётчика
for _ in range(5):
    num = int(input())
    if num > 5:
        total = total + num
average = total / 5
print("Сумма чисел больше 5 =", total)
print("Среднее значение =", average)
print("Если мы хотим найти произведение нужных чисел - в переменную ставим значение 1!")
print()
print("Максимальное/минимальное число:")
largest, smallest = (
    0,
    0,
)  # при помощи цикла мы можем находить максимальное/минимальное число от нужного кол-ва чисел, используя переменные largest или smallest в качесиве счётчика
for _ in range(5):
    num = int(input())
    if num > largest:
        largest = num
    elif num < smallest:
        smallest = num
    elif num == 0:
        nul = num
        print("Количество нулей:", nul)
print("Среди 5 чисел самое большое:", largest, "самое маленькое:", smallest)
print()
x, y = int(input()), int(input())
x, y = y, x  # код обмена двух переменных
print(x, y)
print()
print(
    "Для удобства, можно использовать расширенные операторы присваивания (сочетание операций +, -, *, /, //, % и =)"
)
x = 5
print(x)
x += 5
print(x)
x -= 5
print(x)
x *= 5
print(x)
x /= 5
print(x)
x //= 5
print(x)
x %= 5
print(x)
print()
num = int(input())
flag = True  # флажок - позволяет находить нужное условие в коде и выводить результат
for i in range(2, num):
    if num % i == 0:
        flag = False
    if num == 1:
        print("Единица не простое и не составное число")
    elif flag == True:
        print("Число простое")
    else:
        print("Число составное")
