# -------------------------------------------- #
#
# Find average rating of non-free apps from App Store data-set
#
# -------------------------------------------- #

# Learn 
"""
In the diagram below, we created a list of lists named app_and_price, and we want to extract 
the names of the free apps in a separate list. To do that, complete the following
"""

"""
1. Create an empty list named free_apps.

2. Iterate over app_and_price. For each iteration, we do the following:

-- -- Extract the name of the app and assign it to a variable named name.
-- -- Extract the price of the app and assign it to a variable named price.
-- -- Append the name of the app to free_apps (the empty list that we initialized outside the loop) 
      if the price of the app equals 0

"""

app_and_price = [['Facebook', 0], ['Instagram', 0], ['Plants vs. Zombies', 0.99], ['Minecraft: Pocket Edition', 6.99], ['Temple Run', 0], ['Plague Inc.', 0.99]]

free_apps = []
for app in app_and_price:
    name = app[0]
    price = app[1]

    if price == 0:
        free_apps.append(name)

print(free_apps)

"""
The example above will help us understand what we did on the first screen of this lesson, 
where we extracted only the ratings of free apps. The steps we took above are the same as the 
ones we took on the first screen when we used this snippet of code:
"""

ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])

    if price == 0.0:
        ratings.append(rating)

# Above, we completed the following:
"""
-- Looped through a list of lists named apps_data. For every iteration, we completed the following:

-- -- Extracted the rating of the app as a float and assigned it to a variable named rating.
-- -- Extracted the price of the app as a float and assigned it to a variable named price.
-- -- Appended the rating of the app to ratings (an empty list that we initialized outside the loop) 
if the price of the app equals 0

"""



