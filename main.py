from database import (
    create_table,
    insert_record,
    get_all_records,
    update_record,
    delete_record,
    search_records
)

def menu():
    print("\n--- MENU ---")
    print("1. Add Record")
    print("2. View Records")
    print("3. Update Record")
    print("4. Delete Record")
    print("5. Search Records")
    print("6. Exit")

def get_valid_name():
    while True:
        name = input("Enter name: ").strip()
        if name:
            return name
        print("Name cannot be empty.")

def get_valid_age():
    while True:
        try:
            age = int(input("Enter age: "))
            if age > 0:
                return age
            print("Age must be positive.")
        except:
            print("Enter a valid number.")

def get_valid_email():
    while True:
        email = input("Enter email: ").strip()
        if "@" in email and "." in email:
            return email
        print("Invalid email format.")

def main():
    create_table()

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            name = get_valid_name()
            age = get_valid_age()
            email = get_valid_email()

            insert_record(name, age, email)
            print("Record added.")

        elif choice == "2":
            records = get_all_records()
            for r in records:
                print(r)

        elif choice == "3":
            try:
                record_id = int(input("Enter record ID to update: "))
                name = get_valid_name()
                age = get_valid_age()
                email = get_valid_email()

                update_record(record_id, name, age, email)
                print("Record updated.")
            except:
                print("Invalid ID.")

        elif choice == "4":
            try:
                record_id = int(input("Enter record ID to delete: "))
                delete_record(record_id)
                print("Record deleted.")
            except:
                print("Invalid ID.")

        elif choice == "5":
            keyword = input("Enter name to search: ")
            results = search_records(keyword)

            if results:
                for r in results:
                    print(r)
            else:
                print("No records found.")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()