# ---------------------------------- #
#
# The Else clause -- conditional
#
# ---------------------------------- #

# Learn
"""
Let's use information from the price column to label each app as "free" or "not free." If the price 
equals 0.0, we want to label the app "free." Otherwise, we want to label it "not free."

Remember that we store our dataset as a list of lists -- each row is a list that describes an app. To 
label the app, we want to add the string 'free' or 'not free' at the end of each list (row). On a 
smaller scale, this is what we want to do (below, we're using just a small extract from our dataset, 
showing just the name and the price of four apps)

"""

apps_data = [['Call of Duty: Zombies', 5.0], ['Facebook', 0.0], ['Instagram', 0.0], ['Temple Run', 0.0]]

for app in apps_data:
    price = app[1]

    if price == 0.0:
        app.append('free')
    if price != 0.0:
        app.append('not free')

print(apps_data)