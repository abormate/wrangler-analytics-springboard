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

"""
Notice that we enclosed the genre == 'Social Networking' or genre == 'Games' part within parentheses. 
This helps Python understand the specific logic we want for our if statement.

"""

# We want this logic:
# if (genre == 'Social Networking' or genre == 'Games') and price ==0:

# Not this logic:
# if genre == 'Social Networking' or (genre == 'Games' and price ==0):

"""
If we don't use the parentheses, Python defaults to unwanted results - like incorrectly including 
not-free apps. In the example below, we see that not using parentheses leads us to classifying a 
not-free app as free.

"""

# Image screencapture image for above train of thought | >>>---->>   https://prnt.sc/sxm0CGqKo1W3

"""
Above, we printed 'This gaming or social networking app is free!!' for a not-free app. This is an example of 
a logical error.

"""

"""
In the case of a syntax or runtime error, the computer stops the code from running and raises an error. 
For logical errors, the computer doesn't raise any error - the code runs just fine and the logical error 
is unnoticed. To prevent this, we should pay extra attention to the logic of our code.

"""

# Using parentheses correctly makes a difference:

app_genre = 'Social Networking'
app_price = 100

print((True or False) and False)

if (app_genre == 'Social Networking' or app_genre == 'Games') and app_price == 0:
    print('This gaming or social networking app is free!')

# Output
False

"""
In the code editor on the right, we added the code we used above to extract the ratings for free 
gaming or social networking apps. This code is an example for the exercise below.

"""

# --------------------------------- #
#
# Instructions -- Exercise Practice
#
# --------------------------------- #

