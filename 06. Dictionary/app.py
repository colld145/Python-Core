# person = {
#     "first_name" : "name",
#     "last_name" : "surname",
#     "age" : 24
# }

# print (f"Type: {type(person)}\nName: {person['FirstName']}\nSurname: {person['LastName']}\nAge: {person['Age']}")

# person2 = person.copy()
# person2['age'] = 30
# print(person["age"])

# people_list = [person, person2]

# print(people_list)
# print(people_list[0]['age'])
# print("====================")
# print(people_list[1]['age'])

# for item in people_list:
#     print(item['age'])

"""Task 1:
 Лічильник слів Напишіть програму, яка приймає рядок від користувача і повертає словник, 
в якому ключі - це слова з рядка, а значення - кількість входжень кожного слова. Приклад: Вхід:
 "я люблю програмування, але програмування не завжди легке" Вихід: {'я': 1, 'люблю': 1, 'програмування': 2, 'але': 1,
   'не': 1, 'завжди': 1, 'легке': 1}"""

# text = input("Enter the text: ")
# text = text.split()

# dict = {}

# for word in text:
#     if word in dict:
#         dict[word] += 1
#     else:
#         dict[word] = 1

# print(dict)

"""Задача про суму чисел: Напишіть програму, яка приймає від користувача цілі числа, поки він не введе 0,
 і обчислює суму всіх введених чисел. Виведіть цю суму на екран."""

# exit = False
# sum = 0
# while not exit:
#     input_number = int(input("Enter a number: "))
#     if input_number == 0:
#         exit = True
#     else:
#         sum += input_number

# print(f"Sum = {sum}")

"""2. Задача про визначення простого числа: Напишіть програму, яка приймає від користувача ціле число і визначає,
 чи є воно простим. Просте число - це натуральне число, яке більше 1 і ділиться лише на 1 і на себе без залишку.
   Виведіть відповідне повідомлення на екран."""

# number = int(input("Enter a number: "))

# if number > 1 and number % 1 == 0 and number % number == 0:
#     print(f"{number} is simple number")

"""3. Напишіть програму, яка приймає від користувача список цілих чисел і сортує його за зростанням без 
використання вбудованих функцій сортування. Виведіть відсортований список на екран."""

# import random

# list = []
# for i in range(10):
#     list.append(random.randint(1, 10))

# print("1. Sort to bigger\n2. Sort to smaller")
# choice = input("Enter a choice: ")
# print("=====Before====")
# print(list)
# j = 1
# if choice == "1":
#         for i in range(len(list)):
#             for j in range(len(list)):
#                 if list[i] < list[j]:
#                     temp = list[i]
#                     list[i] = list[j]
#                     list[j] = temp

# elif choice == "2":
#         for i in range(len(list)):
#             for j in range(len(list)):
#                 if list[i] > list[j]:
#                     temp = list[i]
#                     list[i] = list[j]
#                     list[j] = temp
        
# print("=====After=====")
# print(list)
     



"""Напишіть програму, яка об'єднує два словники, додаючи значення з одного словника до значень в 
іншому словнику для спільних ключів. Якщо ключ відсутній в одному словнику, просто додайте його
 зі значенням, якщо він присутній в іншому словнику. Приклад: Вхід: словник1 = {'а': 1, 'б': 2, 'в': 3}
   словник2 = {'б': 3, 'в': 4, 'г': 5} Вихід: {'а': 1, 'б': 5, 'в': 7, 'г': 5}"""

dict1 = {
    'a' : 1,
    'b' : 2,
    'c' : 3
         }

dict2 = {
    'b' : 3,
    'c' : 4,
    'd' : 5
         }

print(dict1)
print(dict2)

for item in dict2:
    if item in dict1:
        dict2[item] = dict2[item] + dict1[item]
    else:
        dict2[item] += dict1[item]
print(dict2)
