
import csv

def read_file():
    try:
        file = open("task.csv", "r")
        csvreader = csv.reader(file)
        return csvreader
    except Exception as error:
        print(f"Error: {error}")


def print_file(csv_file):
        for row in csv_file:
            print(row)
    

def search_by_countries(csv_file, country):
    for row in csv_file:
        if country in row:
            print(row)


def salary_range(csv_file, start, finish):
    for row in csv_file:
        if row[5] >= start and row[5] <= finish:
            print(row)


def search_by_name(csv_file, name):
    for row in csv_file:
        if name in row:
            print(row)


def search_by_surname(csv_file, surname):
    for row in csv_file:
        if surname in row:
            print(row)


def write_country(csv_file, country):
    file = open(f"{country}.csv", "w")
    for row in csv_file:
        if country in row:
            for item in row:
                if item == row[-1]:
                    file.writelines(f"{item}")
                    break
                file.writelines(f"{item},")
            file.writelines("\n")
    file.close()


def country_size(csv_file, country):
    amount = 0
    for row in csv_file:
        if country in row:
            amount += 1
    return amount


def menu():
    while True:
        csv_file = read_file()
        print("1. Print file\n2. Search by Country\n3. Search by Salary\n4. Search by Name\n5. Search by Surname\n6. Write country\n7. Country size\n0. Exit")
        choice = input()
        if choice == "1":
           print_file(csv_file)
        elif choice == "2":
            country = input("Enter a country: ")
            search_by_countries(csv_file, country)
        elif choice == "3":
            start = input("Enter a start: ")
            finish = input("Enter a finish: ")
            salary_range(csv_file, start, finish)
        elif choice == "4":
            name = input("Enter a name: ")
            search_by_name(csv_file, name)
        elif choice == "5":
            surname = input("Enter a surname: ")
            search_by_surname(csv_file, surname)
        elif choice == "6":
            country = input("Enter a country: ")
            write_country(csv_file, country)
        elif choice == "7":
            country = input("Enter a country: ")
            print(f"{country}'s amount of people: {country_size(csv_file, country)}")
        elif choice == "0":
            break


# Start
menu()