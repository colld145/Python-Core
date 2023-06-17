text = input("Enter the text: ")
text = text.split()

reserved_words = input("Enter reserved words: ")
reserved_words = reserved_words.split()
print(reserved_words)

print("------Before-------")
print(text)

for i in range(len(text)):
    for j in range(len(reserved_words)):
        if text[i] == reserved_words[j]:
            text[i] = text[i].upper()
print("------After--------")
print(text)
