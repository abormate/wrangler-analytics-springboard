# ------------------------------------- #
#
# Find average of gaming apps in App Store
#
# ------------------------------------- #

# Learn
# --------------- #

"""
So far, we've used the == and != operators only with integers and floats. We can also use them with 
other data types, such as strings or lists
"""

print('Games' == 'Music')
print('Games' != 'Music')

# Output 
False
True

# --------------- #

print([1,2,3] == [1,2,3])
print([1,2,3] == [1,2,3,4])

# Output
True
False

# ---------------- #

"""
This enables us to answer more questions about our dataset, like the following:

-- What's the average rating for gaming apps?
-- What's the average rating for non-gaming apps?
"""

# Note that the prime_genre column describes the app genre, and the genre of gaming apps is encoded as 'Games'

# image screencapture for "apps genre" --> https://prnt.sc/rMt0WORFqEpe 

