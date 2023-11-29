

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


def put_to_account(sum, current_sum):
    '''
    :param sum:
    :param current_sum:
    :return:
    '''

    if sum>0:
        return sum+current_sum
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


def purche(account_sum, purches):
    sum=float(input('Введите сумму покупки:'))
    if sum<=account_sum:
        purche_name=input('Введите название покупки:')
        account_sum -= sum

        purches.append([purche_name,sum])
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



def run_accout_menu(account_sum, purches):
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        print('')
        print(f'Текущее состояние счета: {account_sum}')


        choice = input('Выберите пункт меню: ')
        if choice == '1':
            sum=float(input('Введите сумму для пополнения: '))
            account_sum=put_to_account(sum, account_sum)

        elif choice == '2':
            account_sum, purches=purche(account_sum, purches)

        elif choice == '3':
            print_purches_history(purches)
        elif choice == '4':
            return account_sum, purches
        else:
            print('Неверный пункт меню')
