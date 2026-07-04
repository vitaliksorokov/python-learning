num = int(input())
while (
    num % 10 != 0
):  # цикл while - позволяет программе выполнять определённый блок команд, пока не выполнится условие while
    print(
        "Не юбилейная дата!"
    )  # блок команд - выполняется, пока условие не будет выполнено
    num = int(input())
print(
    "Не забудь поставить переменную input внутри цикла - иначе получиться бесконечный цикл!"
)
print()
for i in range(5):
    print(i)
print()
# два кода, выполняющие одну и ту же задачу (сверху - с циклом for, снизу - с циклом while)
i = 0
while i < 5:
    print(i)
    i += 1
print()
text = input()
total = 0
while text != "stop":
    total += int(text)
    text = input()
print("Сумма чисел равна", total)
