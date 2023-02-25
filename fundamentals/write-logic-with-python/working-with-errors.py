# -------------------------- #
#
#  Other kinds of errors in Python
#
# -------------------------- #

'''
Now we'll move on to calculating the average rating for the dataset 
that has 7,197 rows. Remember, first we need to open the file AppleStore.csv 
and transform it into a list of lists. Notice that the first list contains 
the titles in the header row of the dataset:
'''

from csv import reader

opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
apps_data = list(read_file)

'''
Output
7198
[['id', 'track_name', 'size_bytes', 'currency', 'price', 'rating_count_tot', 
'rating_count_ver', 'user_rating', 'user_rating_ver', 'ver', 'cont_rating', 
'prime_genre', 'sup_devices.num', 'ipadSc_urls.num', 'lang.num', 'vpp_lic'], 
['284882215', 'Facebook', '389879808', 'USD', '0.0', '2974676', '212', '3.5', 
'3.5', '95.0', '4+', 'Social Networking', '37', '1', '29', '1'], ['389801252', 
'Instagram', '113954816', 'USD', '0.0', '2161558', '1289', '4.5', '4.0', '10.23', 
'12+', 'Photo & Video', '37', '0', '29', '1'], ['529479190', 'Clash of Clans', 
'116476928', 'USD', '0.0', '2130805', '579', '4.5', '4.5', '9.24.12', '9+', 
'Games', '38', '5', '18', '1'], ['420009108', 'Temple Run', '65921024', 'USD', 
'0.0', '1724546', '3842', '4.5', '4.0', '1.6.2', '9+', 'Games', '40', '5', '1', 
'1']]
'''

'''
Unfortunately, calculating the average rating for the dataset isn't 
straightforward because there are some errors we'll encounter. For 
example, if we use the technique we learned and loop over apps_data to 
get the rating sum, we'll get a TypeError:
'''

rating_sum = 0
for row in apps_data:
    rating = row[7]
    rating_sum = rating_sum + rating

# Output 
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

'''
This error happens because the first row of apps_data doesn't contain numbers 
(it describes column names). In the loop body, we assign the value of row[7] 
to the rating variable, and then we add rating to rating_sum. But for the first 
iteration of the loop, row[7] takes the string value 'user_rating' (which is 
a column name). This means that running rating_sum + rating is equivalent to 0 
+ 'user_rating', which causes a TypeError because we can't add strings and 
integers.
'''

# Theoretically, we have 2 solutions for this error.

# 1st solution
'''
1st solution) -- We remove the first row from apps_data, and then we start the 
iteration over. We do that by doing the following:

-- -- Saving the header row to a separate variable named header
-- -- Saving apps_data[1:] back to apps_data — apps_data[1:] is a list slice 
that excludes the first row (the header row)

'''

# 2nd solution
'''
We iterate directly over apps_data[1:], which is a list slice that 
excludes the first row.
'''

header = apps_data[0]
apps_data = apps_data[1:]

rating_sum = 0
for row in apps_data:
    rating = row[7]
    rating_sum = rating_sum + rating

# Output
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

rating_sum = 0
for row in apps_data[1:]:
    rating = row[7]
    rating_sum = rating_sum + rating

# Output
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

"""
We got the same error. Upon inspection of some of the rows in apps_data, 
we see that quotation marks surround all the values, which suggests they 
are strings. Once again, the error is a result of trying to add a string 
to an integer.
"""

print(apps_data[1])
print(apps_data[1][7])
print(type(apps_data[1][7]))

# Output
# ['284882215', 'Facebook', '389879808', 'USD', '0.0', 
# '2974676', '212', '3.5', '3.5', '95.0', '4+', 
# 'Social Networking', '37', '1', '29', '1']
# 3.5
# <class 'str'>

# Practice exercise
"""
This is an experimentation screen. There is no answer-checking. 
Use this screen to explore the errors highlighted above on your own. 
We've opened the file and read the data into Python for you. We've also 
included for the first error we saw above.
"""


from csv import reader

opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
apps_data = list(read_file)

rating_sum = 0
for row in apps_data[1:]:
    rating = float(row[7])
    rating_sum = rating_sum + rating
print(rating_sum)

'''
To address the errors, we need to convert strings to integers or floats (decimal numbers) using the 
int() or float() functions, respectively. The ratings are expressed as decimal points, so we'll convert 
them to floats using the float() function.
'''

# Exercise - dealing with errors
'''
1. Initialize a variable named rating_sum with a value of zero.

2. Loop through the apps_data[1:] list of lists (make sure you don't include the header row). 
For each of the 7,197 iterations of the loop (for each row in apps_data[1:]), do the following:

-- -- Extract the rating of the app, and store it to a variable named rating (the rating has the 
index number 7). Convert the rating value from a string to a float using the float() function.

-- -- Add the value stored in rating to the current value of rating_sum and assign the result back 
to rating_sum.

3. Divide the rating sum (stored in rating_sum) by the number of ratings to get an average value. 
Store the result in a variable named avg_rating.
'''




