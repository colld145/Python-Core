from lib import *


def menu():
    database = create_database()
    exit = False
    while not exit:
        numbering(database)
        print("\n. . .")
        print(
            "\t- 1. Print\n\t- 2. Search\n\n\t- 3. Add\n\t- 4. Edit\n\t- 5. Remove\n\t- 6. Sort\n\n\t- 0. Exit\n"
        )
        choice = input(">> ")
        if choice == "1":
            print_database(database)
        elif choice == "2":
            search = input(
                "\nSEARCH:\n1. by Name\n2. by Producer\n3. by Price\n4. by Group\n5. by Come date\n6. by Life term\n\n0. Back\n\nEnter a type of search: "
            )
            if search == "0":
                continue
            search_item(database, search)
        elif choice == "3":
            add_item(database)

        elif choice == "4":
            print_database(database)
            edit = int(input("\n\n0. Back\n\nEnter a number of item to edit: "))
            edit_item(database, edit)
        elif choice == "5":
            print_database(database)
            delete = int(input("\n\n0. Back\n\nEnter a number of item to delete: "))
            remove_item(database, delete)
        elif choice == "6":
            choice = input(
                "\nSORT:\n1. by Price\n2. by Group\n\n0. Back\n\nEnter a choice: "
            )
            if choice == "1":
                database.sort(key=sort_by_price)
                numbering(database)
                print_database(database)
            elif choice == "2":
                database.sort(key=sort_by_group)
                numbering(database)
                print_database(database)
        elif choice == "0":
            exit = True

    write_file(database)
