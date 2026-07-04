num = int(input()) #при помощи while, мы можем обрабатывать числа, пока цифры в ней не закончатся (например, для подсчёта кол-ва цифр в числе)
counter = 0
while num != 0:
    last_digit = num % 10 #последняя цифра в числе (остаток от деления на 10)
    counter += 1
    num //= 10 #удаляем последнюю цифру в числе (целочисленное деление на 10)
print("Количество цифр в числе:", counter)
print()
num_1 = int(input()) #задача на наличие цифр 6 и 7 в числе input
has_six, has_seven = False, False
while num_1 != 0:
    last_digit = num_1 % 10
    if last_digit == 6:
        has_six = True
    elif last_digit == 7:
        has_seven = True
    num_1 //= 10
if has_six and has_seven:
    print("SIX SEVEEEEEEEEEEN!!!")
elif has_six:
    print("Have a six!")
elif has_seven:
    print("Has a seven!")
else:
    print("No any six or seven!")
print()
num_2 = int(input()) #при помощи for, можно решать задачи на значение каждой цифры по длине числа
n = len(str(num_2))
for i in range(1, n + 1):
    digit = num_2 // 10 ** (n - i) % 10
    print(i, '-я  цифра числа равна ', digit, sep='')
print()
num = 586
while num > 0:
    last_digit = num % 10
    print(last_digit, sep='*', end='#')
    num //= 10
    print()