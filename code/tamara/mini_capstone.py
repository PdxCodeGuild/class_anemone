import requests, pprint
from collections import Counter

region_code = "US-WA-061" 

def regional_birds(region_code): # create method to tell you species of bird in a region
    response=requests.get(f"https://api.ebird.org/v2/product/spplist/{region_code}", headers = { 'X-eBirdApiToken': 'f20hu1432los'})
    # bird_species_list = response.json()
    return response

regional_bird_species = regional_birds(region_code) # L7884500 works

# pprint.pprint(regional_bird_species.text)

# now create a method to show the information for a species of bird then you can create a for loop that takes
# all the species of birds in a region and gives you there information
# additional addons are converting a place name into > GPS > regional code somehow ish like that
# also consider adding on bird song data and taxanomic info like pictures etc. for a species that is selected from the list.
# you can also addon endangered species information from other API for bird species in the list
# still need to import another thingy

state_code = 'US-WA'

def regional_codes(state_code): # create method to tell you species of bird in a region
    response=requests.get(f"https://api.ebird.org/v2/ref/region/list/subnational2/{state_code}", headers = { 'X-eBirdApiToken': 'f20hu1432los'})
    # bird_species_list = response.json()
    return response

regional_state_codes = regional_codes(state_code) # L7884500 works

# pprint.pprint(f"\n{regional_state_codes.text}")

# OKAY so what you need to do is have user input a state and county which is converted into a state code via a dict
# the state code is then entered into the regional_codes function and then the code for the given county is retrieved
# this code can then be used to retrieve all of the species sighted in that region
# then these species can be used to retrieve additional info about them
# it may be easier if you turn this into some kind of Class

# returns a LARGE number of bird species 100 + so just return the common names of the birds and asking the user which one they want more info about may be easiest
# perhaps also organize them by COMMON sightings
# can build on this later on - webpage with pictures, bird songs and information about birds sighted in specific regions
        # can add conservation information, movement information etc.
        # could add the abiity for someone to look up a species and then find what regions of the US they have been seen
        # and list recent sightings
# can even have someone enter a town and then convert that to the county that it is in

def region_sightings(subregion_code):
    response = requests.get(f"https://api.ebird.org/v2/data/obs/{subregion_code}/recent/notable?detail=full", headers = {'X-eBirdApiToken':'f20hu1432los'})
    sighting_list = response.json()
    return sighting_list

species_sightings = region_sightings("US-WA-061")

# pprint.pprint(species_sightings.json())

# print(species_sightings[0]['comName']) # returns mountain bluebird!!! 

# list_species_sighted = [item for item in species_sightings]

# print(list_species_sighted)

# figure out a way to get the local ID from an adress would make search more refined

list_species = []

for sighting in species_sightings:
    list_species.append(sighting['comName'])

number_sightings_species = dict(Counter(list_species))

print(sorted(number_sightings_species.items(), key=lambda x:x[1]), False) ## this works kind of to sort based on sightings

# print(list_species) 
# 
# ## perhaps do a count of the number of sightings per species? can .pop the species
# and add a counter and then perhaps add it to a set that will delete the extras
# OR create a list of each species and add the sighting to the list
# then count the list with len and .pop from each list or something

# may need to pull the species name too to use for other data from other APIs
# can create a dict with key: value that is common_name:species_name to pull from later

# print(set(list_species))