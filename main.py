import os
import shutil
import platform
import victory
import BankAccount


MAIN_MENU={ 1: 'создать папку',
            2: 'удалить (файл/папку)',
            3: 'копировать (файл/папку)',
            4: 'просмотр содержимого рабочей директории',
            5: 'посмотреть только папки',
            6: 'посмотреть только файлы',
            7: 'просмотр информации об операционной системе',
            8: 'создатель программы',
            9: 'играть в викторину',
            10: 'мой банковский счет',
            11: 'смена рабочей директории (*необязательный пункт)',
            12: 'выход'}

current_dir = os.getcwd()


def show_menu(menu):
    while True:
        for key, value in menu.items():
            print(key, ' : ', value)

        print('')

        choice = int(input('Выберите пункт меню: '))
        if choice in menu:
            return choice
        else:
            print('Неверный пункт меню')


account_sum = 0.0
purches = []

while True:

    current_dir = os.getcwd()
    print("Текущая деректория: ", current_dir)

    choice=show_menu(MAIN_MENU)

    if choice == 1:
        #- создать папку
        #после выбора пользователь вводит название (папки,
        #создаем) её в рабочей директории;
        new_folder_name = input('Введите название новой папки:  ')

        try:
            os.mkdir(new_folder_name)
            print(f"Папка \"{new_folder_name}\" успешно создана!")
        except:
            print('Ощибка при создании папки')

    elif choice == 2:
        #- удалить (файл/папку)
        #после выбора пользователь вводит название папки или файла,
        #удаляем из рабочей директории если такой есть;
        del_f_name = input('Ввtдите название папки или файла для удаления:  ')

        del_result = False

        # Пытаемся удалить как файл
        try:
            os.remove(del_f_name)
            print(f"Файл \"{del_f_name}\" успешно удален!")
            del_result = True
        except:
            pass

        # Пытаемся удалить как папку
        try:
            os.rmdir(del_f_name)
            print(f"Папка \"{del_f_name}\" успешно удалена!")
            del_result = True
        except:
            pass

        if not del_result:
            print('Ощибка при удалении папки или файла')


    elif choice == 3:
        #- копировать (файл/папку)
        #после выбора пользователь вводит название папки/файла
        #и новое название папки/файла. Копируем;
        file_src = input('Ввtдите имя файла или папки для копирования:  ')
        file_des = input('Ввtдите имя файла/папки-копии:  ')

        copy_result=False
        #Копируем как файл
        try:
            shutil.copy(file_src, file_des)
            print(f"Файл \"{file_src}\" успешно скопирован!")
            copy_result = True
        except:
            pass

        try:
            shutil.copytree(file_src, file_des)
            print(f"Каталог \"{file_src}\" успешно скопирован!")
            copy_result = True
        except:
            pass

        if not copy_result:
            print('Ощибка при копировании')
        pass
    elif choice == 4:
        #- просмотр содержимого рабочей директории
        #вывод всех объектов в рабочей папке;
        dir_list = os.listdir(current_dir)
        print("Файлы и папки в каталоге'", current_dir, "' :")
        # prints all files
        print(dir_list)
        pass
    elif choice == 5:
        #- посмотреть только папки
        #вывод только папок которые находятся в рабочей папке;
        onlydirs = [d for d in os.listdir(current_dir) if os.path.isdir(os.path.join(current_dir, d))]
        print("Папки в каталоге'", current_dir, "' :")
        print(onlydirs)

    elif choice == 6:
        #вывод только папок которые находятся в рабочей папке;
        #- посмотреть только файлы
        onlyfiles = [f for f in os.listdir(current_dir) if os.path.isfile(os.path.join(current_dir, f))]
        print("Файлы в каталоге'", current_dir, "' :")
        print(onlyfiles)

    elif choice == 7:
        #вывести информацию об операционной системе (можно использовать пример из 1-го урока);
        print("Информация об ОС")
        print(platform.uname())
    elif choice == 8:
        #- создатель программы вывод информации о создателе программы;
        print("Создатель программы: Алексей Фролов")
    elif choice == 9:
        #- играть в викторину запуск игры викторина из предыдущего дз;
        victory.play_victorine()
    elif choice == 10:
        #- мой банковский счет
        #запуск программы для работы с банковским счетом из предыдущего дз
        # (задание учебное, после выхода из программы управлением счетом в главной программе сумму
        # и историю покупок можно не запоминать);
        account_sum, purches=BankAccount.run_accout_menu(account_sum, purches)
    elif choice == 11:
       #- смена рабочей директории (*необязательный пункт)
       #усложненное задание пользователь вводит полный /home/user/... или относительный user/my/... путь.
       new_dir=input("Введите новый рабочий каталог: ")
       #Проверяем что каталог существует
       if os.path.exists(new_dir):
           os.chdir(new_dir)
           print(f'Текущий каталог изменен на {new_dir}:')
       else:
           print(f'Такого каталога {new_dir} не существует:')


    elif choice == 12:
        # Выход
        break