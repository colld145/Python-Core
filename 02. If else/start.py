"""Task 1
Користувач вводить із клавіатури три числа. Залежно від вибору користувача програма виводить на екран
суму трьох чисел або добуток трьох чисел."""

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
# operation = input("Enter an operation ('+' or '*'): ")
# result = 0
# if operation == '+':
#     result = num1 + num2 + num3
#     print(f"{num1} + {num2} + {num3} = {result}")
# elif operation == '*':
#     result = num1 * num2 * num3
#     print(f"{num1} * {num2} * {num3} = {result}")

# ------------------------------------------------------

"""Task 2
Користувач вводить із клавіатури три числа. Залежно від вибору користувача програма виводить на екран 
максимум із трьох, мінімум із трьох або середньоарифметичне трьох чисел."""

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
# operation = input("Enter an operation ('max', 'min' or 'avg'): ")

# if operation == 'max':
#     max = num1
#     if num2 > max:
#         max = num2
#     if num3 > max:
#         max = num3
#     print(f"Max number = {max}")
# elif operation == 'min':
#     min = num1
#     if num2 < min:
#         min = num2
#     if num3 < min:
#         min = num3
#     print(f"Max number = {min}")
# elif operation == 'avg':
#     average = (num1 + num2 + num3) / 3
#     print(f"Average = {average}")

# ------------------------------------------------------------------

"""Task 3
Користувач вводить із клавіатури кількість метрів. Залежно від вибору користувача програма 
конвертує метри в милі, дюйми або ярди."""

meters = int(input("Enter meters: "))
operation = input("Enter an operation ('miles', 'inches' or 'yards'): ")

if operation == "miles":
    miles = meters / 1609
    print(f"Meters to miles: {meters} = {miles}")
elif operation == "inches":
    inches = meters * 39.37
    print(f"Meters to inches: {meters} = {inches}")
elif operation == "yards":
    yards = meters * 1.094
    print(f"Meters to yards: {meters} = {yards}")
