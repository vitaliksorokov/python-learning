age = int(input("Введите возраст "))
if 18 > age:
    print("Паспорт не положен!")
else:
    print("Вот ваш паспорт!")
print()
(
    a,
    b,
    c,
    d,
) = (
    int(input()),
    int(input()),
    int(input()),
    int(input()),
)
if a < b:
    max_ab = b
    min_ab = a
else:
    max_ab = a
    min_ab = b
if c < d:
    max_cd = d
    min_cd = c
else:
    max_cd = c
    min_cd = d
if max_ab < max_cd:
    max_abcd = max_cd
else:
    max_abcd = max_ab

if min_ab < min_cd:
    min_abcd = min_ab
else:
    min_abcd = min_cd

print(max_abcd + min_abcd)
