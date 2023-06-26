# def sum(a, b):
#     return a + b

# result = sum(5, 10)

# print(result)

# ---------------------------------------

# def test(a, b):
#     print(f"{a} + {b} = {a + b}")

# test(5,10)

# ---------------------------------------

# def plus(*numbers):
#     sum = 0
#     for number in numbers:
#         sum += number
#     return sum

# print(plus(2,65,6,7,65))


# ---------------------------------------

"""Напишіть функцію, що обчислює суму елементів списку цілих. Список передається як параметр."""

# def sum_list(list):
#     sum = 0
#     for number in list:
#         sum += number
#     return sum

# list = [1,43,34,12,6,3]
# print(sum_list(list))

"""Напишіть функцію для знаходження максимуму в списку цілих. Список передається як параметр."""

# def max_number(list):
#     list.sort()
#     return(list[-1])

# list = [1,5,7,8,1,2]

# print(max_number(list))

"""Напишіть функцію, що визначає кількість парних, непарних, додатних, від'ємних 
елементів списку цілих. Список передається як параметр."""

# def init_numbers(list):
#     pair_numbers = 0
#     unpair_numbers = 0
#     plus_numbers = 0
#     minus_numbers = 0
#     for number in list:
#         if number % 2 == 0:
#             pair_numbers += 1
#         if number % 3 == 0 or number == 1:
#             unpair_numbers += 1
#         if number > 0:
#             plus_numbers += 1
#         if number < 0:
#             minus_numbers += 1
#     print(f"Pair numbers = {pair_numbers}, Unpair numbers = {unpair_numbers}, Plus numbers = {plus_numbers}, Minus numbers = {minus_numbers}")

# list = [1, 24, -2, 13, -5, 6]

# init_numbers(list)

"""Напишіть функцію, що перевертає вміст списку цілих."""

# def reverse_list(list):
#     list.reverse()
#     return list

# list = [6,1,5,7,1,8,2,10]

# print(reverse_list(list))

"""Напишіть функцію, яка шукає деяке число у списку цілих."""

# def find_number(list, number):
#     return list.index(number)

# list = [6,1,5,7,1,8,2]
# number = 7
# print(find_number(list, number))

"""6. Написати функцію, яка обчислює вартість поїздки на автомобілі на дачу 
(туди і назад). Вхідними даними є: відстань до дачі (км); кількість бензину, 
яку споживає автомобіль на 100 км пробігу; ціна одного літру бензину. 
Дані для розрахунків вводяться користувачем."""

# def journey_cost(distance, gasoline, gas_cost):
#     return ((distance / 100 * gasoline) * 2) * gas_cost

# distance = int(input("Enter a distance (km): "))
# gasoline = int(input("Enter a gasoline (/100 km): "))
# gas_cost = int(input("Enter a gas cost: "))

# print(f"Journey cost = {journey_cost(distance, gasoline, gas_cost)} UAH")

# journey_cost = lambda distance, gasoline, gas_cost: ((distance / 100 * gasoline) * 2) * gas_cost
# print(journey_cost(distance, gasoline, gas_cost))

"""7. Написати функцію, яка отримує відстань, яку пробіг спортсмен та час пробігу 
і повертає швидкість спортсмена. Відстань та час пробігу вводяться користувачем"""

# speed = lambda distance, time: (distance // 1000) // (time // 3600)

# distance = int(input("Enter a distance (m): "))
# time = int(input("Enter a time (s): "))

# print(f"Speed = {speed(distance, time)} km/h")

"""8.Написати калькулятор, робота якого буде основана на функціях. 
Введення цифр та вибір математичної операції виконати в діалоговому стилі 
(запитати у користувача, вивести меню). У програмі передбачити уникнення
 помилок (ділення на нуль і т.д.). Фантазія та «дизайн» меню – ціниться та вітається!!!
Примітка! Кожна арифметична операція описується окремою функцією. 
Побудова самого меню також винесена в окрему функцію."""



# exit = False
# def plus(a, b):
#     return a + b

# def minus(a, b):
#     return a - b

# def multipl(a, b):
#     return a * b

# def divide(a, b):
#     return a / b

# def menu():
#     number1 = input("Enter a number: ")
#     operation = input("Enter an operation: ")
#     number2 = int(input("Enter a number: "))
#     print()
#     return [number1, operation, number2]


# while not exit:
#     menu()
#     number1, operation, number2 = menu()
#     if number1 == "exit":
#         break
#     number1 = int(number1)
#     if operation == "+":
#         print(f"{number1} + {number2} = {plus(number1, number2)}")
#     elif operation == "-":
#         print(f"{number1} - {number2} = {minus(number1, number2)}")
#     elif operation == "*" and number1 != 0 and number2 != 0:
#         print(f"{number1} * {number2} = {multipl(number1, number2)}")
#     elif operation == "/" and number1 != 0 and number2 != 0:
#         print(f"{number1} / {number2} = {divide(number1, number2)}")
#     else:
#         print("Error!")

"""9. Написати наступні функції, які в якості параметра приймають одновимірний масив і
 його розмірністю. Перевірити роботу функції для одновимірних масивів довжини 10 та довжини 7.

функцію Fill(), яка заповнює одновимірний масив випадковими значеннями в діапазоні [-12..20]

шаблонну функцію Print(), яка виводить елементи масиву на екран. Примітка! Протестувати дану
 функцію на масивах типу int, double, char

функцію, яка повертає кількість відємних елементів масиву

перевантажені функції:
- для знаходження середнього арифметичного елементів масиву
- для знаходження максимального елемента масиву в проміжку (між двома вказаними індексами)"""
import random
list = []
size = 10

def fill(list, size):
    for i in range(size):
        list.append(round(((random.uniform(-12, 20))), 2))

def minus_numbers(list):
    minus_number = 0
    for item in list:
        if item < 0:
            minus_number += 1
    return minus_number

def average_list(list):
    average = 0
    for item in list:
        average += item
    average = average // len(list)
    return average

def average_list_in_range(list, start, end):
    average = 0
    for item in list[start:end]:
        average += item
    average = average // len(list)
    return average
fill(list, size)
print(list)
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
print(f"Average number of the list in the range between {start} and {end}: {average_list_in_range(list, start, end)}")
print(f"Minus numbers in the list: {minus_numbers(list)}")
print(f"Average number of the list: {average_list(list)}")

