"""
A restaurant recommendation system.

Here are some example dictionaries. They correspond to the information in
restaurants_small.txt.

Restaurant name to rating:
# dict of {str: int}
{'Georgie Porgie': 87,
'Queen St. Cafe': 82,
'Dumplings R Us': 71,
'Mexican Grill': 85,
'Deep Fried Everything': 52}

Price to list of restaurant names:
# dict of {str: list of str}
{'$': ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything'],
'$$': ['Mexican Grill'],
'$$$': ['Georgie Porgie'],
'$$$$': []}

Cuisine to list of restaurant names:
# dict of {str: list of str}
{'Canadian': ['Georgie Porgie'],
'Chinese': ['Dumplings R Us'],
'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
'Malaysian': ['Queen St. Cafe'],
'Thai': ['Queen St. Cafe'],
'Mexican': ['Mexican Grill']}

With this data for a price '$' and cuisines of ['Chinese', 'Thai'], we
would produce a list like this:
    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
"""

# The file containing the restaurants data.
FILENAME = 'restaurants_small.txt'


def recommend(file, price, cuisines_list):
    """ (file open for reading, str, list of list) -> list of list of str

    Find restaurants in a file that are priced according to the price and tagged with
    any of the items in the cuisines_list. Return a list of list of restaurant names
    with their rating in the form [rating%, restaurant name] sorted by rating% in
    descending order.
    """

    # Read the file and build the data structures with the information in the file.
    # - a dict of {restaurant name: rating%}
    # - a dict of {price: list of restaurant names}
    # - a dict of {cuisine: list of restaurant names}
    name_to_rating, price_to_names, cuisine_to_names = read_restaurants(file)

    # Look for the cuisines or price first?
    # Price: filter out restaurant names for the requested price.
    names_matching_price = price_to_names[price]

    # Now that we have a list of restaurant names that matches the price range.
    # So, now filter out from this list the restaurant names that serve any of the cuisines from cuisines_list.
    names_final = filter_by_cuisine( names_matching_price, cuisines_list, cuisine_to_names)

    # Now we have the list of restaurant names in the right price range and which serve any of the requested cuisines.
    # Need to look at ratings and sort the list.
    result = build_rating_list(name_to_rating, names_final)

    # And we are done! Return the sorted list.
    return result


def build_rating_list(name_to_rating, names_final):
    """ (dict of {str: int}, list of str) -> list of list of [int, str]

    Return a list of [rating%, restaurant name], sorted by rating%

    >>> name_to_rating = {'Georgie Porgie': 87, \
    'Queen St. Cafe': 82, \
    'Dumplings R Us': 71, \
    'Mexican Grill': 85, \
    'Deep Fried Everything': 52}
    >>> names_final = ['Queen St. Cafe', 'Dumplings R Us']
    >>> build_rating_list(name_to_rating, names_final)
    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
    """

    # Initialize empty list.
    result = []
    for name in names_final:
        result.append([name_to_rating[name], name])

    # Sort the result according to rating% in descending order
    result.sort(reverse=True)

    return result


def filter_by_cuisine(names_matching_price, cuisines_list, cuisine_to_names):
    """ (list of str, list of str, dict of {str: list of str}) -> list of str

    Returns a list of restaurant names which serve any of the requested cuisines and are in the requested price range.

    >>> names = ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything']
    >>> cuis = {'Canadian': ['Georgie Porgie'], \
      'Chinese': ['Dumplings R Us'], \
      'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'], \
      'Malaysian': ['Queen St. Cafe'], \
      'Thai': ['Queen St. Cafe'], \
      'Mexican': ['Mexican Grill']}
    >>> cuisines = ['Chinese', 'Thai']
    >>> filter_by_cuisine(names, cuisines, cuis)
    ['Queen St. Cafe', 'Dumplings R Us']
    """

    # Initialize empty list
    result = []

    # Check for each restaurant if it serves any of the requested cuisine(s). If yes then add it to the result.
    for name in names_matching_price:
        for cuisine in cuisines_list:
            if name in cuisine_to_names[cuisine]:
                if name not in result:
                    result.append(name)

    return result


def read_restaurants(file):
    """ (file) -> (dict, dict, dict)

    Return a tuple of three dictionaries based on the information in the file:

    - a dict of {restaurant name: rating%}
    - a dict of {price: list of restaurant names}
    - a dict of {cuisine: list of restaurant names}
    """

    # Get all the lines as a list of strings
    lines = [s.strip('\n') for s in file.readlines()]

    # Now for each restaurant we store it's name, rating, price and cuisines it serves in a list.
    # We create another list restaurant where we put all the restaurant data in a single list
    restaurants_data = []
    restaurant = []
    for line in lines:
        if line == '':
            restaurants_data.append(restaurant)
            restaurant = []
        else:
            restaurant.append(line)

    # A final update to restaurants_data in case something left
    if restaurant:
        restaurants_data.append(restaurant)

    # Initialize the dictionaries with empty values
    name_to_rating = {}
    price_to_names = {'$': [], '$$': [], '$$$': [], '$$$$': []}
    cuisines_to_names = {}

    # We iterate over all the data considering each restaurant at a time and update the dictionaries as necessary.
    for item in restaurants_data:
        name_to_rating[item[0]] = item[1].strip('%')
        price_to_names[item[2]].append(item[0])
        cuisines = item[3].split(',')
        for i in cuisines:
            # Check if the cuisine is already added in the cuisines_to_names dictionary.
            if i in cuisines_to_names.keys():
                cuisines_to_names[i].append(item[0])
            else:
                cuisines_to_names[i] = [item[0]]

    # Finally return the dictionaries.
    return name_to_rating, price_to_names, cuisines_to_names

