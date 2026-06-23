print("Первая система голосования: ")
counter = 0
score = 0
for i in range(2):
    print(
        "Голосует Страна",
        i + 1,
        "!",
        "\n",
        "Введите за кого проголосует первый член жюри: ",
    )
    jury_1 = str(input())
    print(" Введите за кого проголосует второй член жюри: ")
    jury_2 = str(input())
    if jury_1 == jury_2:
        counter = 4
        print(jury_1, "получает 4 балла!")
        score_3 = int(counter)
        counter = 0
    elif jury_1 != jury_2:
        counter_1 = counter + 2
        counter_2 = counter + 2
        print(
            jury_1,
            "и",
            jury_2,
            "получили по 2 балла!",
        )
        score_1, score_2 = int(counter_1), int(counter_2)
        counter = 0
    country_1 = jury_1
    country_2 = jury_2
    country_3 = jury_1 == jury_2
    if country_1 == country_3:
        score_1 = score_1 + score_3
    else:
        score_1 = score_3
    if country_2 == country_3:
        score_2 = score_2 + score_3
    else:
        score_2 = score_3

print(country_1, score_1, country_2, score_2)
