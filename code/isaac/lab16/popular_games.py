'''Most Popular video games'''
# Write a program that displays the data showing the most popular video games between the years of 2020 to 2022.
import requests as req
import pprint as pp
import matplotlib.pyplot as plt

# ask the user for the page and page size
# show max 10 games per page
page = int(input("Which page would you like to view? \n"))
size = int(input("How many searches per page? (max 10 per page) \n"))
    

# create the request.get() function to gather the required data
# data: game name and rating
url = req.get('https://api.rawg.io/api/games?key=48c7cfe6a1ec4e9cbd17cfc91400de82&dates=2020-01-01,2022-04-30',
    params={'page': page, 'page_size': size, 'ordering': '-rating'})

# create a variable containing the data in a json format
game_results = url.json()


# iterate through the results, collecting the following pieces of data
# game name and rating.
for result in game_results['results']:
    name = result['name']
    rating = result['rating']
    prompt = f"\nGame: {name} \n-Rating: {rating}\n"
    # print(prompt)

# create visualization of data gathered
plt.style.use('seaborn')
fig, ax = plt.subplots()

for result in game_results['results']:  # iterate through the data and display the data
    name = result['name']
    rating = result['rating']
    game_name = name
    game_rating = rating
    ax.bar(game_name, game_rating, label=game_name)

plt.xlabel('Game Name', fontsize=10)  # set x label
plt.ylabel('Game Rating', fontsize=10) # set y label
plt.tick_params(axis='x', rotation=10)  # rotate x axis labels
plt.title("Most Popular Games 2020-2022", fontsize=20)  # title and size of title
plt.legend()  # create a legend of each game and the color associated
plt.show()  # show the plot
