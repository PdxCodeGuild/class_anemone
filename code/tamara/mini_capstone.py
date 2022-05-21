import requests, re
from bs4 import BeautifulSoup
from collections import Counter

# create dict of 'user state input':'state code for API' to refer to
state_code_dict = {
    'alabama': 'US-AL', 
    'alaska': 'US-AK', 
    'arizona': 'US-AZ', 
    'arkansas': 'US-AR', 
    'california': 'US-CA', 
    'colorado': 'US-CO', 
    'connecticut': 'US-CT', 
    'delaware':'US-DE', 
    'florida':'US-FL', 
    'georgia':'US-GA', 
    'hawaii': 'US-HI', 
    'idaho': 'US-ID', 
    'illinois': 'US-IL', 
    'indiana': 'US-IN', 
    'iowa': 'US-IA', 
    'kansas':'US-KS', 
    'kentucky':'US-KY', 
    'louisiana': 'US-LA', 
    'maine': 'US-ME', 
    'maryland': 'US-MD', 
    'massachusetts': 'US-MA', 
    'michigan':'US-MI', 
    'minnesota':'US-MN', 
    'mississippi':'US-MS', 
    'missouri':'US-MO', 
    'montana':'US-MT', 
    'nebraska':'US-NE', 
    'nevada':'US-NV', 
    'new hampshire':'US-NH', 
    'new jersey':'US-NJ', 
    'new mexico':'US-NM', 
    'new york':'US-NY', 
    'north carolina':'US-NC', 
    'north dakota':'US-ND', 
    'ohio':'US-OH', 
    'oklahoma':'US-OK', 
    'oregon':'US-OR', 
    'pennsylvania': 'US-PA', 
    'rhode island': 'US-RI', 
    'south carolina': 'US-SC', 
    'south dakota':'US-SD', 
    'tennessee': 'US-TN', 
    'texas':'US-TX', 
    'utah':'US-UT', 
    'vermont': 'US-VT', 
    'virginia':'US-VA', 
    'washington':'US-WA', 
    'west virginia':'US-WV', 
    'wisconsin':'US-WI', 
    'wyoming':'US-WY'
}

class Bird:

    def __init__(self, species=None, common=None): # takes in the species (scientific) name and the common name. This class can be added to with more functions in the future for more information on the bird species.
        self.species = species
        self.common = common

    def species_song(self): # returns a single link for a recording of the species.
        response=requests.get(f"https://www.xeno-canto.org/api/2/recordings", params = {'query': f'{self.species}', 'page':'1'})
        species_songs_list = response.json()
        species_song = species_songs_list['recordings'][0]['file']
        return species_song ## can add a parameter for number of songs you want retrieved and then can retrieve multiple songs in future.
    
    def common_coded(self): # takes the common name of the bird entered by the user and converts it to a code that can be red in the URL
        replace_spaces = self.common.replace(' ','-')
        remove_apostrophe = replace_spaces.replace('\'', '')
        remove_parenthesis = re.sub('\(.*\)', '', remove_apostrophe) # will remove the paranthesis and everything in it or return the string if none exist
        remove_dash = remove_parenthesis.strip('-') # remove extra - on the end caused if paranthesis removed
        remove_x = remove_dash.split('-x-') # if it is a hybrid it will split the two crosses into seperate indexes in a list.
        if len(remove_x) == 2: 
            species_code_1 = '' ## This whole section is to copy the last word on the second species and add it to the first species
            species_code_2 = '' ## otherwise the first species would be just ['white-crested', 'golden-crested-sparrow'] for example but after this it will be
            hybrid_list = [] ## 'white-crested-sparrow' which can be used to retrieve an image
            species_2_split = remove_x[1].split('-') ## this WILL cause an error if not all hybrid species are formatted like this
            species_1_split = remove_x[0].split('-')  ## will need further testing with other hybrid species
            type_bird = species_2_split[-1]
            species_1_split.append(type_bird)
            for word in species_1_split:
                species_code_1 += f'{word}-'
            species_code_1 = species_code_1.strip('-')
            for word in species_2_split:
                species_code_2 += f'{word}-'
            species_code_2 = species_code_2.strip('-')
            hybrid_list.append(species_code_1)
            hybrid_list.append(species_code_2)
            return hybrid_list
        elif len(remove_x) < 2:
            return remove_x # returns the common name converted into common_code 

    def __retrieve_image(self, common_code): # function used to retrieve an image of a bird at a given index in the common_code_list (see bird_image())
            response=requests.get(f"https://www.audubon.org/field-guide/bird/{common_code}#photo1")
            page_data = response.text
            data_tree = BeautifulSoup(page_data, 'html.parser') # creates a parse tree to extract data from the html (page_data)
            species_images = []
            for data in data_tree.find_all('img'): # finds all img files in the data tree
                image_files = data['src'] # src is a tag used in html
                if 'bird' in image_files and 'thumbnail' not in image_files:
                    species_images.append(image_files)
            return species_images[0] ### can change this to return the whole list if you want to give user more options on seeing more images 

    def bird_image(self): ## to be used for 'web scrapping' images
        common_code_list = self.common_coded()
        if len(common_code_list) < 2:
            common_code = common_code_list[0]
            species_image = self.__retrieve_image(common_code)
            species_image_list = []
            species_image_list.append(species_image)
            return species_image_list ## return a single image file for the bird
        if len(common_code_list) == 2:
            hybrid_images = []
            common_code_1 = common_code_list[0]
            species_1_image = self.__retrieve_image(common_code_1) # return a single image for the first species in the hybrid bird
            common_code_2 = common_code_list[1]
            species_2_image = self.__retrieve_image(common_code_2) # returns a single image for the second species in the hybrid bird
            hybrid_images.append(species_1_image)
            hybrid_images.append(species_2_image)
            return hybrid_images 

def regional_code(state_code, county):
    response=requests.get(f"https://api.ebird.org/v2/ref/region/list/subnational2/{state_code}", headers = {'X-eBirdApiToken': 'f20hu1432los'})
    regional_state_codes = response.json()
    subregion_code = ''
    for region in regional_state_codes:
        if county in region.values():
            subregion_code += region['code']

    return subregion_code ### returns the code for the county enterted by the user so it can be used to retrieve regional sightings vis the ebird API

# use to retrieve recent notable sightings in a region
def region_sightings(subregion_code):
    response = requests.get(f"https://api.ebird.org/v2/data/obs/{subregion_code}/recent/notable?detail=full", headers = {'X-eBirdApiToken':'f20hu1432los'})
    sighting_list = response.json()

    list_species = []
    for sighting in sighting_list:
        list_species.append(sighting['sciName'])
    list_names = []
    for sighting in sighting_list:
        list_names.append(sighting['comName'])
    species_names = dict(zip(list_names, list_species)) # creates common name : scientific name dict to be referred to for retrieving song. scientific name needed by API.
    
    number_sightings = Counter(list_names) # counts the number of sightings 
    number_sightings_sorted = sorted(number_sightings.items(), key=lambda x:x[1], reverse = True) # sorts based on sightings and reverses it so that most sighted birds are first
    number_sightings_dict = dict(number_sightings_sorted) 

    return [number_sightings_dict, species_names]

while True:
    state = input(f"\nType the name of the state you would like to search for notable bird sightings in or type 'done' to exit: ").lower()
    if state in ['n', 'done', 'exit', 'd']:
        break
    else:
        try:
            state_code = state_code_dict[state]
        except KeyError:
            print(f"\n'{state}' was an invalid state entry please check your spelling and try again.")

    while True:
        county = input(f"\nWhat county in {state.title()} would you like to search for notable bird sightings in? ").title()
    ## this will cause an error if they put an invalid county or if the county name has an ' or if they put 'county' on the end of the name
        try:
            sightings = (region_sightings(regional_code(state_code, county)))[0] # gives dict of sightings in common name ranked by number of sightings
            species_name = (region_sightings(regional_code(state_code, county)))[1] # gives dict of common name: species name
            break
        except TypeError:
            print("\nThat was an invalid county entry. Please check your spelling and try again. Do NOT add 'county' on to the end of the name.")
    
    print(f"\nIn {county} county over the past 30 days the following notable birds have been reported:\n") 

    for bird in sightings:
        print(f"{bird}: seen {sightings.get(bird)} times")

    while True:
        common_name = input(f"\nWhich type of bird would you like more information on or type 'done' to try another regional search? ") # will need to .lower when looking through dict as well
        if common_name in ['done', 'd', 'exit', 'cancel']:
            break
        else:
            try:
                species = species_name[common_name]
            except KeyError:
                print("\nThat was an invalid entry. Please enter the bird's common name exactly as it is displayed (copy and paste).")
                ### it would be nice to user proof this more
        species_info = Bird(species, common_name)
        try:
            print(f'\n{common_name} (species: {species})\n\nsong: {species_info.species_song()}')
        except IndexError:
            print(f'\n{common_name} (species: {species})\n\nsong: There are no recordings on file for this species') ## common with hybrid birds can return both parent species songs in future instead.
        bird_image_list = species_info.bird_image()
        if len(bird_image_list) < 2:
            print(f'\nimage: {bird_image_list[0]}')
        if len(bird_image_list) == 2:
            print(f'\n{common_name} is a hybrid bird. Here are two images from the two species it is crossed with:\n\nimage 1: {bird_image_list[0]}\nimage 2: {bird_image_list[1]}')
        another_bird = input(f"\nWould you like to look up the info for another bird sighted in {county} county (y/n)? ")
        if another_bird in ['yes', 'y', 'yeah', 'yep']:
            pass
        else:
            break

        ## Overall seems to work but needs more testing with different birds and seeing if it goes
        ## to the right image/audio file

        
