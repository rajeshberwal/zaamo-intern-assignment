import psycopg2 # To work with PostgreSQL

# Establishing a connection with PostgreSQL Database
conn = psycopg2.connect(
    user="username",
    password="password",
    host="127.0.0.1",
    port="5432",
    database="db_name")
cursor = conn.cursor()

# PostgreSQL command to create a table named restaurant in database
cmnd = '''CREATE TABLE IF NOT EXISTS restaurant(
    rest_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    restaurant_type VARCHAR(255),
    description VARCHAR(255),
    monday_opening_time TIME,
    monday_closing_time TIME,
    tuesday_opening_time TIME,
    tuesday_closing_time TIME,
    wednesday_opening_time TIME,
    wednesday_closing_time TIME,
    thursday_opening_time TIME,
    thursday_closing_time TIME,
    friday_opening_time TIME,
    friday_closing_time TIME,
    saturday_opening_time TIME,
    saturday_closing_time TIME,
    sunday_opening_time TIME,
    sunday_closing_time TIME
)'''

# Executing the Command to DB
cursor.execute(cmnd)

cursor.close()

# To commit all the changes to DB
conn.commit()

# Closing the connection with DB
conn.close()