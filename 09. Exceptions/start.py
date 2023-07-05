# try:
#     number = int(input("Enter a number: "))

#     print(number)
# except:
#     print("Invalid type")



# try:
#     number = int(input("Enter a number: "))

#     print(number)
# except ValueError as error:
#     print("Invalid type:", error)



# import sys

# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error:", err)
# except ValueError:
#     print("Could not convert data to an integer.")
# except Exception as err:
#     print(f"Unexpected {err=}, {type(err)=}")
#     raise



# ------------------------------------------------------------


"""Завдання 1

Напишіть програму, яка запитує в користувача число і обчислює його квадратний корінь. 
Обробіть виняток, що виникає при введенні від'ємного числа, і виведіть повідомлення про помилку."""

# from math import sqrt

# try:
#     number = int(input("Enter a number: "))
#     sqrt_ = sqrt(number)
#     print(f"sqrt({number}) = {sqrt_}")
# except ValueError:
#     print("Error!")

"""Реалізуйте перше завдання через функцію. Функція повинна приймати число як параметр і повертати квадратний корінь числа.
 Перевірка коректності отриманих даних повинна бути всередині функції. Створіть дві версії реалізації функції:

Перша версія не обробляє виняток всередині функції. Уся обробка знаходиться зовні;
Друга версія обробляє виняток усередині функції."""

# from math import sqrt

# def sqrt_with_try(number):
#     try:
#         return sqrt(number)
#     except ValueError:
#         return "Enter a number bigger than 0"


# try:
#     number = int(input("Enter a number: "))
#     sqrt_ = sqrt(number)
#     print(f"sqrt({number}) = {sqrt_}")
# except ValueError:
#     print("Enter a number bigger than 0")



# number = int(input("Enter a number: "))
# sqrt_ = sqrt_with_try(number)
# print(sqrt_)


"""Напишіть програму, яка дає змогу заповнити користувачеві словник із клавіатури парами "ключ/значення". 
Після отримання даних відобразіть на екрані меню, яке дозволяє виконати такі операції:

Відображення словника;
Пошук значення в словнику;
Заміна значення в словнику. Значення має бути знайдено за ключем;
Відображення значення за ключем, введеним користувачем;
Видалення значення за ключем, введеним користувачем.

Обробіть виняток, що виникає під час виходу за межі словника (користувач ввів невірний ключ), і 
виведіть повідомлення про помилку."""


dict = {}

for i in range(3):
    key = input("Enter a key: ")
    item = input("Enter an item: ")

    dict[key] = item

exit = False

while not exit:
    choice = int(input(f"{dict}\n1. Search the element in dictionary\n2. Change the element in dictionary\n3. Search via key\n4. Delete via key\n0.Exit\n> "))
    if choice == 0:
        exit = True
        break
    elif choice == 1:
        try:
            search_item = input("Enter an element: ")
            for value in dict:
                pass
        except ValueError as error:
            print(f"Error: {error}")
        except Exception as error:
            print(f"Error: {error}")
    elif choice == 2:
        try:
            print(dict)
            change_by_key = input("Enter a key to change: ")
            new_item = input("Enter a new element: ")
            dict[change_by_key] = new_item
        except ValueError as error:
            print(f"Error: {error}")
        except Exception as error:
            print(f"Error: {error}")
    elif choice == 3:
        try:
            print(dict)
            search_by_key = input("Enter a key to search: ")
            if search_by_key in dict:
                print(f"Item found! {search_by_key} : {dict[search_by_key]}")
        except ValueError as error:
            print(f"Error: {error}")
        except Exception as error:
            print(f"Error: {error}")   
    elif choice == 4:
        try:
            print(dict)
            delete_by_key = input("Enter a key to delete: ")
            removed_value = dict.pop(delete_by_key)
        except ValueError as error:
            print(f"Error: {error}")
        except Exception as error:
            print(f"Error: {error}")   