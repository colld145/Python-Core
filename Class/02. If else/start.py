# import random
# number = int(input("Enter day number: "))
# # number = random.randint(1, 7)
# if number == 1:
#     print("It's Monday.")
# elif number == 5:
#     print("It's Friday.")
# else:
#     print("ERROR!")
'''Користувач вводить із клавіатури два числа. Необхідно знайти суму чисел, різницю чисел, добуток чисел. Результат обчислень вивести на екран.'''

# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))

# print("Plus = ", number1 + number2, "Minus = ", number1 - number2, "Multipl = ", number1 * number2, "Division = ", number1 / number2)



'''Користувач вводить із клавіатури два числа. Необхідно знайти максимум із двох чисел і вивести його на екран.'''

# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))

# if number1 > number2:
#     print(f"{number1}")
# elif number1 < number2:
#     print(f"{number2} ")
# elif number1 == number2:
#     print("It's the same numbers.")





'''Користувач вводить із клавіатури два числа. Необхідно знайти мінімум із двох чисел і вивести його на екран.'''

# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))

# if number1 < number2:
#     print(f"{number1}")
# elif number1 > number2:
#     print(f"{number2} ")
# elif number1 == number2:
#     print("It's the same numbers.")




'''Користувач вводить із клавіатури два числа.
 Залежно від вибору користувача потрібно показати суму двох чисел, різницю двох чисел, середньоарифметичне або добуток двох чисел.'''

# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# operation = input("Enter an operation: ")
# result = 0
# if operation == '+':
#     result = number1 + number2
#     print(f"{number1} + {number2} = {result}")
# elif operation == '-':
#     result = number1 - number2
#     print(f"{number1} - {number2} = {result}")
# elif operation == '*':
#     result = number1 * number2
#     print(f"{number1} * {number2} = {result}")
# elif operation == '/':
#     result = number1 / number2
#     print(f"{number1} / {number2} = {result}")
# elif operation == 'average':
#     floatResult = float(result)
#     result = (number1 + number2) / 2
#     print(f"Average = {result}")

'''Користувач вводить із клавіатури довжину лінії. Потрібно відобразити на екрані горизонтальну лінію з * , вказаної довжини.

Наприклад, якщо було введено 7, тоді виведення на екран буде таким'''

# number = int(input("Enter the number: "))
# if number == 1:
#     print("*")
# elif number == 2:
#     print("**")
# elif number == 3:
#     print("***")
# elif number == 4:
#     print("****")
# elif number == 5:
#     print("*****")
# else:
#     print("ERRRRRRRRRRRROR!")


'''Користувач вводить із клавіатури довжину лінії та символ для заповнення лінії. Потрібно відобразити на екрані горизонтальну 
лінію із введеного символу, вказаної довжини.

Наприклад, якщо було введено 5 і &, тоді виведення на екран буде таким:'''

# symbol = input("Enter a symbol: ")
# number = int(input("Enter the number: "))

# if number == 1:
#     print(f"{symbol}")
# elif number == 2:
#     print(f"{symbol}{symbol}")
# elif number == 3:
#     print(f"{symbol}{symbol}{symbol}")
# elif number == 4:
#     print(f"{symbol}{symbol}{symbol}{symbol}")
# elif number == 5:
#     print(f"{symbol}{symbol}{symbol}{symbol}{symbol}")
# else:
#     print("ERRRRRRRRRRRROR!")

'''Користувач із клавіатури вводить кількість годин. Якщо отримане значення знаходиться в діапазоні від 0 до 6, 
потрібно вивести напис "Good Night", якщо в діапазоні від 6 до 13 — "Good Morning", якщо в діапазоні від 13 до 17 — "Good Day",
якщо в діапазоні від 17 до 0 — "Good Evening". Верхня межа діапазону не враховується. Наприклад, число 6 входить до діапазону
від 6 до 13.'''

time = int(input("Enter an hour: "))
if time >= 0 and time < 6:
    print("Good Night!")
elif time >= 6 and time < 13:
    print("Good Morning!")
elif time >= 13 and time < 17:
    print("Good Day!")
elif time >= 17 and time < 24:
    print("Good Evening!")
else:
    print("ERROR!")
