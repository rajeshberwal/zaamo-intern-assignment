from get_info import get_info
import psycopg2

# Database Connection
conn = psycopg2.connect(
    user="username",
    password="password",
    host="127.0.0.1",
    port="5432",
    database="db_name")
cursor = conn.cursor()

# Query to insert data into database
postgres_insert_query = """INSERT INTO restaurant (
    name,
    restaurant_type,
    description,
    monday_opening_time,
    monday_closing_time,
    tuesday_opening_time,
    tuesday_closing_time,
    wednesday_opening_time,
    wednesday_closing_time,
    thursday_opening_time,
    thursday_closing_time,
    friday_opening_time,
    friday_closing_time,
    saturday_opening_time,
    saturday_closing_time,
    sunday_opening_time,
    sunday_closing_time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s,%s)"""

# record_to_insert = (5, 'One Plus 6', 950)

# data = get_info()
# timing = data[3]
# print(timing['monday']['opens_at'])

for i in range(100):
    data = get_info()

    name = data[0]
    restaurant_type = data[1]
    description = data[2]
    timing = data[3]

    record_to_insert = (
        name,
        restaurant_type,
        description,
        timing['monday']['opens_at'],
        timing['monday']['closes_at'],
        timing['tuesday']['opens_at'],
        timing['tuesday']['closes_at'],
        timing['wednesday']['opens_at'],
        timing['thursday']['closes_at'],
        timing['thursday']['opens_at'],
        timing['thursday']['closes_at'],
        timing['friday']['opens_at'],
        timing['friday']['closes_at'],
        timing['saturday']['opens_at'],
        timing['saturday']['closes_at'],
        timing['sunday']['opens_at'],
        timing['sunday']['closes_at'],
    )

    cursor.execute(postgres_insert_query, record_to_insert)

    conn.commit()

cursor.close()
conn.close()