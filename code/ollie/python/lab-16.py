' Lab 16 - Mini Capstone: CAP2CAP '

""" The purpose of this program is to calculate the distace between
any two country capitals in the world, in the user's unit of choice.

If this became a larger capstone project I would include all cities with
a population over 10,000 and allow more than two capitals and determine
the shortest path through all chosen capitals. """

from geopy import distance                          # to convert (lat, long) to distance in km
import pandas as pd

data = pd.read_csv("concap.csv")                            # converts csv file of capitals' data to dataframe

data = data.rename(columns = {
    "CountryName": "COUNTRY",
    "CapitalName": "CAPITAL",
    "CapitalLatitude": "LAT",
    "CapitalLongitude": "LONG",
    "CountryCode": "CODE",
    "ContinentName": "CONTINENT"
    })

def cap_distance():
    cap1 = input("Enter a country's capital: ").title()
    cap2 = input("Enter another country's capital: ").title()

    cap_data = data[data['CAPITAL'].isin([cap1, cap2])].reset_index()                           # grabs dataframe info for only the two user given countries

    coord_dist = distance.distance((cap_data.loc[0, 'LAT'], cap_data.loc[0, 'LONG']), (cap_data.loc[1, 'LAT'], cap_data.loc[1, 'LONG']))                # get coords from both countries under 'Long' and 'Lat' columns and return distance between them

    return coord_dist.meters

def user_distance():                            # convert distance to user's uinit of choice and display for them
    units = input("What unit would you like your distance represented in? ").lower()
    if units in ['m', 'meter', 'meters']:
        dist = round(cap_distance(), 2)
        print(f"The distance between your two capitals is {dist} meters.")
    elif units in ['cm', 'centimeter', 'centimeters']:
        dist = round((cap_distance() / 0.01), 2)
        print(f"The distance between your two capitals is {dist} centimeters.")
    elif units in ['km', 'kilometer', 'kilometers']:
        dist = round((cap_distance() / 1000), 2)
        print(f"The distance between your two capitals is {dist} kilometers.")
    elif units in ['mi', 'mile', 'miles']:
        dist = round((cap_distance() / 1609.34), 2)
        print(f"The distance between your two capitals is {dist} miles.")
    elif units in ['yd', 'yard', 'yards']:
        dist = round((cap_distance() / 0.9144), 2)
        print(f"The distance between your two capitals is {dist} yards.")
    elif units in ['ft', 'foot', 'feet']:
        dist = round((cap_distance() / 0.3048), 2)
        print(f"The distance between your two capitals is {dist} feet.")
    elif units in ['in', 'inch', 'inches']:
        dist = round((cap_distance() / 0.0254), 2)
        print(f"The distance between your two capitals is {dist} inches.")

print(f"""
                        ~~ Welcome to: CAP2CAP! ~~
               ,_   .  ._. _.  .
           , _- ','|~\~      ~/      ;-'_   _-'   __,;_;_,    ~~-
  /~~-\_/-'~'--' \~~| ',    ,'      /  / ~|-_\_/~/       ~~--~~~~'--_
  /              ,/'-/~ '\ ,'    , '|,'|~                   ._/-, /
  ~/-'~\_,       '-,| '|. '      ,\ /'~                /    /_  /
         '|        '',\|\        _\~     ,_                  /|
          '\        /'           |_/~\_,-,~              ,_,/ |
           |       /             _-~'\_ _~|              \ ) /
            \   __-\            /      ~ |\  \_          /  ~
  .,         '\ |,  ~-_        |          |\_' ~|  /\  \~ ,
               ~-_'  ~~        \           '-,   \,' /\/  |
                 '\_,~'\_       \_ _,       /     '  |, /|'
                   /     \_       ~ |      /         \  ~'; -,_.
                   |       ~\        |    |  ,        '-_, ,; ~ ~
                    \,      /        \    / /|            ,-, ,   -,
                     |    ,/          |  |' |/          ,-   ~ \   '.
                    ,|   ,/           \ ,/              \       |
                     |   |             ~                 -~~-, /   _
                     | ,/'                                    ~    /
                     / ,'                                      
                     ',|  ~""")     # Google search: 'ascii art world map'
user_distance()