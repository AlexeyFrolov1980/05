import BankAccount
import victory
# 4. В файле написать тесты для каждой ""чистой"" функции, чем больше тем лучше.
# Это могут быть функции консольного файлового менеджера, а так же программы мой счет и программы викторина

def test_put_to_account():
    assert BankAccount.put_to_account(10,100) == 110
    assert BankAccount.put_to_account(-10,100) == 100

def test_date_to_str():
    assert victory.date_to_str('21.01.2013') == 'двадцать первое января 2013 года'

# 5. (Дополнительно*) так же попробовать написать тесты для ""грязных"" функций,
# например копирования файла/папки, ...

