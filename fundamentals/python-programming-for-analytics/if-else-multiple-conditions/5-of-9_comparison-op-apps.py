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

