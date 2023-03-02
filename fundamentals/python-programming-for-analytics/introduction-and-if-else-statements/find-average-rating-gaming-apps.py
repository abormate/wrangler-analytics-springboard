# ------------------------------------- #
#
# Find average of gaming apps in App Store
#
# ------------------------------------- #

# Learn
# --------------- #

"""
So far, we've used the == and != operators only with integers and floats. We can also use them with 
other data types, such as strings or lists
"""

print('Games' == 'Music')
print('Games' != 'Music')

# Output 
False
True

# --------------- #

print([1,2,3] == [1,2,3])
print([1,2,3] == [1,2,3,4])

# Output
True
False

# ---------------- #

"""
This enables us to answer more questions about our dataset, like the following:

-- What's the average rating for gaming apps?
-- What's the average rating for non-gaming apps?
"""

# Note that the prime_genre column describes the app genre, and the genre of gaming apps is encoded as 'Games'

# image screencapture for "apps genre" --> https://prnt.sc/rMt0WORFqEpe 

"""
To compute the average rating of gaming apps, we can use the same approach we used on the previous 
screen when we computed the average rating of free and non-free apps. In the code example below, 
we do the following:

-- Initialize an empty list named games_ratings.
-- Loop through apps_data[1:], where apps_data is a list of lists that stores our dataset. For each iteration, we do the following:

-- -- Assign the rating as a float to a variable named rating.
-- -- Assign the genre to a variable named genre and the genre will be saved as a string.
-- -- Append the rating value stored in rating to the list games_ratings if the value in genre is equal to the string 'Games'.

-- Compute the average rating of gaming apps and assign the result to avg_rating_games.

-- Print avg_rating_games

"""

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

games_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]

    if genre == 'Games':
        games_ratings.append(rating)

avg_rating_games = sum(games_ratings) / len(games_ratings)
print(avg_rating_games)

# Output
3.6850077679958573

# ------------------------------------------------ #

# Practice - Exercise

# ------------------------------------------------ #

# Instructions 
'''
Using the same techniques in the diagram above, compute the average rating of non-gaming apps.

1. Initialize an empty list named non_games_ratings.

2. Loop through the apps_data list of lists (make sure you don't include the header row). 
   For each iteration of the loop, do the following:

-- -- Assign the rating of the app as a float to a variable named rating (the index number of the rating 
       column is 7).

-- -- Assign the genre of the app to a variable named genre (index number 11).

-- -- If the genre is not equal to 'Games', append the rating to the non_games_ratings list.

3. Compute the average rating of non-gaming apps and assign the result to a variable named 
    avg_rating_non_games.

4. Optional exercise: compare the average rating of gaming apps (3.69) with the average rating of 
    non-gaming apps. Why do you think we see this difference?

'''

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

non_games_ratings = []

for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    if genre != 'Games':
        non_games_ratings.append(rating)

avg_rating_non_games = sum(non_games_ratings)/len(non_games_ratings)
print(avg_rating_non_games)