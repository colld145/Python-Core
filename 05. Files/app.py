# Task 1.
"""Користувач вводить з клавіатури назви файлів, 
доки він не введе слово "quit". Після завершення введення програма має 
об'єднати вміст усіх внесених назв файлів в один."""

# texts = []
# while True:
#     # We enter text1.txt and text2.txt
#     input_text = input("Enter a file name: ")
#     if input_text == 'quit':
#         break
#     file = open(f"{input_text}", 'r+')
#     text = file.read()
#     texts.append(text)
#     file.close()
#
# file = open('all_texts.txt', 'w')
# for item in texts:
#     file.write(f'{item}\n')
# file.close()


# Task 2.
"""Користувач вводить з клавіатури назви файлів, 
доки він не введе слово "quit". 
Після завершення введення програма має записати у підсумковий файл символи, 
які містяться у всіх внесених назвах файлів 
(символи мають бути у кожному файлі). """

symbols_lists = []
while True:
    input_text = input("Enter a file name: ") # We enter symbols1.txt, symbols2.txt and symbols3.txt
    if input_text == 'quit':
        break
    file = open(f"{input_text}", 'r+')
    symbols = file.read()
    symbols.split()
    symbols_lists.append(symbols)
    file.close()

common_symbols = []
for i in symbols_lists:
    for char in symbols_lists[0]:
        is_common = True

        for file_name in symbols_lists[1:]:
            if char not in file_name:
                is_common = False
                break

        if is_common:
            common_symbols.append(char)

temp_list = []
for char in common_symbols:
    if char not in temp_list:
        temp_list.append(char)
common_symbols = temp_list.copy()
common_symbols.remove(' ')
file = open('common_symbols.txt', 'w')
for char in common_symbols:
    file.write(f'{char} ')
file.close()