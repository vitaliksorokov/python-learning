from math import sqrt

num = int(input())
flag = True
for i in range(2, int(sqrt(num)) + 1):
    if num % i == 0:
        flag = False
        break  # при помощи break мы можем мгновенно завершить цикл, если выполнилось какое-то условие
if flag:  # if flag == True
    print("Число простое")
else:
    print("Число составное")
print()
print(
    "Код с простыми/составным числами - наглядный пример использования break.",
    "\n"
    "Если мы введём большое число и не будем сразу завершать цикл по нахождению первого делителя - программа будет обрабатывается очень долго!",
)
print()
total = 0  # программа будет считать наши 10 чисел, но если мы введём отрицательное число - сразу прекратит работу и выдаст результат
for i in range(10):
    num = int(input())
    if num < 0:
        break
    total += num
print(total)
print()
num = int(input())
number = num
flag = False
while num != 0:
    last_digit = num % 10
    if last_digit == 5:
        flag = True
        break
    num //= 10
if flag:
    print("В числе есть цифра 5")
else:
    print("В числе нету цифры 5")
print()
print(
    "Мы можем внедрять несколько условий для остановки цикла, если каждое условие будем по отдельности if: break!"
)
print()
for i in range(1, 101):
    if i == 2 or i == 10 or i == 20 or i == 50 or i == 100:
        continue  # при помощи continue мы можем пропустить отдельные элементы, при этом НЕ останавливая сам цикл
    print(i, end=" ")
