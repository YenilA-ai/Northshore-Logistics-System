from database import create_table, insert_record, get_all_records

def menu():
    print("\n--- MENU ---")
    print("1. Add Record")
    print("2. View Records")
    print("3. Exit")

def main():
    create_table()

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            email = input("Enter email: ")

            insert_record(name, age, email)
            print("Record added.")

        elif choice == "2":
            records = get_all_records()
            for r in records:
                print(r)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()