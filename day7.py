s = input()  # мы вводим строку, тип данных - str
s1 = "Питон рулит!"  # строка, тип данных - str
s2, s3 = "", " "  # пустая строка и строка из пробела, тип данных - str
length = len(
    s1
)  # функция len, для подсчёта кол-ва симоволов в строке (с пробелами и знаками)
print(s1, length)  # переменная length вывела количество символов в строке переменной s1
s1, s2 = "Питон рулит!", str(
    float(input())
)  # str - позволяет преобразовать число в строку
print(s1, s2)
s3 = s2 + s1 + "!!!"  # мы можем складывать (сцеплять) строки, как числа, в одну строку
print(s3, "- От перестановки мест слагаемых строк результат меняется!")
s = input() * 3  # мы можем умножать строки для того, чтобы повторить её на n раз
print(
    s,
    "- число можно умножить на строку и наоборот, но нельзя умножить строку на строку. Если строку умножим на 0 - получится пустая строка",
)
text = """Python is an interpreted, high-level, general-purpose programming language.
Created by Guido van Rossum and first released in 1991, Python design 
philosophy emphasizes code readability with its notable use of significant whitespace."""  # многострочный текст
print(text)
print()  # задача на сцепление строк
print(
    '"Python is a great language!"'
    + ", said Fred."
    + ' "I don'
    + "'t ever remember having this much fun before."
    + '"',
    sep="",
)
print()
name, surname = str(input()), str(input())  # задача на встречу человека
print("Hello", name, surname + "!", "You have just delved into Python")
print()
club = str(input())  # задача на длину названия команды
print("Футбольная команда", club, "имеет длину", len(club), "символов")
print()
first_city = input()  # задача на длины 3 городов
second_city = input()
third_city = input()

# ищем минимальную длину среди всех городов
min_city_len = min(len(first_city), len(second_city), len(third_city))
# ищем максимальную длину среди всех городов
max_city_len = max(len(first_city), len(second_city), len(third_city))

# длину каждого города сравниваем с минимальной длиной
if len(first_city) == min_city_len:
    print(first_city)
elif len(second_city) == min_city_len:
    print(second_city)
else:
    print(third_city)

# длину каждого города сравниваем с максимальной длиной
if len(first_city) == max_city_len:
    print(first_city)
elif len(second_city) == max_city_len:
    print(second_city)
else:
    print(third_city)
print()
a, b, c = input(), input(), input()

max_len = max(len(a), len(b), len(c))
min_len = min(len(a), len(b), len(c))

if (
    (max_len + min_len) / 2 == (len(a))
    or (max_len + min_len) / 2 == len(b)
    or (max_len + min_len) / 2 == len(c)
):
    print("YES")
else:
    print("NO")
print()
s = str(input())
if "е" in s:  # оператор in - позволяет проверить наличие одной строки внутри другой
    print("Тут есть буква е")
else:
    print("Тут нету буквы е")
s = str(input())
if "." not in s:
    print("Тут нету точка")
else:
    print("Тут есть точка")
print(
    "При помощи in, мы можем сокращать код для проверки переменной на равенство/неравенство, а также наличия нескольких символов в строке"
)
print("ab" in "abc", "\n", "ac" in "abc", '\n', "Ab" in "abc" sep='') #для in важна точность последовательности. Также он чувствителен к регистру
