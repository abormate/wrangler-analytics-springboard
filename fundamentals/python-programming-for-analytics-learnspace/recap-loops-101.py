# Learn 

"""
In this lesson on conditional statements, we'll learn how to ask more advanced questions about datasets, by using the following tools:

How to use if statements
How to use Boolean values
How to use comparison operators with strings or lists

Let's work with a dataset that stores information for 7,197 mobile apps and we'll ask questions like the following (in regard to average ratings):

What's the average rating of non-free apps?
What's the average rating of free apps?
"""


opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

apps_names = []
for row in apps_data[1:]:
    print()
