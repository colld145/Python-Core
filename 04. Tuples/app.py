import random

"""Task 1"""

# list = []
# for i in range(10):
#     list.append(random.randint(1, 10))
# print(list)

# j = 1

# for i in range(len(list)):
#     for j in range(len(list)):
#         if list[j] > list[i]:
#             temp = list[i]
#             list[i] = list[j]
#             list[j] = temp

# print(list)


"""Task 2"""

# list = []
# for i in range(10):
#     list.append(random.randint(1, 10))
# print(list)

# set = {0}
# set.clear()

# for number in list:
#     set.add(number)
# print(set)


"""Task 3"""

list = []
for i in range(10):
    list.append(random.randint(1, 10))

print(list)

for number in list:
    if not number % 2 == 0:
        print(f"First unpaired number: {number}")
        break
