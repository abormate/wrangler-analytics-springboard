# ------------------------------------ #
#
# Recap and Multiple Conditions
#
# ------------------------------------ #

"""
So far, we've only worked with single conditions, like the following:

If price equals 0.0 (if price == 0)
If genre equals "Games" (if genre == 'Games')
Single conditions won't allow us to answer more advanced questions, like these:

What's the average rating of free gaming apps?
What's the average rating of not-free gaming apps?
What's the average rating of free non-gaming apps?
What's the average rating of not-free non-gaming apps?


Fortunately, we can combine two or more conditions together into a single if statement using the and 
keyword. In the two diagrams below, we can use and to simultaneously check whether an app is both free 
and has a gaming genre.

"""

app_1_price = 0
app_1_genre = 'Games'

if app_1_price == 0 and app_1_genre == 'Games':
    print('This is a free game!')

print(app_1_price == 0 and app_1_genre == 'Games')

# Output
# This is a free game!
# True

# ------------------------- #

# Example 2

app_2_price = 19
app_2_genre = 'Games'

if app_2_price == 0 and app_2_genre == 'Games':
    print('This is a free game!')

print(app_2_price == 0 and app_2_genre == 'Games')

# Output
False

# ------------------------- #

"""
Notice above that code like app_1_price == 0 and app_1_genre == 'Games' outputs a single Boolean value.
"""
# illustration diagram --> screenshot image --> https://prnt.sc/bYt8oVys_nCv 

# Python evaluates any combination of Booleans to a single Boolean value:

# Example
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# Output
True
False
False
False

# ------------------------- #

"""
As a rule, when we combine Booleans using and the resulting Boolean is True only if all the 
Booleans are True. If any of the Booleans are False, then the resulting Boolean will be False
"""

print(True and True and True)
print(True and True and True and True)
print(True and True and False)
print(True and True and True and False)

# Output
True
True
False
False

# ---------------------------------- #
#
# Exercises and Practice
#
# ---------------------------------- #

"""
Complete the code in the editor to compute the average rating of free gaming apps.

Inside the for loop, append the rating to the free_games_ratings list if the price equals 0.0 and 
the genre equals 'Games'.

Outside the for loop, compute the average rating of free gaming apps. Assign the result to a variable 
named avg_rating_free_games

"""

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_games_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    genre = row[11]