import psycopg2
from config import load_config

def create_tables():
    """ Create tables in the PostgreSQL database """

    commands = [
            """
            CREATE TABLE IF NOT EXISTS users(
                user_id SERIAL PRIMARY KEY,
                user_name VARCHAR(255) UNIQUE NOT NULL
                );

            CREATE TABLE IF NOT EXISTS users_score(
                score_id SERIAL PRIMARY KEY,
                user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
                score INTEGER NOT NULL,
                level INTEGER NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """]

    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)

                conn.commit()

    except (psycopg2.DatabaseError, Exception) as error:
        print('Error creating tables:', error)

if __name__ == '__main__':
    create_tables()
