# ------------------------------------ #
#
# Comparison Operator Applications with Python
#
# ------------------------------------ #

# Learn 
# Comparison operators allow us to answer more advanced questions about our dataset
"""
questions such as...

1. How many apps have a rating of 4.0 or greater?
2. What is the average rating of the apps that have a price greater than $9?
3. How many apps have a price greater than $9?
4. How many apps have a price less than or equal to $9?

"""

# Using what we know, we can answer the first question in at least two ways.

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

apps_4_or_greater = []

for row in apps_data[1:]:
    rating = float(row[7])
    if rating >= 4.0:
        apps_4_or_greater.append(rating)

print(len(apps_4_or_greater))

# Output
4781

# Above, we did the following:
"""
-- Initialized an empty list named apps_4_or_greater.
-- Looped through apps_data[1:], and for every iteration, we:

-- -- Stored the rating value as a float to a variable named rating.
-- -- Appended the rating to apps_4_or_greater if the value stored in rating was greater than or equal 
to 4.0.


-- Measured the length of the apps_4_or_greater list to find out the number of apps that have a rating 
of 4.0 or greater.

-- -- After the loop, the apps_4_or_greater list only stores the ratings of the apps that were rated 4.0 
or better. The list apps_4_or_greater has 4,781 ratings that are 4.0 or greater, which means that there 
are 4,781 apps that have a rating of 4.0 or greater.

"""

"""
We can also use another approach to answer the question: we initialize a variable with a value of 0 
and then increment that variable by 1 each time we find a rating of 4.0 or greater:

"""

n_of_apps = 0

for row in apps_data[1:]:
    rating = float(row[7])
    if rating >= 4.0:
        n_of_apps = n_of_apps + 1

print(n_of_apps)

# Output
4781

# Above, we did the following:
"""

-- Initialized a variable n_of_apps with a value of 0.
-- Looped through apps_data[1:], and for every iteration, we did the following:

-- -- Stored the rating value as a float to a variable named rating.
-- -- Incremented the value of n_of_apps by 1 if the value stored in rating was greater than or equal to 4.0.

-- Printed the value of n_of_apps to determine the number of apps with a rating of 4.0 or greater.
   n_of_apps was incremented by 1 during the loop every time a rating was 4.0 or greater. The value of 
   n_of_apps is 4,781 after the looping, which means that 4,781 ratings are 4.0 or greater. Each rating 
   belongs to an app, so this means that there are 4,781 apps that have a rating of 4.0 or greater.

"""

"""

Now let's answer the other three questions:

-- What is the average rating of the apps that have a price greater than $9?
-- How many apps have a price greater than $9?
-- How many apps have a price less than or equal to $9?

"""

# ----------------------------------- #
#
# Practice - Exercise - Hands on
#
# ----------------------------------- #

"""
1. Compute the average rating of the apps that have a price greater than $9.

-- -- Using a for loop, isolate the ratings of all the apps that have a price greater than $9. When you 
iterate over apps_data, don't include the header row.

-- -- Find the average value of these ratings and assign the result to a variable named avg_rating

2. Determine how many apps have a price greater than $9 and assign the result to a variable named 
n_apps_more_9. You can use the list of ratings from the previous question to find the answer.

3. Determine how many apps have a price less than or equal to $9 and assign the result to a variable 
named n_apps_less_9. The list of ratings from the first question can help you find a quick answer

"""

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

app_rating = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    
    if price > 9.0:
        app_rating.append(rating)

avg_rating = sum(app_rating)/len(app_rating)

n_apps_more_9 = len(app_rating)

