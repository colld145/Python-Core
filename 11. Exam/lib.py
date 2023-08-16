# ===============================================
# Application's Library


database = []


def menu():
    while True:
        print("1. Add item\n2. Print items\n3. Edit item\n4. Remove item\n5. Search item\n\n0. Exit\n")
        choice = input("Enter a choice: ")
        if choice == "1":
            add_item(database)
        elif choice == "2":
            print_all_items(database)
        elif choice == "3":
            edit_item(database)
        elif choice == "4":
            remove_item(database)
        elif choice == "5":
            search_item(database)
        elif choice == "0":
            break
    

def add_item(database):
    number = len(database) + 1
    name = input("Enter an item name: ")
    producer = input("Enter an item producer: ")
    price = input("Enter an item price: ")
    item = [number, name, producer, price]
    database.append(item)


def print_all_items(database):
    for item in database:
        print_item(item)


def print_item(item):
    print(f"{item[0]}. Name: {item[1]}\nProducer: {item[2]}\nPrice: {item[3]}\n")


def edit_item(database):
    print_all_items(database)
    choice = input("Enter a number of item to edit: ")
    for item in database:
        if item[0] == choice:
            editing = input("1. Name\n2. Producer\n3. Price\n\nEnter an element to edit: ")
            if editing == "1":
                new_name = input("Enter a new name: ")
                item[1] = new_name
            elif editing == "2":
                new_producer = input("Enter a new producer: ")
                item[2] = new_producer
            elif editing == "3":
                new_price = input("Enter a new price: ")
                item[3] = new_price


def remove_item(database):
    print_all_items(database)
    deleting = int(input("Enter a number of item to remove: "))
    i = 1
    for item in database:
        if i == deleting:
            database.remove(item)
        i+=1


def search_item(database):
    search_type = input("1. Search by name\n2. Search by producer\n3. Search by price\n\nEnter a type of search: ")
    i = 1
    if search_type == "1":
        search_name = input("Enter a name for search: ")
        print("\n==================\nRESULT: ")
        for item in database:
            if search_name in item:
                print(f"{i}. Name: {item[0]}\nProducer: {item[1]}\nPrice: {item[2]}\n")
            i+=1