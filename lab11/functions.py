from tabulate  import tabulate
from config    import load_config
import csv
import psycopg2



def insert_from_console():
    """ Insert a single user from console input. """


    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                print("select mode:\n1 - insert one data\n2 - insert many data\n")
                choice = input("Enter choice: ")                

                if choice == '1': 
                    name_input   = input("Enter name: ")
                    number_input = input("Enter phone number: ")                   
                    cur.execute("""
                                CREATE OR REPLACE PROCEDURE insert_or_update(name_input VARCHAR(255), number_input VARCHAR(15))
                                AS $$
                                BEGIN
                                    IF EXISTS (SELECT 1 FROM PhoneBook WHERE name = name_input) THEN 
                                        UPDATE PhoneBook SET number = number_input WHERE name = name_input;
                                    ELSE
                                        INSERT INTO PhoneBook(name, number) VALUES (name_input, number_input);
                                    END IF;
                                END;
                                $$ LANGUAGE plpgsql;
                                """)
                    cur.execute("CALL insert_or_update(%s, %s)", (name_input, number_input))
                    conn.commit()

                elif choice == '2':
                    quantity = int(input("Enter how much user are there: "))
                    names    = []
                    numbers  = []

                    for i in range(quantity):
                        name_i   = input(f"Enter name {i+1}: ")
                        number_i = input(f"Enter number {i+1}: ")

                        names.append(name_i)
                        numbers.append(number_i)
                    

                    cur.execute("""
                                CREATE OR REPLACE PROCEDURE insert_many_data(name_input VARCHAR(255)[], number_input VARCHAR(15)[])
                                AS $$       
                                DECLARE
                                    i INT;
                                    incorrect_data TEXT[] := '{}';
                                    unique_data TEXT[] := '{}';
                                BEGIN
                                    FOR i IN 1..ARRAY_LENGTH(name_input, 1) LOOP
                                        IF number_input[i] !~ '^\d{10,20}$' THEN
                                            incorrect_data := ARRAY_APPEND(incorrect_data, name_input[i] || ' -> ' || number_input[i]);
                                        ELSE
                                            BEGIN
                                                IF EXISTS (SELECT 1 FROM PhoneBook WHERE name = name_input[i]) THEN
                                                    unique_data := ARRAY_APPEND(unique_data, name_input[i] || ' -> ' || number_input[i]);
                                                ELSE
                                                    INSERT INTO PhoneBook(name, number) VALUES (name_input[i], number_input[i]); 
                                                END IF;
                                            END;
                                        END IF;
                                    END LOOP;

                                    RAISE NOTICE 'Incorrect data: %', incorrect_data;
                                    RAISE NOTICE 'Skipped data (duplicates): %', unique_data;
                                END;
                                $$ LANGUAGE plpgsql;
                                """)

                    cur.execute("CALL insert_many_data(%s, %s)", (names, numbers))
                    conn.commit()
                    
                    notices = conn.notices
                    for notice in notices:
                        print(notice)
                    
                    conn.notices.clear()               
                
                else: print("Invalide choice"); return

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
                            cur.execute("""
                                        CREATE OR REPLACE PROCEDURE insert_by_CSV(name_input VARCHAR(255), number_input VARCHAR(15))
                                        AS $$
                                        DECLARE
                                            unique_data TEXT[] := '{}';
                                        BEGIN
                                            IF EXISTS (SELECT 1 FROM PhoneBook WHERE name = name_input) THEN
                                                unique_data := ARRAY_APPEND(unique_data, name_input || ' -> ' || number_input);
                                            ELSE
                                                INSERT INTO PhoneBook(name, number) VALUES (name_input, number_input);
                                            END iF;
                                            RAISE NOTICE 'Skipped Date (duplicates) --> %s', unique_data;
                                        END;
                                        $$ LANGUAGE plpgsql;
                                        """)
                            cur.execute("CALL insert_by_CSV(%s, %s)", (name, number))
                            
                            notices = conn.notices
                            for notice in notices:
                                print(notice)
                            conn.notices.clear()                           
                    
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
                    cur.execute("""
                                CREATE OR REPLACE PROCEDURE update_by_name(new_name VARCHAR(255), identifier VARCHAR(255))
                                AS $$
                                BEGIN
                                    UPDATE PhoneBook SET name = new_name WHERE name = identifier;
                                END;
                                $$ LANGUAGE plpgsql;
                                """)
                    cur.execute("CALL update_by_name(%s, %s)", (new_name, identifier))

                    print("Name updated successfully.")

                elif choice == '2':
                    new_number = input("Enter the new number: ")
                    cur.execute("""
                                CREATE OR REPLACE PROCEDURE update_by_number(new_number VARCHAR(15), identifier VARCHAR(15))
                                AS $$
                                BEGIN
                                    UPDATE PhoneBook SET number = new_number WHERE number = identifier;
                                END;
                                $$ LANGUAGE plpgsql;
                                """)
                    cur.execute("UPDATE PhoneBook SET number = %s WHERE name = %s", (new_number, identifier))

                    print("\nPhone number updated successfully.\n")

                else:
                    print("Invalid choice.")
                    return

                conn.commit()
    except Exception as error:
        print("\nError updating entry:\n", error)

def query_data():
    """ Query data with different filters, displayed nicely. """

    print ("\nChoose a filter:\n1 - Show all\n2 - Filter by name\n3 - Filter by phone\n4 - Search by pattern\n")
    choice = input("\nEnter choice [1/2/3/4]: ")

    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:

                if choice == '1':
                    cur.execute("""
                                CREATE OR REPLACE FUNCTION show_all()
                                RETURNS TABLE(id INT, name VARCHAR(255), number VARCHAR(15))
                                AS $$
                                BEGIN
                                    RETURN QUERY
                                    SELECT PhoneBook.id, PhoneBook.name, PhoneBook.number
                                    FROM PhoneBook;
                                END;
                                $$
                                LANGUAGE plpgsql;
                                """)
                    cur.execute("SELECT * FROM show_all()")
                    rows = cur.fetchall()

                elif choice == '2':
                    exact_name = input("Enter name to search: ")
                    cur.execute("""
                                CREATE OR REPLACE FUNCTION search_by_name(exact_name VARCHAR(255))
                                RETURNS TABLE(id INT, name VARCHAR(255), number VARCHAR(15))
                                AS $$
                                BEGIN
                                    RETURN QUERY
                                    SELECT PhoneBook.id, PhoneBook.name, PhoneBook.number
                                    FROM PhoneBook
                                    WHERE PhoneBook.name = exact_name;
                                END
                                $$ LANGUAGE plpgsql;
                                """)
                    cur.execute("SELECT * FROM  search_by_name(%s)", (exact_name,))
                    rows = cur.fetchall()

                elif choice == '3':
                    exact_number = input("Enter number to search: ")
                    cur.execute("""
                                CREATE OR REPLACE FUNCTION search_by_number(exact_number VARCHAR(15))
                                RETURNS TABLE(id INT, name VARCHAR(255), number VARCHAR(15))
                                AS $$
                                BEGIN
                                    RETURN QUERY
                                    SELECT PhoneBook.id, PhoneBook.name, PhoneBook.number
                                    FROM PhoneBook
                                    WHERE PhoneBook.number = exact_number;
                                END
                                $$ LANGUAGE plpgsql;
                                """)
                    cur.execute("SELECT * FROM  search_by_number(%s)", (exact_number,))
                    rows = cur.fetchall()

                elif choice == '4':
                    pattern = input("Enter pattern (e.g., 'Ali' or '87%'): ")
                    cur.execute("""
                                CREATE OR REPLACE FUNCTION search_pattern(pattern VARCHAR(255))
                                RETURNS TABLE(id INT, name VARCHAR(255), number VARCHAR(15))
                                AS $$
                                BEGIN
                                    RETURN QUERY
                                    SELECT PhoneBook.id, PhoneBook.name, PhoneBook.number
                                    FROM PhoneBook
                                    WHERE PhoneBook.name ILIKE '%' || pattern || '%'
                                       OR PhoneBook.number ILIKE '%' || pattern || '%';
                                END;
                                $$ LANGUAGE plpgsql;
                                """)
                    cur.execute("SELECT * FROM search_pattern(%s)", (pattern,))
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
                    cur.execute("""
                                CREATE OR REPLACE PROCEDURE delete_by_name(name_input VARCHAR(255))
                                AS $$
                                BEGIN
                                    DELETE FROM PhoneBook WHERE name = name_input;
                                END;
                                $$ LANGUAGE plpgsql;
                                """)
                    cur.execute("CALL delete_by_name(%s)", (name,))
                    print(f"\nDeleted {cur.rowcount} record with name '{name}'.\n")

                elif choice == '2':
                    number = input("Enter the number to delete: ")
                    cur.execute("""
                                CREATE OR REPLACE PROCEDURE delete_by_number(number_input VARCHAR(20))
                                AS $$
                                BEGIN
                                    DELETE FROM PhoneBook WHERE number = number_input;
                                END;
                                $$ LANGUAGE plpgsql;
                                """)
                    cur.execute("CALL delete_by_number(%s)", (number,))
                    print(f"\nDeleted {cur.rowcount} record with number '{number}'.\n")

                else:
                    print("Invalid choic.")
                    return

                conn.commit()

    except Exception as error:
        print("Error deleting entry:", error)


def select_part_of_data():
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT COUNT(id) FROM PhoneBook")
                length = cur.fetchone()[0]
                print("Length of table is : ", length)

                offset = int(input("Enter offset: "))
                if offset > length: print("Offset cannot be less than length of database"); return
                if offset < 0:      print("Offset cannot be less than zero");               return

                limit = int(input("Enter limit: "))
                if limit + offset > length: limit = length - offset
                if limit < 0:               print("Limit cannot be less than zero"); return

                cur.execute("""
                            CREATE OR REPLACE FUNCTION  select_part_of_data_base(offset_input INT, limit_input INT)
                            RETURNS TABLE(id INT, name VARCHAR(255), number VARCHAR(15))
                            AS $$
                            BEGIN
                                RETURN QUERY
                                SELECT * FROM PhoneBook ORDER BY id LIMIT limit_input OFFSET offset_input;
                            END;
                            $$ LANGUAGE plpgsql
                            """)

                cur.execute("SELECT * FROM select_part_of_data_base(%s, %s)", (offset, limit))

                rows = cur.fetchall()
                if rows: print('\n' + tabulate(rows, headers=[desc[0] for desc in cur.description], tablefmt="fancy_grid"))
                else:    print("Query executed. No results in display.")



                conn.commit()

    except  Exception as error:
        print("Error offset and limit: ", error)
