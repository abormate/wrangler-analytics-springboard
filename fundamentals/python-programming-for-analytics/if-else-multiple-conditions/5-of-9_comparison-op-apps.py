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

