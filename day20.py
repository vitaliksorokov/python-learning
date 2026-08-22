letter = ord('A') #ord() - функция, которая возвращает числовой код символа в таблице ASCII
print(letter)
print('ASCII - схема кодировки, где при помощи чисел от 0 до 127 кодируются символы, цифры и знаки препинания.')
print('Если мы в функцию ord() введём несколько символов - она выдаст ошибку!')
letter_1 = chr(97) #chr() - функция, которая возвращает символ по его числовому коду в таблице ASCII
print(letter_1)
print('У маленькой и большой буквы в кодировке ASCII разный числовой код (разница в 32). Если мы в функцию chr() введём несколько чисел - она выдаст ошибку!')
print()
for i in range(26): #задача на вывод всех букв английского алфавита в верхнем регистре
    print(chr(ord('A') + i), end=' ') #ord() используем для числового кода буквы, а дальше при помощи chr() он конвертируется в букву
print()
print('Следует помнить, что буквы, например, русского и английского алфавита имеют совершенно разные числовые коды в таблице ASCII. Поэтому при работе с буквами разных алфавитов нужно быть внимательным!')
print('Некоторые программы по редакции кода, например VS Code, имеют автоматическую подсветку букв разных алфавитов, что помогает избежать ошибок при работе с ними.')
for i in range(32):
    print(chr(ord('а') + i), end=' ') #задача на вывод всех букв русского алфавита в нижнем регистре
print()
letter = input() #задача на нахождение следующей буквы в алфавите (русский алфавит)
if ord(letter) >= ord('Я'):
    print('Дальше букв нет')
else:
    print(chr(ord(letter) + 1))
print()
a, b = int(input()), int(input()) #задача на вывод всех букв в диапазоне от a до b (по числовым кодам в таблице ASCII)
for i in range(a, b + 1):
    print(chr(i), end=" ")
print()
text = input() #задача на шифрование текста по ASCII
for i in range(len(text)):
    print(ord(text[i]), end=' ')
print()
heaviest_word, maximum = 0, 0 #задача на нахождение самого "тяжёлого" слова в строке (по сумме числовых кодов букв в таблице ASCII)
for i in range(4):
    text = input()
    word = 0
    for i in range(len(text)):
        word += ord(text[i])
    if word > maximum:
        maximum = word
        heaviest_word = text
print(heaviest_word)
print()
text = input() #задача на цену сообщения в пчёлках
letter_price, message_price = 0, 0
for i in range(len(text)):
    letter_price = ord(text[i]) * 3
    message_price += letter_price
    letter_price = 0
print(f"Текст сообщения: '{text}'")
print(f'Стоимость сообщения: {message_price}🐝')
print()
text = input() #задача на стоимость сообщения, но с мухляжем
eng, rus = 'eyopaxcETOPAHXCBM', 'еуорахсЕТОРАНХСВМ'
letter_price, message_price, lEtter_price, mEssage_price = 0, 0, 0, 0
for c in text:
    if c in 'eyopaxcETOPAHXCBM':
        for i in range(len(rus)):
            c = c.replace(eng[i], rus[i])
        letter_price = ord(c) * 3
        message_price += letter_price
        letter_price
    else:
        letter_price = ord(c) * 3
        message_price += letter_price
        letter_price
for s in text:
    lEtter_price = ord(s) * 3
    mEssage_price += lEtter_price
    lEtter_price = 0
print(f'Старая стоимость: {mEssage_price}🐝')
print(f'Новая стоимость: {message_price}🐝')
print()
