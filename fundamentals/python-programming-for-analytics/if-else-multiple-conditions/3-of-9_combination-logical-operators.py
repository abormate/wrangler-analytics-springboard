# ---------------------------------- #
#
# Combining Logical Operators with Python
#
# ---------------------------------- #

# Learn 
"""
In the previous exercise, we computed the average rating of the apps with a genre that is either 
"Social Networking" or "Games." We can ask even more specific questions, like these:

-- What is the average rating of free apps with a genre that is either "Social Networking" or "Games"?
-- What is the average rating of not free apps with a genre that is either "Social Networking" or "Games"?

"""

"""
To answer the first question, we need to isolate the apps that meet both criteria:

-- Are in either the "Social Networking" or "Games" genre
-- Have a price of 0.0

"""

# To isolate these apps, we can combine or with and in a single if statement:

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_games_social_ratings = []

for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    price = float(row[4])

#    if (genre == 'Social Networking' or genre == 'Games') and price ==0:

