text = 'come alive, surrender to the Blinding light...' #в Python при работе со строками имеется большое количество методов - встроенных функций, которые связаны с конкретным объектом
print(text, '\n', text.capitalize(), sep='') #capitalize() - метод строки, который делает первый символ заглавным, а все остальные - строчным
print('Если символы в строке не являются буквами алфавита (цифры, знаки на клавиатуре), то метод capitalize() оставит их неизменными!')
print()
text = "I'm a angel, i'm DEMON, I'M A psycho for no ReASon..."
print(text, '\n', text.swapcase(), sep='') #swapcase() - метод строки, который меняет строчные буквы на заглавные и наоборот
print()
print(text.title()) #title() - метод строки, которые меняет первый символ КАЖДОГО слова на заглвный, а остальные символы - в строчные
print('Метод title не учитывает наличие апострофа или аббревиатуры, поэтому если в слове есть апостроф - то первый символ после него также заменится на заглавный, а аббревиатура будет написано только с первой заглавной буквой!')
print()
text = 'This is not enough!'
print(text, '\n', text.lower(), sep='') #lower() - метод строки, который меняет все символы на строчные
print()
print(text, '\n', text.upper(), sep='') #upper() - метод строки, который меняет все символы на заглавные
print()
print('Методы строк НЕ изменяют изначальную строку, а возвращают новую! Чтобы изменить значение переменной строки - нужно явно прописать это: text = text.метод_строки()!')
print()
text = input() #задача на проверку имени/фамилии на правильное написание
if text == text.title():
    print('YES')
else:
    print('NO')
print()
text = input() #задача на проверку текста на хороший оттенок
if 'хорош' in text.lower():
    print('YES')
else:
    print('NO')
print()
text = input() #задача на подсчёт количества буквенных строчных символов в тексте
s_text = text.lower()
count = 0
for i in range(len(text)):
    if text[i] == s_text[i] and text[i] not in '0123456789+-=%$#@!^&*()":;.,/\'~`<>[]{}_':
        count += 1
print(count)
print()
text = 'Loooooooove is a burning thing, and it makes a fiery ring...'
print(text, '\n', text.count('o'), '\n', text.count('o', 0, 5), sep='') #count() - метод строки, который подсчитывает количество вхождений подстроки в строку
print('Метод count() имеет 3 параметра - подстроку, с какого индекса начинать поиск и до какого индекса искать подстроку. Если не указать 2 последних параметра - поиск будет осуществляться по всей строке!')
print()
print(text.startswith('L'), text.startswith('...')) #startswith() - метод строки, который проверяет, начинается ли строка с указанной подстроки (True/False)
print(text.endswith('...'), text.endswith('L')) #endswith() - метод строки, который проверяет, заканчивается ли строка указанной подстрокой (True/False)
print()
text = 'jalla, jalla, they want jalla'
print(text, '\n', text.find('jalla'), sep='') #find() - метод строки, который возвращает индекс первого вхождения подстроки в строку (то есть индекс первого символа подстроки в строке)
print(text.find('they'))
print('Если подстрока не найдена - метод find() возвращает -1. Метод find() имеет 3 параметра - подстроку, с какого индекса начинать поиск и до какого индекса искать подстроку. Если не указать 2 последних параметра - поиск будет осуществляться по всей строке! rfind() - работает также, но с конца строки!')
print()
print(text.index('jalla'), text.index('they')) #index() - метод строки, который также возвращает индекс первого вхождения подстроки в строку (то есть индекс первого символа подстроки в строке)
print('Отличие index() и find() в том, что первый в случае ненахода индекса выдаст ошибку, а второй - просто вернёт -1! Однако, он также имеет версию rindex(), которая ищет с конца строки!')
print()
text = '                            Бугагашечки                        '
print(text.strip(), '\n', text.lstrip(), '\n', text.rstrip(), sep='') #strip() и его вариации l и r - метод строки, который удаляет пробелы в начале и конце строки (strip), только в начале (lstrip) или только в конце (rstrip)
print('Метод strip() и его вариации l и r - удаляют только пробелы в начале и/или конце строки, но не удаляют пробелы внутри строки!')
print()
text = 'jalla, jalla, they want jalla'
print(text, '\n', text.replace('jalla', 'more'), sep='') #replace() - метод строки, который заменяет указанную подстроку на другую подстроку
print('Метод replace() имеет 3 параметра - подстроку, на которую нужно заменить и количество замен. Если не указать 3-й параметр - замена будет произведена по всей строке!')
print()
text = input() #задача на подсчёт количества слов в строке (слово - это последовательность символов, разделённая пробелами)
print(text.count(' ') + 1)
print()
text = input() #задача на подсчёт количества АГЦТ в строке
text = text.upper()
print('Аденин:', text.count('А'))
print('Гуанин:', text.count('Г'))
print('Цитозин:', text.count('Ц'))
print('Тимин:', text.count('Т'))
print()
n = int(input()) #задача на подсчёт количества строк, в которых встречается подстрока '11' не менее 3-х раз
count = 0
for i in range(n):
    text = input()
    if text.count('11') >= 3:
        count += 1
print(count)
print()
text = input() #задача на подсчёт количества цифр в строке
count = 0
for i in range(10):
    count += text.count(str(i))
print(count)
print()
text = input() #задача на нахождение символа, который встречается в строке чаще всего
maximum, b = 0, 0
for i in range(len(text)):
    if text.count(text[i]) >= maximum:
        maximum = text.count(text[i])
        b = text[i]
print(b)
print()
text = input() #задача на нахождение индекса первого и последнего вхождения символа 'f' в строке
if text.count('f') == 1:
    print(text.find('f'))
elif text.count('f') >= 2:
    print(text.find('f'), text.rfind('f'))
else:
    print('NO')
print()
text = input() #задача на удаление из строки всех символов, которые находятся между первым и последним вхождением символа 'h'
first_index = int(text.find('h'))
last_index = int(text.rfind('h'))
print(text[0:first_index] + text[last_index + 1:])
print()
text, text1, text2 = 'Заборчик', '1234', '#####'
print(text.isalnum(), text1.isalnum(), text2.isalnum()) #isalnum() - метод строки, который проверяет, состоит ли строка только из букв и цифр (True/False)
print(text.isalpha(), text1.isalpha(), text2.isalpha()) #isalpha() - метод строки, который проверяет, состоит ли строка только из букв (True/False)
print(text.isdigit(), text1.isdigit(), text2.isdigit()) #isdigit() - метод строки, который проверяет, состоит ли строка только из цифр (True/False)
print('Пустые строки и строки из пробелов не считаются ни за одну из перечисленных категорий, поэтому для них все методы вернут False!')
print()
text, text1, text2 = 'Заборчик', '1234', 'ЗАБОРЧИК'
print(text.islower(), text1.islower(), text2.islower()) #islower() - метод строки, который проверяет, состоит ли строка только из строчных букв (True/False)
print(text.isupper(), text1.isupper(), text2.isupper()) #isupper() - метод строки, который проверяет, состоит ли строка только из заглавных букв (True/False)
print('Методы islower() и isupper() игнорируют небуквенные символы и возвращают False, если в строке нету букв, но при их наличие и выполнении буквами условия - вернут True!')
print()
text, text1 = '   ', 'Пробел'
print(text.isspace(), text1.isspace()) #isspace() - метод строки, который проверяет, состоит ли строка только из пробелов (True/False)
print('Пустая строка не равно пробелам, поэтому метод isspace() для пустой строки вернёт False!')
n = int(input()) #задача на запрещенные комментарии (пустые или только из пробелов)
for i in range(n):
    comment = input()
    if comment.isspace() == True or comment == '': #запрещенные комментарии
        print(i + 1, ': COMMENT SHOULD BE DELETED', sep='')
    else:
        print(i + 1, ': ', comment, sep='')
s = input() #задача на проверку, что номер автомобиля соответствует формату (буква + 3 цифры + _ + 2 буквы)
flag = 'NO'
correct_letters = 'АВЕКМНОРСТУХ'

if 9 <= len(s) <= 10:
    letters = s[0] + s[4:6]
    digits = s[1:4] + s[7:]
    underscore = s[6]

    if digits.isdigit() and underscore == '_':
        flag = 'YES'

    for c in letters:
        if c not in correct_letters:
            flag = 'NO'
            break

print(flag)