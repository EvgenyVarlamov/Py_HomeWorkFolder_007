def menu():
    print('ТЕЛЕФОННЫЙ СПРАВОЧНИК')
    flag=True
    while flag == True:
        stat = int(input('Просмотр контактов "1", запись нового контакта "2", выход "3"\n'))
        if stat == 1 or stat == 2 or stat == 3:
            flag = not flag
    if stat == 1:
        print('Выберите формат вывода нового контакта')
        while flag == False:
            rec = int(input('Контакты в одну строку "1", контакты в четыре строки "4"\n'))
            if rec == 1 or rec == 4:
                flag = not flag
        if rec == 1:
            return 'read_1'
        elif rec == 4:
            return 'read_4'
    elif stat == 2:
        print('Выберите формат ввода нового контакта')
        while flag == False:
            rec = int(input('Ввод в одну строку "1", ввод в четыре строки "4"\n'))
            if rec == 1 or rec == 4:
                flag = not flag
        if rec == 1:
            return 'write_1'
        elif rec == 4:
            return 'write_4'
    else:
        return 'exit'


def get_data(mes):
    return input(mes)


def output_data(data):
    print(data)
