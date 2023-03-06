# ---------------------------------- #
#
# The "OR" operator - Multiple conditions for If and Else
#
# ---------------------------------- #

# Learn 
# ---------------------------------- #

"""
If we look at the first five apps, we can see in the prime_genre column that Facebook's genre is 
"Social Networking," while the genre for Clash of Clans and Temple Run is "Games"
"""

# Apps data-table --> screencapture --> https://prnt.sc/cYF8E8n8sZ8y
# Apps data-table scrolled horizontally --->> screencapture --->> https://prnt.sc/SJia4Bef7VZ6 

"""
Since social networking apps and games are usually popular, we may want to further investigate this 
category. One thing we might want to determine is the average rating of this category that encompasses 
games and social networking apps.

To do that, we need to isolate the ratings of all the apps whose genre is either "Social Networking" 
or "Games" into a separate list. Then, we can compute the average value using techniques we already know.

If we want to isolate the ratings of these apps using the condition if genre == 'Social Networking' 
and genre == 'Games', we'll end up with an empty list because there's no app with a genre that is 
both "Social Networking" and "Games" — an app can only have one genre.
"""

apps_data = ["csv file with apps data"]
games_social_ratings = []

for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]

    if genre == 'Social Networking' and genre == 'Games':
        games_social_ratings.append(rating)

print(games_social_ratings)
print(len(games_social_ratings))

# Output
[]
0

# ------------------------------------------ #

"""
We need to isolate the rating of an app only if the genre is "Social Networking" or "Games," 
not "Social Networking" and "Games." To account for this difference, we can use or instead of and
"""

apps_data = ["csv file with apps data"]
games_social_ratings = []

for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]

    if genre == 'Social Networking' or genre == 'Games':
        games_social_ratings.append(rating)

print(games_social_ratings[:5])
print(len(games_social_ratings))

# Output
[3.5, 4.5, 4.5, 4.5, 4.5]
4029

# ------------------------------------------ #

"""
We call or and and logical operators. Just like and, or unites two or more Booleans. As we learned 
previously, Python evaluates any combination of Booleans to a single Boolean value
"""

print(True or True)
print(True or False)
print(False or True)
print(False or False)

# Outputs
True
True
True
False

# Another example ------------------------- #

print(True and True)
print(True and False)
print(False and True)
print(False and False)

# Outputs 
True
False
False
False

# ----------------------------------------- #

"""
When we combine Booleans using or, the resulting Boolean is False only if all the Booleans are False. 
If any of the Booleans are True, then the resulting Boolean is True
"""

print(False or False or False)
print(False or False or False or True)

# Outputs
False
True

# ----------------------------------------- #

"""
Returning to our apps example, the condition if genre == 'Social Networking' or genre == 'Games' 
resolves to False when an app's genre is neither "Social Networking" nor "Games." Otherwise, it 
resolves to True.

Now let's practice using the or operator by computing the average rating of the apps with a genre 
of either "Social Networking" or "Games.
"""

# ------------------------------------------ #
#
# Practice exercise
#
# ------------------------------------------ #

# Instructions 
"""
Complete the code in the editor to compute the average rating of the apps with a genre that is either 
"Social Networking" or "Games."

-- -- Inside the for loop, append the rating to the games_social_ratings list if the genre is either 
       'Social Networking' or 'Games'.

-- -- Outside the for loop, compute the average rating of the apps with a genre that is either 
      "Social Networking" or "Games," and assign the result to a variable named avg_games_social
"""

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    if genre == 'Social Networking' or genre == 'Games':
        games_social_ratings.append(rating)

avg_games_social = sum(games_social_ratings)/len(games_social_ratings)
print(avg_games_social)