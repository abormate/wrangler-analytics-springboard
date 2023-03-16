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

"""
-- -- The preceding if statement (or the other preceding elif clauses) resolves to False; and

-- -- The condition specified after the elif keyword evaluates to True

"""

# In our case above, if price == 0.0 is True, the computer executes app.append('free') and moves 
# forward without executing any of the following elif clauses

"""
If price > 0.0 and price < 20 is True, then app.append('affordable') executes, and the remaining two 
elif clauses are disregarded. If price >= 20 and price < 50 is True, then app.append('expensive') 
executes and the last elif clause is disregarded

"""

# ----------------------------------- #
#
# Practice - Activity 
#
# ----------------------------------- #

"""
The app_ratings variable provided in the code editor includes average user rating information for a 
few apps. Using if and elif clauses, append a statement that describes how each app rating compares 
to the overall average user rating of the entire AppleStore.csv dataset, which is 3.52

"""

# Inside the for loop, complete the following:

"""
-- -- If the app rating is less than 3.0, then label the app as "below average" by appending the string 
      'below average' to the current iteration variable.

-- -- Else if the app rating is greater than or equal to 3.0 and below 4.0, then label the app as 
      "roughly average" by appending the string 'roughly average' to the current iteration variable.

-- -- Else if the app rating is greater than or equal to 4.0 label the app "better than average" by 
       appending the string 'better than average' to the current iteration variable

"""

# Print app_ratings to see the results

app_ratings = [['Facebook', 3.5], ['Notion', 4.0], ['Astropad Standard', 4.5], ['NAVIGON Europe', 3.5]]

for app in app_ratings:
    rating = app[1]

    if rating < 3.0:
        app.append("below average")
    elif rating >= 3.0 and rating < 4.0:
        app.append("roughly average")
    elif rating >= 4.0:
        app.append("better than average")
    
print(app_ratings)