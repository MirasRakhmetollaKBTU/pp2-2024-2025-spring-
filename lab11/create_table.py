import psycopg2
from config import load_config

def create_tables():
    """ Create tables in the PostgreSQL database """

    commands = [
            """
            CREATE TABLE IF NOT EXISTS PhoneBook (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                number VARCHAR(15) NOT NULL
                )
            """]

    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Execute the CREATE TABLE statement
                for command in commands:
                    cur.execute(command)

                conn.commit()

    except (psycopg2.DatabaseError, Exception) as error:
        print('Error creating tables:', error)


if __name__ == '__main__':
    create_tables()
