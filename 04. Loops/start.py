people = ['John', 'Adam', 'Sarah', 'Paul', 'Eva']

# for person in people:
#     print(person)

# for person in people:
#     if person == 'Sarah':
#         print(person)
#         break
    
# for i in range(len(people)):
#     print(people[i])

# print(people.index("Sarah"))
# count = 0
# while count <= 10:
#     print(f"Count = {count}")
#     count += 1

# Показати таблицю множення для числа, введеного користувачем. Наприклад, якщо користувач вводить число 7, потрібно показати:

# number = int(input("Enter a number:"))
# counter = 1
# while counter <= 10:
#     print(f"{number} * {counter} = {number * counter}")
#     counter += 1

# counter = 1
# number = 1
# while counter <= 10:
#     iterator = 1
#     while iterator <= 10:
#         print(f"{number} * {iterator} = {number * iterator}")
#         iterator +=1
#     print("-------------")
#     number +=1
#     counter+=1

# Написати програму — конвертер валют. Реалізувати спілкування з користувачем через меню.


# exit = False
# while not exit:
#     cash = int(input("Enter cash:"))
#     choice = int(input(f"Buy 36.57\tSell 37.45\n1. Buy\n2. Sell\n0. Exit\nEnter choice:"))
#     if choice == 1:
#         import os
#         os.system('cls')
#         print(f"Your deal: {cash} = {int(cash / 36.57)} $")
#     elif choice == 2:
#         import os
#         os.system('cls')
#         print(f"Your deal: {cash} = {int(cash * 37.45)} UAH")
#     elif choice == 0:
#         exit = True
#     else:
#         import os
#         os.system('cls')
#         print("Wrong choice!")

'''Користувач вводить із клавіатури дві межі діапазону та число. Якщо число не потрапляє в діапазон, 
програма просить користувача повторно ввести число і так доти, доки він не введе число правильно. 
Програма відображає всі числа діапазону, виділяючи число знаками оклику. Наприклад:
1 2 3 !4! 5 6 7'''

# num1 = int(input("Enter the first range number:"))
# num2 = int(input("Enter the second range number:"))

# exit = False

# while not exit:
#     number = int(input("Enter the number:"))
#     if number < num1 or number > num2:
#         print("Error!")
#     else:
#         tempExit = False
#         counter = num1
#         while not tempExit:
#             if counter == num2:
#                 tempExit = True
#             if counter == number:
#                 print(f"!{number}!")
#                 counter+=1
#             else:
#                 print(counter)
#                 counter += 1

'''Написати гру "Вгадай число". Програма загадує число в діапазоні від 1 до 500. Користувач намагається його вгадати.
 Після кожної спроби програма видає підказки: більше чи менше його число, ніж загадане. 
 Наприкінці програма видає статистику: за скільки спроб вгадано число, скільки часу це зайняло. 
 Передбачити вихід по 0 у разі, якщо користувачеві набридло вгадувати число.'''


# exit = False
# import random
# number = random.randint(1, 10)
# while not exit:
#     my_try = int(input("Enter the number:"))
#     if my_try > number:
#         print(f"{my_try} is bigger. Try again.")
#     elif my_try < number:
#         print(f"{my_try} is smaller. Try again.")
#     elif my_try == number:
#         print(f"You win!")
#         exit = True

'''Користувач із клавіатури вводить елементи списку цілих і деяке число. 
Необхідно порахувати скільки разів дане число присутнє в списку. Результат вивести на екран.'''

import random
list = []
for i in range(10):
    list.append(random.randint(1, 10))
print(list)

number = int(input("Enter the number: "))
counter = 0

for i in range(len(list)):
    if list[i] == number:
        counter+=1

print(f"Number {number} in list {counter} times.")