# ===============================================
# Application's Library


import csv
import time
import os
from datetime import date
from tabulate import tabulate


def read_file():
    try:
        file = open("database.csv", "r")
        csvreader = csv.reader(file)
        return csvreader
        file.close()
    except Exception as error:
        print(f"Error: {error}")


def write_file(database):
    try:
        file = open("database.csv", "w")
        for row in database:
            for item in row:
                if item == row[-1]:
                    file.writelines(f"{item}")
                    break
                file.writelines(f"{item},")
            file.writelines("\n")
        file.close()
        return print("File saved successfully!")
    except Exception as error:
        print(f"Error: {error}")


database = []
csvreader = read_file()


def create_database(csvreader, database):
    for item in csvreader:
        item[3] = int(item[3]) # Change price data type
        database.append(item)


def menu():
    create_database(csvreader, database)
    exit = False
    while not exit:
        numbering(database)
        print("\n. . .")
        print("\t- 1. Add item -\n\t- 2. Print items -\n\t- 3. Edit item -\n\t- 4. Remove item -\n\t- 5. Search item -\n\n\t- 0. Exit -\n")
        choice = input(">> ")
        if choice == "1":
            add_item(database)
        elif choice == "2":
            print_database(database)
        elif choice == "3":
            print_database(database)
            search = input("Enter a number of item to edit: ")
            edit_item(database, search)
        elif choice == "4":
            # It's going to be print and search!!
            remove_item(database)
        elif choice == "5":
            search_item(database)
        elif choice == "0":
            exit = True
    
    write_file(database)
    

def add_item(database):
    i = 0
    for item in database:
        i+=1
    number = str(i+1)
    name = input("Enter an item name: ")
    producer = input("Enter an item producer: ")
    price = int(input("Enter an item price: "))
    product_group = input("Enter an item product group: ")
    come_date = date.today()
    life_term = input("Enter an item life term: ")
    item = [number, name, producer, price, product_group, come_date, life_term]
    database.append(item)


def print_database(item):
    print(tabulate(item, headers=["№", "Name", "Producer", "Price", "Group", "Come date", "Life term"]))


def edit_item(database, choice):
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
    print_database(database)
    deleting = int(input("Enter a number of item to remove: "))
    i = 1
    for item in database:
        if i == deleting:
            database.remove(item)
        i+=1


def numbering(database):
    i = 1
    for item in database:
        item[0] = i
        i+=1


def search_by_name(database, search_name):
    search_list = []
    for item in database:
            if search_name in item:
                search_list.append(item)
    return search_list


def search_by_producer(database, search_producer):
    search_list = []
    for item in database:
        if search_producer in item:
            search_list.append(item)
    return search_list


def search_by_price(database, start, finish):
    search_list = []
    for item in database:
        if item[3] >= start and item[3] <= finish:
             search_list.append(item)
    return search_list


def search_item(database):
    search_type = input("1. Search by name\n2. Search by producer\n3. Search by price\n\nEnter a type of search: ")
    if search_type == "1":
        search_name = input("Enter a name to search: ")
        print(f"\n*** Search by Name '{search_name}' - RESULT: ")
        print_database(search_by_name(database, search_name))
    elif search_type == "2":
        search_producer = input("Enter a producer to search: ")
        print(f"\n*** Search by Producer '{search_producer}' - RESULT: ")
        print_database(search_by_producer(database, search_producer))
    elif search_type == "3":
        start = int(input("Enter a start of range: "))
        finish = int(input("Enter a finish of range: "))
        print(f"\n*** Search by Price '{start} - {finish}' - RESULT: ")
        print_database(search_by_price(database, start, finish))


