print("В Python есть несколько способов вывести символы из списка:")
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(numbers)):  # первый способ - через for с индексами
    print(numbers[i])
print()
for num in range(len(numbers)):  # второй способ - через for с переменной
    print(num)
print()
print(
    *numbers, sep="\n"
)  # третий способ - при помощи распаковки списка (достигается это при помощи символа звёздочки в начале; его можно сделать через пробел или через строку)
print(
    "Метод вывода элементов при помощи * в начале работает также и для строк. Важно - нужно, чтобы она была вписана в переменную и не заключать её в кавычки!"
)
s = "Python"
print(*s)
print(
    "На распаковку списка не влияет фактор наличия только строк, только чисел или же наличие этих 2 типов данных!"
)
date = [23, "мая", 2009]
print(*date)
print()
numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111] #задача на сумму квадратов всех чисел в списке
total = 0
for i in numbers:
    total += i ** 2
print(total)
print() #задача на вывод чисел - сначала отрицательных, потом нулей, потом положительных
n = int(input())
negatives, positives, zeros = [], [], []
for i in range(n):
    digit = int(input())
    if digit < 0:
        negatives.append(digit)
    elif digit > 0:
        positives.append(digit)
    else:
        zeros.append(digit)
print(*negatives, sep='\n')
print(*zeros, sep='\n')
print(*positives, sep='\n')
print()
n = int(input()) #задача на добавление уникальных слов в список
words = []
for i in range(n):
    text = str(input())
    if text not in words:
        words.append(text)
    else:
        continue
print(*words, sep='\n')
print()
n = int(input()) #задача на вывод списков чисел и квадрата суммы числа + 1
numbers = []
numbers_2 = []
for i in range(n):
    digit = int(input())
    digit_2 = (digit + 1) ** 2
    numbers.append(digit)
    numbers_2.append(digit_2)
print(*numbers, sep='\n')
print()
print(*numbers_2, sep='\n')
print()
