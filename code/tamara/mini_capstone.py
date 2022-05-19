import requests
from collections import Counter

### can also easily add on option to retrieve ALLL species EVER sighted in a region as fun additional option
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

    def __init__(self, species):
        self.species = species

    def species_song(self): # returns a single link for a recording of the species. Returns the download link. If you can find a way to use the download link to play the file through python then the 'file-name' key will give you the mp3 file name.
        response=requests.get(f"https://www.xeno-canto.org/api/2/recordings", params = {'query': f'{self.species}', 'page':'1'})
        species_songs_list = response.json()
        species_song = species_songs_list['recordings'][0]['file']
        return species_song ## can add a parameter for number of songs you want retrieved and then can retrieve multiple songs
    
    def species_image(self):
        # response=requests.get()
        pass ### this is for later when I can find a bird image api, can also make a bird info one as well when I find that kind of API

def regional_code(state_code, county):
    response=requests.get(f"https://api.ebird.org/v2/ref/region/list/subnational2/{state_code}", headers = { 'X-eBirdApiToken': 'f20hu1432los'})
    regional_state_codes = response.json()

    subregion_code = ''
    for region in regional_state_codes:
        if county in region.values():
            subregion_code += region['code']

    return subregion_code ### returns the code for the county enterted by the user and passed in as a paramter

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
    species_names = dict(zip(list_names, list_species))
    
    number_sightings = Counter(list_names) 
    number_sightings_sorted = sorted(number_sightings.items(), key=lambda x:x[1], reverse = True) 
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

    county = input(f"\nWhat county in {state.title()} would you like to search for notable bird sightings in? ").title()

    sightings = (region_sightings(regional_code(state_code, county)))[0] # gives dict of sightings in common name ranked by number of sightings
    species_name = (region_sightings(regional_code(state_code, county)))[1] # gives dict of common name: species name // can be used to retrieve species info from other apis

    print(f"\nIn {county} county over the past 30 days the following notable birds have been reported:") 

    for bird in sightings:
        print(f"\n{bird}: seen {sightings.get(bird)} times")

    while True:
        common_name = input(f"\nWhich type of bird would you like more information on or type 'done' to try another regional search? ") # will need to .lower when looking through dict as well
        if common_name in ['done', 'd', 'exit', 'cancel']:
            break
        else:
            try:
                species = species_name[common_name]
            except KeyError:
                print("That was an invalid entry. Please enter the bird's common name exactly as it is displayed.")
        species_info = Bird(species)
        print(f'\n{common_name} ({species}) song: {species_info.species_song()}')
        another_bird = input(f"\nWould you like to look up the info for another bird sighted in {county} county (y/n)? ")
        if another_bird in ['yes', 'y', 'yeah', 'yep']:
            pass
        else:
            break