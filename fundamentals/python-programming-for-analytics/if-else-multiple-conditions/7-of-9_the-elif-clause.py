# ---------------------------------- #
#
# The Elif clause -- conditionals 
#
# ---------------------------------- #

# Learn

"""
Let's do some more specific labeling than just "free" and "not free." We want to label 
the apps using this convention


price	            label
------              ----------------
price == 0	        free
0 < price < 20	    affordable
20 ≤ price < 50	    expensive
price ≥ 50	        very expensive

"""

# Using what we know, we can only do the transformations above using a combination of if statements. 
# This is what the process looks like on the small dataset below:

apps_data = [['Facebook', 0.0], ['Notion', 14.99], ['Astropad Standard', 29.99], 
             ['NAVIGON Europe', 74.99]]

for app in apps_data:
    price = app[1]

    if price == 0.0:
        app.append('free')
    if price > 0.0 and price < 20:
        app.append('affordable')
    if price >= 20 and price < 50:
        app.append('expensive')
    if price >= 50:
        app.append('very expensive')

print(apps_data)

# Output
# [['Facebook', 0.0, 'free'], ['Notion', 14.99, 'affordable'], ['Astropad Standard', 29.99, 'expensive'], 
# ['NAVIGON Europe', 74.99, 'very expensive']]

"""
When an app is free, price == 0.0 evaluates to True and app.append('free') executes. Then the computer 
continues to do redundant operations - it checks for the following

"""

# price > 0 and price < 20
# price >= 20 and price < 50
# price >= 50

"""
We already know the three conditions above evaluate to False once we determine that price == 0.0 is True. 
To stop the computer from doing redundant operations, we can use elif clauses

"""

apps_data = [['Facebook', 0.0], ['Notion', 14.99], ['Astropad Standard', 29.99], 
             ['NAVIGON Europe', 74.99]]

for app in apps_data:
    price = app[1]

    if price == 0.0:
        app.append('free')
    elif price > 0.0 and price < 20:
        app.append('affordable')
    elif price >= 20 and price < 50:
        app.append('expensive')
    elif price >= 50:
        app.append('very expensive')

print(apps_data)

# Output
# [['Facebook', 0.0, 'free'], ['Notion', 14.99, 'affordable'], ['Astropad Standard', 29.99, 'expensive'], 
# ['NAVIGON Europe', 74.99, 'very expensive']]

# The code within the body of an elif clause executes only under the following circumstances

