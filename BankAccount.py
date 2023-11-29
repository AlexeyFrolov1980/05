import os
import json

ACCOUNT_FILE_NAME = 'current_account.txt'

PURCHES_FILE_NAME = 'purches_history.txt'

"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню
"""


def put_to_account(sum_to_put):
    '''
    :param sum:
    :param current_sum:
    :return:
    '''

    if sum_to_put>0:
        current_sum=get_account_value()
        res = sum_to_put+current_sum
        save_account(res)
        return res
    else:
        print("Сумма должна быть больше 0")
        return current_sum


"""
2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню
"""


def purche():
    sum_input = float(input('Введите сумму покупки:'))
    account_sum = get_account_value()
    if sum_input<=account_sum:
        purche_name =input('Введите название покупки:')
        purches = get_purches()
        account_sum -=  sum_input
        purches.append([purche_name, sum_input])
        save_account(account_sum)
        save_purch(purches)

    else:
        print('денег не хватает')

    return account_sum, purches


"""
3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню
"""


def print_purches_history(purches):
    for pu in purches:
        print(pu)
    return



"""
4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""



def get_account_value(account_value_file_name=ACCOUNT_FILE_NAME):
    #Проверчем, что файл для записи сведений о сумме на счете еесть
    if os.path.exists(account_value_file_name):
        #Читаем из файла сумму
        with open(account_value_file_name, 'r', encoding='utf-8') as f:
            res = float(f.read())
        return res
    else:
        return 0

def save_account(accuont_sum, account_value_file_name=ACCOUNT_FILE_NAME):
    with open(account_value_file_name, 'w', encoding='utf-8') as f:
        f.write(str(accuont_sum))
    return accuont_sum


def save_purch(purches, purches_file_name=PURCHES_FILE_NAME):
    with open(purches_file_name, 'w') as f:
        json.dump(purches, f)


def get_purches(purches_file_name = PURCHES_FILE_NAME):
    if os.path.exists(purches_file_name):
        #Читаем из файла сумму
        with open(purches_file_name, 'r') as f:
            res = json.load(f)
        return res
    else:
        return list([])







def run_accout_menu():



    while True:
        account_sum=get_account_value()
        purches=get_purches()

        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        print('')
        print(f'Текущее состояние счета: {account_sum}')


        choice = input('Выберите пункт меню: ')
        if choice == '1':
            sum_to_put=float(input('Введите сумму для пополнения: '))
            put_to_account(sum_to_put)

        elif choice == '2':
            purche()

        elif choice == '3':
            purches=get_purches()
            print_purches_history(purches)
        elif choice == '4':
            return 0
        else:
            print('Неверный пункт меню')


#run_accout_menu()