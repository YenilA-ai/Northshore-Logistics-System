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
            record_id = int(input("Enter record ID to update: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            email = input("Enter new email: ")

            update_record(record_id, name, age, email)
            print("Record updated.")

        elif choice == "4":
            record_id = int(input("Enter record ID to delete: "))
            delete_record(record_id)
            print("Record deleted.")

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