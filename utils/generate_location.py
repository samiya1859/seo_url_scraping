import random

def generate_location():
    # Predefined list of countries and cities
    locations = [
        ('usa', 'miami'),
        ('usa', 'new-york'),
        ('uk', 'london'),
        ('france', 'paris'),
        ('germany', 'berlin'),
        ('italy', 'rome'),
        ('spain', 'madrid'),
        ('japan', 'tokyo'),
        ('mexico', 'mexico-city'),
        ('india', 'delhi'),
        ('new-zealand', 'auckland'),
        ('norway', 'oslo'),
        ('finland', 'helsinki'),
        ('switzerland', 'zurich'),
        ('belgium', 'brussels'),
        ('austria', 'vienna'),
        ('sweden', 'gothenburg'),
        ('denmark', 'copenhagen'),
        ('turkey', 'istanbul'),
        ('thailand', 'bangkok'),
        ('south-korea', 'seoul'),
        ('singapore', 'singapore')
    ]
    
    # Randomly select a country and city
    country, city = random.choice(locations)
    
    # Format the URL
    return country, city
