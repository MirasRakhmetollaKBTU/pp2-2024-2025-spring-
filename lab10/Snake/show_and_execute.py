import psycopg2
from config import load_config
from tabulate import tabulate

def show_data():
    """ Show Table """
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:

                cur.execute("SELECT * FROM SnakeGame")
                rows = cur.fetchall()

                if rows: print('\n' + tabulate(rows, headers['ID', 'Player_Name', 'Player_Level', 'Player_Score'], tablefmt='fancy_grid'))
                else:    print('\nNo records\n')

    except Exception as error:
        print("\nError showing data:", error)

def execute_sql(command):
    """ Execute any sql command """

    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(command)
                
    except Exception as error:
        print("\nError showing data:", error)

def main():
    print("1 - Show data\n2 - Exucte any SQL command\n")
    choice = input("Enter choice: ")

    if choice == '1':
        show_data()
    elif choice == '2':
        print("Enter SQL command")
        command = input("SQL> ")
        execute_sql(command)
    else:
        print("Invalid command.")

if __name__ == '__main__':
    main()
