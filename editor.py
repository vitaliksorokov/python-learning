print('Это твой мини-редактор никнейма! Введи твой никнейм:')
nickname = input()
new_nickname, first_nickname = nickname, nickname #новый ник (изменяется), первый ник (исходный)
print('Твой ник: ', nickname, '! Что хочешь с ним сделать?', sep='')
print('1. Перевернуть', '2. Добавить буквы', '3. Убрать буквы', '4. Середина никнейма', '5. Сохранить результат', sep='\n')
action = int(input())
while action != 5: #пока не выбрана опция Сохранить результат
    while action > 5 or action < 1:
        print('Этого действия нету, попробуй ещё раз')
        print('1. Перевернуть', '2. Добавить буквы', '3. Убрать буквы', '4. Середина никнейма', '5. Сохранить результат', sep='\n')
        action = int(input())
    if action == 1: #переворот никнейма
        new_nickname = nickname[::-1] #переворот
        print('Твой новый ник: ', new_nickname)
        nickname = new_nickname
    elif action == 2: #добавить буквы
        middle = (len(nickname) + 1 ) // 2 #середина никнейма
        print(nickname[:middle], '|', nickname[middle:], sep='')
        print('Ты хочешь добавить буквы в первой или второй половине никнейма? 1 - первая половина, 2 - вторая половина')
        answer = int(input())
        if answer == 1: #первая половина
            print('Введи буквы, которые хочешь добавить: ')
            letters = input()
            new_nickname = letters + nickname[:middle] + nickname[middle:] #буквы + первая половина никнейма + вторая половина никнейма
            print('Твой новый ник: ', new_nickname)
            nickname = new_nickname
        elif answer == 2: #вторая половина
            print('Введи буквы, которые хочешь добавить: ')
            letters = input()
            new_nickname = nickname[:middle] + letters + nickname[middle:] #первая половина + буквы + вторая половина
            print('Твой новый ник: ', new_nickname)
            nickname = new_nickname
    elif action == 3: #удалить буквы
        if len(nickname) < 2: #если текущий ник состоит из 1 символа
            print('В твоём текущем никнейме слишком мало букв! Программа не может оставить пустое поле!')
        else:
            middle = (len(nickname) + 1 ) // 2 #середина никнейма
            print(nickname[:middle], '|', nickname[middle:], sep='') 
            print('Ты хочешь удалить буквы в первой или второй половине никнейма? 1 - первая половина, 2 - вторая половина')
            answer = int(input())
            if answer == 1: #первая половина
                print('Сколько первых букв из первой половины хочешь удалить?')
                n_letters = int(input())
                while n_letters > len(nickname[:middle]): #пока кол-во удаляемых букв больше, чем количество букв в первой половине
                    print('Программа не может удалить столько символов!')
                    n_letters = int(input())
                new_nickname = nickname[n_letters: middle] + nickname[middle:] #ник - от n-ного номера никнейма до середины никнейма + от середины до конца никнейма 
                print('Твой новый ник: ', new_nickname)
                nickname = new_nickname
            elif answer == 2: #вторая половина
                print('Сколько последних букв из второй половины хочешь удалить?')
                n_letters = int(input())
                while n_letters > len(nickname[middle:]): #пока кол-во удаляемых букв больше, чем количество букв во второй половине
                    print('Программа не может удалить столько символов!')
                    n_letters = int(input())
                new_nickname = nickname[:middle] + nickname[middle: -n_letters] #ник - от начала до середины никнейма + от середины никнейма до n * (-1) номера никнейма (n * (-1) = последняя буква, до которой идём)
                print('Твой новый ник: ', new_nickname)
                nickname = new_nickname    
    elif action == 4: #действие с серединой
        print('Пока автор не очень понимает, как это сделать и функция недоступна. Спасибо за понимание')
    print('Что сделаем дальше? ', '1. Перевернуть', '2. Добавить буквы', '3. Убрать буквы', '4. Оставить середину никнейма', '5. Сохранить результат', sep='\n')   
    action = int(input())
print('Поздравляю! Ты создал новый никнейм при помощи нашего редактора!', '\n', 'Исходный ник: ', first_nickname, '\n', 'Новый ник: ', nickname) #сохранение нового ника