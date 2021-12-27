# Zaamo Internship Assignment

## Description

Part - 1:

Hit an external api https://random-data-api.com/api/restaurant/random_restaurant around 100
time using a script and save the data coming from the api in database. Save the data of name,
type and description along with opening and closing hours. Create a database schema in order
to save this data in an efficient way.

Part - 2:

After saving the data, create a rest api which will take type as a parameter and returns the list of
restaurants that are open at that time.
For example, If a person likes Italian the type parameter will be Italian and the rest api will
return all the Italian restaurants that are open at the time of calling the api.

## Uses

Creating an Virtual Environment

```python
pip install virtualenv
virtualenv env_name
```

Activating the Virtual Environment

```bash
source ./env_name/Scripts/activate
```

Installing all the Libraries

```python
pip install -r requirements.txt
```

Using Script to Scrap the data and saving in Database:

```python
cd api-to-db-script
python main.py
```

Update the information of DB in create-table.py and main.py. Recommened to use config module.

Accessing the Restaurant data using API:

```python
python api.py
```

Visit host:5000/api/restaurants/<restaurant_type>(Here replace restaurant_type with type you want to search).