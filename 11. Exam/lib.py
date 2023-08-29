# ===============================================
# Application's Library


import csv
import time
import os
from datetime import date, timedelta, datetime
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


def create_database():
    csvreader = read_file()
    database = []
    for item in csvreader:
        item[3] = int(item[3])  # Change price data type
        database.append(item)
    return database


def sort_by_price(item):
    return item[3]


def sort_by_group(item):
    return item[4]


def add_item(database):
    i = 0
    for item in database:
        i += 1
    number = str(i + 1)
    name = input("Enter an item name: ")
    producer = input("Enter an item producer: ")
    price = int(input("Enter an item price: "))
    product_group = input("Enter an item product group: ")
    come_date = date.today()
    life_term_input = input("Enter an item life term: ")
    life_term_input = life_term_input.split()
    life_term_number = int(life_term_input[0])
    if life_term_input[1] == "day" or life_term_input[1] == "days":
        life_term = come_date
        life_term = life_term + timedelta(days=life_term_number)
    if life_term_input[1] == "week" or life_term_input[1] == "weeks":
        life_term = come_date
        life_term = life_term + timedelta(weeks=life_term_number)
    if life_term_input[1] == "month" or life_term_input[1] == "months":
        life_term_number = life_term_number * 30
        life_term = come_date
        for i in range(life_term_number):
            life_term = life_term + timedelta(days=1)

    item = [number, name, producer, price, product_group, come_date, life_term]
    database.append(item)


def print_database(item):
    print(
        tabulate(
            item,
            headers=[
                "№",
                "Name",
                "Producer",
                "Price",
                "Group",
                "Come date",
                "Life term",
            ],
        )
    )


def edit_item(database, choice):
    for item in database:
        if item[0] == choice:
            editing = input(
                "1. Name\n2. Producer\n3. Price\n4. Group\n\nEnter an element to edit: "
            )
            if editing == "1":
                new_name = input("Enter a new name: ")
                item[1] = new_name
            elif editing == "2":
                new_producer = input("Enter a new producer: ")
                item[2] = new_producer
            elif editing == "3":
                new_price = input("Enter a new price: ")
                item[3] = new_price
            elif editing == "4":
                new_group = input("Enter a new group: ")
                item[4] = new_group


def remove_item(database, choice):
    i = 1
    for item in database:
        if i == choice:
            database.remove(item)
        i += 1


def numbering(database):
    i = 1
    for item in database:
        item[0] = i
        i += 1


def search_by_name(database, search_item):
    search_list = []
    was_found = False
    for item in database:
        for element in item[1].split():
            if search_item.lower() in element:
                search_list.append(item)
                was_found = True
                break
    if not was_found:
        item = ["-", "ITEM", "NOT", "FOUND", "-", "-", "-"]
        search_list.append(item)
    return search_list


def search_by_producer(database, search_item):
    search_list = []
    was_found = False
    for item in database:
        for element in item[2].split():
            if search_item.lower() in element:
                search_list.append(item)
                was_found = True
                break
    if not was_found:
        item = ["-", "ITEM", "NOT", "FOUND", "-", "-", "-"]
        search_list.append(item)
    return search_list


def search_by_group(database, search_item):
    search_list = []
    was_found = False
    for item in database:
        for element in item[4].split():
            if search_item.lower() in element:
                search_list.append(item)
                was_found = True
                break
    if not was_found:
        item = ["-", "ITEM", "NOT", "FOUND", "-", "-", "-"]
        search_list.append(item)
    return search_list


def search_by_price(database, start, finish):
    search_list = []
    was_found = False
    for item in database:
        if item[3] >= start and item[3] <= finish:
            search_list.append(item)
            was_found = True
    if not was_found:
        item = ["-", "ITEM", "NOT", "FOUND", "-", "-", "-"]
        search_list.append(item)
    return search_list


def search_by_date(database, date):
    search_list = []
    was_found = False
    for item in database:
        if item[5] == date:
            search_list.append(item)
            was_found = True
    if not was_found:
        item = ["-", "ITEM", "NOT", "FOUND", "-", "-", "-"]
        search_list.append(item)
    return search_list


def search_by_life_term(database, date):
    search_list = []
    was_found = False
    for item in database:
        if item[6] < date:
            search_list.append(item)
            was_found = True
    if not was_found:
        item = ["-", "ITEM", "NOT", "FOUND", "-", "-", "-"]
        search_list.append(item)
    return search_list


today = date.today()


def search_item(database, choice):
    if choice == "1":
        search_name = input("Enter a name to search: ")
        print(f"\n*** Search by Name '{search_name}' - RESULT: ")
        print_database(search_by_name(database, search_name))
    elif choice == "2":
        search_producer = input("Enter a producer to search: ")
        print(f"\n*** Search by Producer '{search_producer}' - RESULT: ")
        print_database(search_by_producer(database, search_producer))
    elif choice == "3":
        start = int(input("Enter a start of range (min): "))
        finish = int(input("Enter a finish of range (max): "))
        print(f"\n*** Search by Price '{start} - {finish}' - RESULT: ")
        print_database(search_by_price(database, start, finish))
    elif choice == "4":
        search_group = input("Enter a group to search: ")
        print(f"\n*** Search by Group '{search_group}' - RESULT: ")
        print_database(search_by_group(database, search_group))
    elif choice == "5":
        search_come_date = input(
            "Enter a come date to search (format: 'DD' 'MM' 'YYYY'): "
        )
        search_come_date = search_come_date.split(" ")
        date = f"{search_come_date[2]}-{search_come_date[1]}-{search_come_date[0]}"
        print(f"\n*** Search by Come date '{date}' - RESULT: ")
        print_database(search_by_date(database, date))
    elif choice == "6":
        deadline_input = input(
            "Enter a deadline (format: 'NUMBER' 'days' or weeks' or 'months'): "
        )
        deadline_input = deadline_input.split()
        deadline_number = int(deadline_input[0])
        if deadline_input[1] == "day" or deadline_input[1] == "days":
            deadline_date = today + timedelta(days=deadline_number)
        elif deadline_input[1] == "week" or deadline_input[1] == "weeks":
            deadline_date = today + timedelta(weeks=deadline_number)
        elif deadline_input[1] == "month" or deadline_input[1] == "months":
            deadline_date = today + timedelta(days=deadline_number * 30)
        deadline_date = str(deadline_date)
        print(f"\n*** Search by Life term '{deadline_date}' - RESULT: ")
        print_database(search_by_life_term(database, deadline_date))
