# Lab 16 - Mini Capstone (Movie Search)
# Fran Kappes

#   This program will take in two search parameters (actor names) 
#   and find what common movie(s) both actors were in.
#   It requires calls to two different IMDB APIs (SearchName and Name).
#   Actor filmographies are loaded into a Pandas DataFrame and then 
#   queried to find duplicate movie titles across both actors.

import requests
import pandas as pd
import re
import pprint

### Define functions ###

# Define find_actor_id function which invokes the Search Name API that fetches actor id
# based on actor name.

def find_actor_id(actor):

    actor_id = ''
    actor_name = ''

    # Make first API call to fetch id for the actor
    search_name_response = requests.get('https://imdb-api.com/en/API/SearchName', params={'apiKey': 'k_qq4vuxy0', 'expression': actor})
    
    # Fetch id from the response, where actor_1 name matches the 'title' response element (where actor name is returned)
    search_name_results = search_name_response.json()['results']     # list of dictionaries
    
    # pprint.pprint(search_name_response.json())        ### TEST

    # Determine if there is an actor that matches the search string.
    # Convert API and user strings to uniform case and also strip spaces for a better comparison
    for search_name_result in search_name_results:
        # print(re.sub('[\W_]+', '', search_name_result['title'].lower()))  ### TEST

        if re.sub('[\W_]+', '', search_name_result['title'].lower()) == re.sub('[\W_]+', '', actor.lower()):

            actor_id = search_name_result['id']
            actor_name = search_name_result['title']

            # print(actor_id,' - ',search_name_result['title'])     ### TEST
        
    return actor_id, actor_name


def find_actor_films(actor_id, actor_name, filmography_df):
    
    # Make second API call to fetch movies for that actor
    name_response = requests.get('https://imdb-api.com/en/API/Name', params={'apiKey': 'k_qq4vuxy0', 'id': actor_id})

    name_results = name_response.json()['castMovies']     # list of dictionaries

    for name_result in name_results:
        films = []

        if name_result['role'] == 'Actress' or name_result['role'] == 'Actor':
            if name_result['year']:         # Ignore any films that don't have a release year

                # print(actor_name, name_result['title'], ' - ', name_result['year'])     ### TEST

                # Populate dataframe with actor's filmography
                temp_df = pd.DataFrame({'Actor ID': [actor_id],
                                    'Actor Name' : [actor_name],
                                    'Movie Title' : [name_result['title']],
                                    'Release Year' : [name_result['year']]})

                filmography_df = pd.concat([filmography_df, temp_df], ignore_index = True, axis = 0)

    return filmography_df          


### Main logic ###

# Create empty filmography data frame
filmography_df = pd.DataFrame(columns = ['Actor ID' , 'Actor Name', 'Movie Title' , 'Release Year'])

# Initialize variables
n = 1           # loop variable
actors = []     

# Main loop that prompts user for names of actors and looks up their filmography

while n < 3:    # we want to loop two times

    # Collect actor names from user
    actor = input("What is the first and last name of actor {}? ".format(n))

    # Search for actor in IMDB database
    actor_id, actor_name = find_actor_id(actor)
    actors.append(actor_name)  

    # Find all films that actor has been in
    if actor_id:
        match = 1
        films = find_actor_films(actor_id, actor_name, filmography_df)
        filmography_df = films
    else:
        print('No match found for ',actor)
        match = 0
        break
    
    n += 1


# Find common movies across both actors
# Constrain on release year, to ensure that both actors are in the same movie
# (and not two separate versions of the same movie).
common_films = filmography_df[filmography_df.duplicated(['Movie Title', 'Release Year'])]
common_films = common_films['Movie Title']


# Return results
if match == 1:
    if common_films.empty:
        print('\n')
        print(actors[0],'and',actors[1],'were not in any movies together\n')
        print('\n')
    else:
        print('\n')
        print(actors[0],'and',actors[1],'were in these movies together:\n')
        print(common_films.to_string(index=False))    # do not print dataframe index
        print('\n')
    