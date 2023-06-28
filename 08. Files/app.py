# path = '08. Files/file.txt'
# files = open(path, 'w')

# print(f"files: {files}\nName: {files.name}\nIs closed: {files.closed}\nMode: {files.mode}")

# files.write("Hello, World!\n")
# files.write("This is a test.\n")
# files.close()

# files = open(path, 'a')
# files.write("Python the best!\n")
# files.close()

# files = open(path, 'r+')
# text = files.read()
# print(text)
# files.close()

"""Task 1. Маємо текстовий файл. Створіть новий файл та перепишіть з вихідного файлу всі слова, 
що складаються не менше, ніж із семи літер."""

file = open('08. Files/data.txt', 'w')
file.write("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Sed aliquam lorem a tellus egestas, sit amet rutrum nisi dapibus. 
Vestibulum dignissim nisl tortor, id consequat libero rutrum sit amet. 
Phasellus molestie posuere mi, eu congue quam finibus luctus. In vulputate
quis nisi porta laoreet. Donec eleifend consectetur risus, a 
rhoncus libero mollis lobortis. Etiam bibendum imperdiet quam
nec rhoncus. Duis a erat nec arcu molestie tempor ac sed mi.
Nullam faucibus suscipit tortor at gravida. Phasellus congue vel
est et aliquam. Integer tincidunt justo et diam dictum, bibendum
consectetur erat laoreet. Curabitur sit amet lorem ut orci ornare
convallis. Proin hendrerit urna ac quam pharetra, id porta metus
varius. Aenean libero mauris, scelerisque ut pretium a, vehicula
sit amet orci. Mauris vestibulum velit turpis, eu interdum lorem
ullamcorper in. Ut magna sapien, ullamcorper vel nibh et, 
convallis porta libero.""")
file.close()

# file = open('08. Files/data.txt', 'r+')
# text = file.read()
# text = text.split()
# print(text)
# text2 = []
# for word in text:
#     if len(word) > 7:
#         text2.append(word)
# file.close()

# file = open('08. Files/data_backup.txt', 'w')
# for word in text2:
#     file.write(f"{word}\n")
# file.close()

"""Task 2. Маємо текстовий файл. Перепишіть його рядки в інший файл. Порядок рядків у 
другому файлі має бути зворотним до порядку рядків у заданому файлі."""

# file = open('08. Files/data.txt', 'r+')
# text = []
# for line in file:
#     text.append(line)
# text.reverse()
# print(text)
# file.close()

# file = open('08. Files/data2.txt', 'w')
# for line in text:
#     file.write(line)

# file.close()

"""Task 3. Маємо текстовий файл. Підрахуйте кількість слів, що починаються з символу,
 який задає користувач."""

# file = open('08. Files/data.txt', 'r+')
# text = file.read()
# text = text.split()
# file.close()
# print(text)
# text2 = []
# counter = 0
# input_symbol = input("Enter the symbol: ")
# for word in text:
#     if word[0] == input_symbol:
#         text2.append(word)
#         counter += 1
# print(text2)
# print(f"Words with the first symbol '{input_symbol}': {counter}")


"""Task 4. Маємо текстовий файл. Перепишіть до іншого файлу всі його рядки замінюючи
 в них символ * на символ &, і навпаки."""

# file = open('08. Files/data3.txt', 'r+')
# text = []
# for line in file:
#     text.append(line)
# file.close()

# file = open('08. Files/data4.txt', 'w')
# for line in text:
#     if '*' in line:
#         line.replace('*', '&')
#     elif '&' in line:
#         line.replace('&', '*')
#     file.write(line)

# file.close()

"""Task 5. Маємо текстовий файл. Підрахуйте кількість символів у ньому."""

# file = open('08. Files/data.txt', 'r+')
# text = file.read()
# file.close()
# print(len(text))

"""Task 6. Маємо текстовий файл. Підрахуйте кількість рядків у ньому."""

# file = open('08. Files/data.txt', 'r+')
# text = []
# for line in file:
#     text.append(line)
# file.close()

# print(len(text))

"""Task 7. Маємо текстовий файл. Створіть новий файл, прибравши з нього всі неприйнятні слова.
 Список неприйнятних слів міститься в іншому файлі. """

file = open('08. Files/text.txt', 'r+')
text = file.read()
file.close()

file = open('08. Files/langs.txt', 'r+')
langs = file.read().split(' ')
file.close()

for word in langs:
    text = text.replace(word, "*********")
print(text)

file = open('08. Files/new_text.txt', 'w')
file.write(text)
file.close()

"""Task 8. Напишіть програму транслітерації з української на англійську, та навпаки. 
Візьміть дані для транслітерації з одного файлу і запишіть їх до іншого. 
Мовну пару встановлює користувач у меню."""

