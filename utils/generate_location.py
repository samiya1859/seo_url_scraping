import random

def generate_location():
    # Predefined list of countries and cities
    locations = [
        ('usa', 'new-york'),
        ('usa','florida'),
        ('france', 'paris'),
        ('japan', 'tokyo'),
        ('mexico', 'mexico-city'),
        ('norway', 'oslo'),
        ('finland', 'helsinki'),
        ('switzerland', 'zurich'),
        ('austria', 'vienna'),
        ('turkey', 'istanbul'),
        ('thailand', 'bangkok'),
        ('south-korea', 'seoul'),
    ]
    
    # Randomly select a country and city
    country, city = random.choice(locations)
    
    # Format the URL
    return country, city
