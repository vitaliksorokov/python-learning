grade = int(input("Введите вашу оценку: "))
if grade >= 10:
    print("По пятибальной шкале:", 5)
elif grade >= 7:
    print("По пятибальной шкале:", 4)
elif grade >= 4:
    print("По пятибальной шкале:", 3)
elif grade >= 2:
    print("По пятибальной шкале:", 2)
else:
    print("Вы не аттестованы!")
