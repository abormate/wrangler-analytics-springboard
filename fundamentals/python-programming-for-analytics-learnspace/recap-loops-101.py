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

"""
To answer these two questions, we need to find a way to separate free apps from non-free or purchase apps, because they are all listed together in our dataset. We must specifically complete the following:

Isolate the ratings for free and non-free apps in separate lists.
Compute the average rating for each list.
"""

# Exercise 
# ------------------------ # 
'''
Complete the code in the editor to find the names for all of the apps in the dataset. The AppleStore.csv is available under the csv tab in the editor to the right.

Inside the for loop, complete the following:
-- -- Assign the name of an app to a variable called name. The name is the second element in each row (the index starts at 0).
-- -- Append the value stored in name to the apps_names list using the list_name.append() function (note the apps_names list is already defined in the code editor) and be careful with indentation.

Print the first 5 elements in apps_names list to display the names of the apps.
'''


opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

apps_names = []
for row in apps_data[1:]:
    print()
