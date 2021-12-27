from typing import Any, List
import requests
import json


def get_info() -> List[Any]:
    """
    Returns a list containg the information about Restaurant 
  
    Parameters:
    None: None
  
    Returns:
    List[int]: List containg the Name, Type, Description and Timing of the Restaurant
  
    """
    response = requests.get('https://random-data-api.com/api/restaurant/random_restaurant')

    # Check if connection is OK or Not
    # print(response.status_code)

    data = response.text

    # Parsing into JSON format
    json_data = json.loads(data)

    name = json_data['name']                    # Name of the Restaurant
    rest_type = json_data['type']               # Type of Food at That Restaurant
    description = json_data['description']      # Description of the Restaurant
    timing = json_data['hours']                 # Timing of the Restaurant

    return [name, rest_type, description, timing]


# timing = get_info()[3]
# print(timing['monday']['opens_at'], timing['monday']['closes_at'])