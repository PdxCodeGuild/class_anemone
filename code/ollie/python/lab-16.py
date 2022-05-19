' Lab 16 - Mini Capstone '

""" The purpose of this program is to calculate the distace between
any two country capitals in the world, in the user's unit of choice."""

from geopy import distance                                  # to calculate distance on the surface of the Earth
import pandas as pd                                         # to load capital cities dataset 

data = pd.read_csv("concap.csv")                          # load dataframe with capitals

# renaming columns in capitals file to names I can work with easily
data.rename(columns={"countryName": "Country", "capitalName": "Capital", "capitalLatitude": "Lat", "capitalLongitude": "Long", "countryCode": "Code", "continentName": "Continent"}, inplace=True)
data.sample(3)
