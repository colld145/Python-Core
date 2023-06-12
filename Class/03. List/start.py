# prog_lang = ["C#", "C++", "Python", "JavaScript", "Go", "Java"]
# print(type(prog_lang))
# print("============================= Append ==============================")
# prog_lang.append("TypeScript")
# print(prog_lang)
# print("============================= Remove ==============================")
# prog_lang.remove("TypeScript")
# print(prog_lang)
# print("============================= Insert ==============================")
# prog_lang.insert(2, "Rust")
# print(prog_lang)
# print("============================= pop =================================")
# prog_lang.pop(1)
# print(prog_lang)
# print("============================= Reverse =============================")
# prog_lang.reverse()
# print(prog_lang)
# print("============================= Sort ================================")
# prog_lang.sort()
# print(prog_lang)
# print("============================= Sort reverse ========================")
# prog_lang.sort(reverse=True)
# print(prog_lang)

# mix_list = [1, 64, -5, "Lemon", [54, ["Banana", False], "Apple"], True]
# print(mix_list[4][1][1])
# print(mix_list)
# print(len(mix_list[4][1]))
# print("============================= Reverse ========================")
# mix_list.reverse()
# # print("============================= Sort ===========================")
# # mix_list.sort() # Error
# print(mix_list)
# mix_list.extend(prog_lang)
# print(mix_list)
# print("\n---------------------------------------------\n")
# tmp_list = mix_list
# tmp_list = mix_list.copy()
# print(f"Mix list: {mix_list}\nTemp list: {tmp_list}")
# print("\n---------------------------------------------\n")
# tmp_list[0] = 2222222222
# print(f"Mix list: {mix_list}\nTemp list: {tmp_list}")

'''Користувач із клавіатури вводить елементи списку цілих. Необхідно порахувати суму всіх елементів та їхнє середньоарифметичне.
 Результати вивести на екран.'''
# list = [int(input("Enter number:")),int(input("Enter number:")),int(input("Enter number:")),int(input("Enter number:")),int(input("Enter number:"))]

# sum = list[0] + list[1] + list[2] + list[3] + list[4]
# print(f"Sum = {sum}")
# average = (list[0] + list[1] + list[2] + list[3] + list[4]) / len(list)
# print(f"Average = {average}")
# number = int(input("Enter number: "))
# list.append(number)
# print(list)

# ----------------------------------------------

# nums = []
# num1 = int(input("Enter the first number:"))
# nums.append(num1)
# num2 = int(input("Enter the second number:"))
# nums.append(num2)
# num3 = int(input("Enter the third number:"))
# nums.append(num3)

# print(nums)

# count = len(nums)
# print(f"Length = {count}")

# sum = nums[0] + nums[1] + nums[2]
# print(f"Sum = {sum}")
# avg = (nums[0] + nums[1] + nums[2]) / count
# print(f"Average = {avg}")

'''Користувач вводить із клавіатури час у секундах, що минув від початку дня. Залежно від вибору користувача потрібно порахувати скільки годин,
 хвилин і секунд залишилося до опівночі.'''

# time = int(input("Enter the time: "))
# operation = input("Enter an operation ('hour', 'min' or 'sec'):")
# if operation == 'hour':
#     hour = 24 - (time / 3600)
#     print(f"{hour} hours to midnight")
# elif operation == 'min':
#     min = 1440 - (time / 60)
#     print(f"{min} minutes to midnight")
# elif operation == 'sec':
#     sec = 86400 - time
#     print(f"{sec} seconds to midnight")

'''Завдання 1
Користувач вводить із клавіатури число. Необхідно перевірити його на парність і непарність. Якщо число парне, потрібно вивести на екран число
 і напис Even number. Якщо число непарне виведіть на екран число і напис Odd number.'''

# number = int(input("Enter a number: "))

# if number % 2 == 0:
#     print("Even number.")
# else:
#     print("Odd number.")

'''Завдання 2
Користувач вводить із клавіатури число. Необхідно перевірити його на кратність 7. Якщо число кратне, потрібно вивести на екран число
 і напис Number is a multiple of 7. Якщо число не кратне, виведіть на екран число і напис Number is not a multiple of 7.'''

# number = int(input("Enter a number: "))

# if number % 7 == 0:
#     print("Number is a multiple of 7.")
# else:
#     print("Number is not a multiple of 7.")

'''Завдання 3
Користувач вводить із клавіатури два числа. Необхідно знайти максимум із двох чисел і вивести його на екран.'''

# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))

# if number1 > number2:
#     print(f"{number1}")
# elif number1 < number2:
#     print(f"{number2} ")
# elif number1 == number2:
#     print("It's the same numbers.")

'''Завдання 4
Користувач вводить із клавіатури два числа. Необхідно знайти мінімум із двох чисел і вивести його на екран.'''

# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))

# if number1 < number2:
#     print(f"{number1}")
# elif number1 > number2:
#     print(f"{number2} ")
# elif number1 == number2:
#     print("It's the same numbers.")

'''Завдання 5
Користувач вводить із клавіатури два числа. Залежно від вибору користувача потрібно показати суму двох чисел, різницю двох чисел,
 середньоарифметичне або добуток двох чисел.'''

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

'''Завдання 6
Користувач вводить із клавіатури номер дня тижня (1-7). Необхідно вивести на екран назву дня тижня. Наприклад, якщо 1, то на
 екрані напис "понеділок", 2 — "вівторок" і т.д.'''

# day = int(input("Enter the day: "))

# if day == 1:
#     print("Monday.")
# elif day == 2:
#     print("Tuesday.")
# elif day == 3:
#     print("Wednesday.")
# elif day == 4:
#     print("Thursday.")
# elif day == 5:
#     print("Friday.")
# elif day == 6:
#     print("Saturday.")
# elif day == 7:
#     print("Sunday.")

'''Завдання 7
Користувач вводить із клавіатури номер місяця (1-12). Необхідно вивести на екран назву місяця. 
Наприклад, якщо 1, то на екрані напис "січень", 2 — "лютий" і т.д.'''

# month = int(input("Enter the day: "))

# if month == 1:
#     print("January.")
# elif month == 2:
#     print("February.")
# elif month == 3:
#     print("March.")
# elif month == 4:
#     print("April.")
# elif month == 5:
#     print("May.")
# elif month == 6:
#     print("June.")
# elif month == 7:
#     print("July.")
# elif month == 8:
#     print("August.")
# elif month == 9:
#     print("September.")
# elif month == 10:
#     print("October.")
# elif month == 11:
#     print("November.")
# elif month == 12:
#     print("December.")


'''Завдання 9
Користувач вводить два числа. Необхідно визначити, чи ці числа є рівними і, якщо ні, вивести їх на екран у порядку зростання.'''

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 == num2:
    print("Equal numbers.")
else:
    if num1 < num2:
        print(f"{num1}, {num2}")
    else:
        print(f"{num2}, {num1}")
