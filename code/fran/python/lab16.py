# Lab 16 - Mini Capstone (Movie Search)
# Fran Kappes

# This program will take in two search parameters (two actors) 
#   and find what common movie(s) they were both in.

import requests
import pandas as pd
import pprint

### Define functions ###

# Define function that invokes the Search Name API that fetches actor id
def find_actor_id(actor):

    actor_id = ''
    actor_name = ''

    # Make first API call to fetch id for the actor
    search_name_response = requests.get('https://imdb-api.com/en/API/SearchName', params={'apiKey': 'k_qq4vuxy0', 'expression': actor})
    # response = requests.get('https://imdb-api.com/en/API/AdvancedSearch', params={'apiKey': 'k_qq4vuxy0', 'name': actor_1})
   
    # Fetch id from the response, where actor_1 name matches the 'title' response element (where actor name is returned)

    search_name_results = search_name_response.json()['results']     # list of dictionaries
    # pprint.pprint(search_name_response.json())

    # Display actors to user
    for search_name_result in search_name_results:
        if search_name_result['title'].lower() == actor.lower():
            actor_id = search_name_result['id']
            actor_name = search_name_result['title']
            # print(search_name_result['id'],' - ',search_name_result['title']) 
            print(actor_id,' - ',search_name_result['title']) 
        
        # ADD LOGIC TO HANDLE THE CASE WHERE NO NAME MATCHES. In that case,
        #   return the result set back to the user and have them select the actor
        #   "Multiple results returned for your search string. Please enter the id
        #    of the actor you want to search on: "
        # ALSO: Handle the case where you get two records back with the same name (e.g. Al Pacino)

    return actor_id, actor_name


# Define function that invokes the Name API that fetches actor's filmography
def find_actor_films(actor_id):

    # filmography = []

    print("Before second API call...")
    # Make second API call to fetch movies for that actor
    name_response = requests.get('https://imdb-api.com/en/API/Name', params={'apiKey': 'k_qq4vuxy0', 'id': actor_id})

    name_results = name_response.json()['castMovies']     # list of dictionaries

    for name_result in name_results:
        if name_result['role'] == 'Actress' or name_result['role'] == 'Actor':
            if name_result['year']:         # Ignore any films that don't have a release year
                # filmography = name_result['title']
                # film_year = name_result['year']
                print(name_result['title'], ' - ', name_result['year']) 
        # print(name_result['role'])

    # pprint.pprint(response.json())

    # return film_title, film_year

# Define function that inserts actor id, actor name, and filmography (including release year) 
#  into a Pandas DataFrame
def insert_film_info():
    pass


# Define function that finds the movie(s) that both actors were in.
#  Constrain on release year, to ensure that both actors are in the same movie
#  (and not two separate versions of the same movie).
def find_common_movies():
    pass

### Main logic ###

# Initialize loop variable
n = 1
actors = ''

while n < 3:    # CHANGE TO 3  # we want to loop two times

    # Collect actor names from user
    actor = input("What the is first and last name of actor {}? ".format(n))
    # actor_2 = input("What the is first and last name of actor ",n,"? ")

    # Search for actor in IMDB database
    actor_id, actor_name = find_actor_id(actor)
    actors += actor_name  ###  FIX THIS; MIGHT NEED TO DO LIST INSTEAD
    print('actors: ', actors)
    # print('actor_id from function: ', actor_id)
    # print('actor_name from function: ', actor_name)

    # Find all films that actor has been in
    if actor_id:
        films = find_actor_films(actor_id)
    else:
        print('No match found')

    # Insert actor info into Pandas data frame
    ### OR, 

    # Insert filmography into Pandas data frame
    # insert_film_info()

    n += 1

# Find common movies across both actors
# common_movies = find_common_movies()

# Return results
