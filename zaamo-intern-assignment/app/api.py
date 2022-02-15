from flask import Flask, jsonify
from typing import List, Tuple
import psycopg2
from datetime import datetime


# Establishing the connection with DB
conn = psycopg2.connect(
    user="username",
    password="db_password",
    host="127.0.0.1",
    port="5432",
    database="db_name")
cursor = conn.cursor()

# To get information from Database
def get_info(restaurant_type: str) -> List[Tuple]:
    """
    Will take Restaurant Type that we are searching for and will return all the restaurant that are open at that time.

    Parameters:
    restaurant_type: Type of the restaurant that client is looking for.
  
    Returns:
    List[Tuple]: List of Tuples containg the Name, Type, Description of the given type of Restaurants

    """
    curr_day = datetime.now().strftime("%A")
    curr_hour = datetime.now().time().hour
    curr_minute = datetime.now().time().minute
    curr_second = datetime.now().time().second

    cmnd = ''

    # Creating Query according to the day
    cmnd = f"SELECT name, restaurant_type, description FROM restaurant WHERE restaurant_type = '{restaurant_type}' and {curr_day.lower()}_opening_time < '{curr_hour}:{curr_minute}:{curr_second}' and monday_closing_time > '{curr_hour}:{curr_minute}:{curr_second}'"
    cursor.execute(cmnd)
    result = cursor.fetchall()
    
    return result


app = Flask(__name__)

@app.route('/api/restaurants/<restaurant_type>')
def home(restaurant_type: str):
    # Getting the list of all the open Restaurant at current time
    info = get_info(restaurant_type.capitalize())

    data = []

    # Formating Data for Easy Access
    for name, rest_type, description in info:
        d = {
            'name': name,
            'type': rest_type,
            'descriprtion': description
        }

        data.append(d)

    # returing the data to host/api/<type>
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
    cursor.close()
    conn.close()
