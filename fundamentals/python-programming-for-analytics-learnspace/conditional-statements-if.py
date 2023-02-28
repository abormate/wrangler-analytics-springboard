# ----------------------- #
#
# "If" Conditional Statements
#
# ----------------------- #

# Learn 
# ------------------------# 

'''
To isolate only the ratings of the free apps, we need to add a condition to our code. Specifically, 
we want to add a rating to the ratings list only if the price equals 0.0:
'''

# Follow link: Image screenshot from learning module --->> https://prnt.sc/tEtesNX9ruP2

'''
To implement the condition above (If the price equals 0.0, then do:) in our code, 
we can use an if statement:
'''

# Follow Link: Screencapture ---->> https://prnt.sc/9Y-sUqA2mwaa 

# In the example above, we iterate over the apps_data[1:], and for each iteration, 
# complete the following:

'''
-- -- Assign the rating as a float to a variable named rating.

-- -- Assign the price as a float to a variable named price. (The price also comes as a string, 
so we need to convert it to a float.)

-- -- If the price equals 0.0, we append the rating to the ratings list (if the price is 0.0, 
then it means the app must be free). Whenever price doesn't equal 0.0, the code ratings.append(rating) 
doesn't execute.
'''

# Here are a few things to notice about the if statement:

"""
-- -- The if statement starts with if, it continues with price == 0.0 and it ends with :

-- -- Use the == operator to check if the price is equal to 0.0. Don't confuse == with = (= is a variable 
assignment operator in Python; we use it to assign values to variables, it doesn't tell us anything 
about equality).

-- -- Indent ratings.append(rating) four spaces to the right relative to the if statement.
"""

# ------------------------------------- #

# Exercise -- Activity 

# ------------------------------------- #

# Directive: 
# Complete the code in the editor to find the average rating for free apps.

"""
1. Inside the for loop, complete the following:

-- -- Assign the price of an app as a float to a variable named price. The price is the fifth element 
in each row (the index starts at 0).

-- -- If price == 0.0, append the value stored in rating to the free_apps_ratings list using the 
list_name.append() function (note the free_apps_ratings is already defined in the code editor).


2. Outside the for loop body, compute the average rating of free apps. Assign the result 
to a variable named avg_rating_free. The ratings are stored in the free_apps_ratings list.

"""

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    if price == 0.0:
        free_apps_ratings.append(rating)

avg_rating_free = sum(free_apps_ratings)/len(free_apps_ratings)
print(avg_rating_free)