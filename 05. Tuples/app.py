# lang = ("C++", "Python", "JavaScript", "C#", "Go", "C++")

# print(len(lang))
# print(lang)

# fruits = ("Apple", "Banana", "Orange", "Cherry")
# print(f"Type: {type(fruits)}\nLength: {len(fruits)}")

# print("Banana" in fruits)
# del fruits
# print(fruits)

# fruits = {"Apple", "Banana", "Orange", "Cherry"}
# print(f"Type: {type(fruits)}\nLength: {len(fruits)}")
# fruits.add("Lemon")
# fruits.add("Lemon")
# fruits.add("Lemon")
# # fruits.pop()
# fruits.remove("Lemon")
# print(fruits)
# print("Lemon" in fruits)

# ---------------------------------------------------------------------------

# print(text[::-1])

# text = input("Enter the text: ")
# text = text.split()
# text.reverse()
# print(text)

"""Користувач вводить із клавіатури рядок і символ для пошуку. Порахуйте скільки разів у рядку зустрічається шуканий символ. 
Отримане число виведіть на екран."""

# text = input("Enter the text: ")
# entering_symbol = input("Enter the symbol: ")

# iterator = 0
# for symbol in text:
#     if entering_symbol in symbol:
#         iterator += 1

# print(f"Symbol '{entering_symbol}' in the text: {iterator}")

"""Task 4. 
У вас є два кортежі. Створіть третій кортеж, який є об'єднанням перших двох кортежів."""

# tuple1 = ("Apple", "Banana")
# tuple2 = ("Orange", "Lemon")
# tuple3 = (tuple1 + tuple2)

# print(tuple3)

"""Task5 

У вас є список елементів. Напишіть програму, щоб створити новий список, який містить тільки унікальні 
елементи зі старого списку."""

# import random

# list = []
# for i in range(10):
#     list.append(random.randint(1, 10))
# print(list)

# set = {0}
# set.clear()
# # for i in range(10):
# #     set.add(list[i])

# for number in list:
#     set.add(number)
# print(set)

"""У вас є дві множини. Напишіть програму, щоб знайти елементи, які є спільними для обох множин."""

# import random
# set1 = {0}
# set2 = {0}
# set3 = {0}
# set1.clear()
# set2.clear()
# set3.clear()
# for i in range(10):
#     set1.add(random.randint(1, 10))
#     set2.add(random.randint(1, 10))

# print(set1)
# print(set2)

# for i in set1:
#     for j in set2:
#         if i == j:
#             set3.add(i)

# for element in set1:
#     if element in set2:
#         set3.add(element)

# print(set3)

"""У вас є список чисел.
 Напишіть програму, щоб відсортувати цей список в порядку зростання без використання вбудованих функцій сортування."""

import random

list = []
for i in range(10):
    list.append(random.randint(1, 10))
print(list)

j = 1

for i in range(len(list)):
    for j in range(len(list)):
        if list[j] > list[i]:
            temp = list[i]
            list[i] = list[j]
            list[j] = temp

print(list)