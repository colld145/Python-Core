from lib import *


def menu():
    database = create_database()
    exit = False
    while not exit:
        numbering(database)
        print("\n. . .")
        print(
            "\t- 1. Add item\n\t- 2. Print items\n\t- 3. Edit item\n\t- 4. Remove item\n\t- 5. Search item\n\t- 6. Sort by Price\n\t- 7. Sort by Group\n\n\t- 0. Exit\n"
        )
        choice = input(">> ")
        if choice == "1":
            add_item(database)
        elif choice == "2":
            print_database(database)
        elif choice == "3":
            print_database(database)
            edit = int(input("Enter a number of item to edit: "))
            edit_item(database, edit)
        elif choice == "4":
            print_database(database)
            delete = int(input("Enter a number of item to delete: "))
            remove_item(database, delete)
        elif choice == "5":
            search = input(
                "1. Search by Name\n2. Search by Producer\n3. Search by Price\n4. Search by Group\n5. Search by Come date\n6. Search by Life term\n\nEnter a type of search: "
            )
            search_item(database, search)
        elif choice == "6":
            database.sort(key=sort_by_price)
            numbering(database)
            print_database(database)
        elif choice == "7":
            database.sort(key=sort_by_group)
            numbering(database)
            print_database(database)
        elif choice == "0":
            exit = True

    write_file(database)
