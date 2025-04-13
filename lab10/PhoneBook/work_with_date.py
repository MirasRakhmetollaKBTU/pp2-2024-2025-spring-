import psycopg2
import csv
from config import load_config
from tabulate import tabulate # You may not have this library, pleas download this if it is not avalable

def insert_from_console():
    """ Insert a single user from console input. """
    name   = input("Enter name: ")
    number = input("Enter phone number: ")

    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(
                        "INSERT INTO PhoneBook (name, number) VALUES (%s, %s)",
                        (name, number)
                        )

                conn.commit()
                print("\nData inserted successfully.\n")

    except Exception as error:
        print("Error inserting from console:", error)

def insert_from_csv(file_path):
    """ Insert multiple users from a CSV file. """
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                with open(file_path, newline='', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if len(row) == 2:
                            name, number = row
                            cur.execute(
                                    "INSERT INTO PhoneBook (name, number) VALUES (%s, %s)",
                                    (name, number)
                                    )
                    conn.commit()
                    print("\nCSV data uploaded successfully.\n")


    except Exception as error:
        print("Error inserting from CSV:", error)


def update_date():
    """ Update a user's name or phone number based on ID or name. """

    print("\nWhat do you want to update?\n1 - Update name\n2 - Update phone number\n")
    choice = input("Enter choice [1/2]: ")

    identifier = input("Enter the name of the user to update: ")

    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:

                if choice == '1':
                    new_name = input("Enter the new name: ")
                    cur.execute(
                        "UPDATE PhoneBook SET name = %s WHERE name = %s", 
                        (new_name, identifier)
                    )

                    print("Name updated successfully.")

                elif choice == '2':
                    new_number = input("Enter the new number: ")
                    cur.execute(
                        "UPDATE PhoneBook SET number = %s WHERE name = %s",
                        (new_number, identifier)
                    )

                    print("\nPhone number updated successfully.\n")

                else:
                    print("Invalid choice.")
                    return

                conn.commit()
    except Exception as error:
        print("\nError updating entry:\n", error)

def query_data():
    """ Query data with different filters, displayed nicely. """

    print ("\nChoose a filter:\n1 - Show all\n2 - Filter by name\n3 - Filter by phone\n4 - Search by partial match")
    choice = input("\nEnter choice [1/2/3/4]: ")

    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:

                if choice == '1':
                    cur.execute("SELECT * FROM PhoneBook")
                    rows = cur.fetchall()

                elif choice == '2':
                    name = input("Enter name to search: ")
                    cur.execute("SELECT * FROM PhoneBook WHERE name = %s", (name,))
                    rows = cur.fetchall()

                elif choice == '3':
                    number = input("Enter number to search: ")
                    cur.execute("SELECT * FROM PhoneBook WHERE number = %s", (number,))
                    rows = cur.fetchall()

                elif choice == '4':
                    pattern = input("Enter partial name or number (e.g., 'Ali' or '87%'): ")
                    cur.execute("SELECT * FROM PhoneBook WHERE name ILIKE %s OR number ILIKE %s", 
                                (f"%{pattern}%", f"%{pattern}%"))
                    rows = cur.fetchall()

                else:
                    print("Invalid choice.")
                    return

                if rows:
                    print("\n" + tabulate(rows, headers=["ID", "Name", "Phone number"], tablefmt="fancy_grid"))
                else:
                    print("\nNo records found.\n")

    except Exception as error:
        print("\nError querying data:\n", error)

def run_custom_sql():
    """ Allow user to write and run custom SQL commands. """

    print("\nEnter your SQL query below")
    query = input("SQL> ")

    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(query)

                try:
                    rows = cur.fetchall()
                    if rows: print('\n' + tabulate(rows, headers=[desc[0] for desc in cur.description], tablefmt="fancy_grid"))
                    else:    print("Query executed. No results in display.")

                except psycopg2.ProgrammingError:
                    # Not SELECT query (e.g., INSERT/UPDATE/DELETE)
                    print("Query executed succesfully (no return values).")

                conn.commit()

    except Exception as error:
        print("Error executing custom SQL:", error)

def delete_entry():
    """ Delete an entry from the PhoneBook by name or number. """
    print("\nChoose deletion filter:\n1 - Delete by name\n2 - Delete by number")
    choice = input("Enter choice [1/2]: ")

    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:

                if choice == '1':
                    name = input("Enter the name to delete: ")
                    cur.execute("DELETE FROM PhoneBook WHERE name = %s", (name,))
                    print(f"\nDeleted {cur.rowcount} record with name '{name}'.\n")

                elif choice == '2':
                    number = input("Enter the number to delete: ")
                    cur.execute("DELETE FROM PhoneBook WHERE number = %s", (number,))
                    print(f"\nDeleted {cur.rowcount} record with number '{number}'.\n")

                else:
                    print("Invalid choic.")
                    return

                conn.commit()

    except Exception as error:
        print("Error deleting entry:", error)

if __name__ == '__main__':

    going = True
    while going:
        print('Choose an option\n\n1 - Insert from console\n2 - Upload from CSV file\n3 - Update date\n4 - Query Date\n5 - Deletion\n6 - custom commands\n7 - Exit')
        choice = input("\nEnter option [1/2/3/4/5/6/7]: ")

        if choice == '1':   insert_from_console()
        elif choice == '2': insert_from_csv('CSV_DATA.csv')
        elif choice == '3': update_date()
        elif choice == '4': query_data()
        elif choice == '5': delete_entry()
        elif choice == '6': run_custom_sql()
        elif choice == '7': print("\nProcess ended.\n"); going = False
        else: print("\nInvalid choice.\n")
