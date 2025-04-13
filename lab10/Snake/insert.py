from config import load_config
import psycopg2

def insert_data(username, userlevel, userscore):
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(
                        "INSERT INTO SnakeGame (player_Name, player_Level, Player_Score) VALUES(%s,%s,%s)",
                        (username, userlevel, userscore)
                        )

                conn.commit()
                print("\nData inserted succesfully.\n")
    except Exception as error:
        print("Error inserting data:", error)
