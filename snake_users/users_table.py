import psycopg2

config = psycopg2.connect(
    host = 'localhost',
    database='postgres',
    user='postgres',
    password='zzzz06'
)
cur = config.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    level INTEGER NOT NULL,
    score INTEGER NOT NULL);
""")

cur.execute("""
INSERT INTO users (username, level, score) 
VALUES ('Aizat', 0, 0), ('Aboo', 0, 0);
""")

config.commit()

cur.close()
config.close()