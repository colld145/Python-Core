"""Task 3
Напишіть програму, яка приймає рядок і намагається перетворити його на число.

Обробіть виняток, що виникає при неможливості перетворення, і виведіть повідомлення про помилку."""

# try:
#     digit_str = input("Enter a digit: ")
#     digit_int = int(digit_str)
#     print(f"Digit: {digit_int}, Type: {type(digit_int)}")
# except ValueError as error:
#     print(f"Error: {error}")
# except Exception as error:
#     print(f"Error: {error}")

"""Task 4
Реалізуйте третє завдання через функцію. 
Функція повинна приймати рядок і відображати результат перетворення на екран. 
Створіть дві версії реалізації функції:

Перша версія не обробляє виняток усередині функції. Уся обробка знаходиться зовні;
Друга версія обробляє виняток усередині функції."""

################################################################
# The first version


# def str_to_int(digit):
#     digit_int = int(digit)
#     return digit_int
#
#
# try:
#     digit_str = input("Enter a digit: ")
#     digit_int = str_to_int(digit_str)
#     print(f"Digit: {digit_int}, Type: {type(digit_int)}")
# except ValueError as error:
#     print(f"Error: {error}")
# except Exception as error:
#     print(f"Error: {error}")

###############################################################
# The second version


def str_to_int(digit):
    try:
        digit_int = int(digit)
        return digit_int
    except ValueError as error:
        print(f"Error: {error}")
    except Exception as error:
        print(f"Error: {error}")


digit_str = input("Enter a digit: ")
digit_int = str_to_int(digit_str)

if digit_int:
    print(f"Digit: {digit_int}, Type: {type(digit_int)}")