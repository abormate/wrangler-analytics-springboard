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

# Output
[['Call of Duty: Zombies', 5.0, 'not free'], ['Facebook', 0.0, 'free'], ['Instagram', 0.0, 'free'], 
 ['Temple Run', 0.0, 'free']]

"""
In the code above, we iterated through the apps_data list of lists and for each iteration we completed 
the following:

-- We saved the price value to a variable named price.
-- If price == 0.0, we appended the string 'free' to the list app (app is the iteration variable).
-- If price != 0.0, we appended the string 'not free' to the list app

"""

"""
For each iteration, the computer checked whether price == 0.0 and price != 0.0. After we find out an 
app is price == 0.0, we don't need to check price != 0.0 for the same app.

In our small dataset above, we have three free apps. The computer evaluated price == 0.0 as True three 
times and then it checked the price != 0.0 for the same number of times. This means that the computer 
performed three redundant operations -- it still evaluated price != 0.0 while knowing that price == 0.0 is 
True.

If we have a dataset with 5,000 free apps, this means 5,000 redundant operations. We can avoid this 
redundancy by combining an if statement with an else clause

"""

apps_data = [['Call of Duty: Zombies', 5.0], ['Facebook', 0.0], ['Instagram', 0.0], ['Temple Run', 0.0]]

for app in apps_data:
    price = app[1]

    if price == 0.0:
        app.append('free')
    else:
        app.append('not free')

print(apps_data)

# Output 
[['Call of Duty: Zombies', 5.0, 'not free'], ['Facebook', 0.0, 'free'], ['Instagram', 0.0, 'free'], 
 ['Temple Run', 0.0, 'free']]



# The code within the body of an else clause executes only if the if statement that precedes it 
# resolves to False

if False:
    print(1)
else:
    print(2)

# Output 
2

# ---------- #

if True:
    print(1)
else:
    print(2)

# Output 
1

# Here's an example that's like our example above

price = 5

if price == 0:
    print('free')
else:
    print('not free')

# Output
# not free

price = 0

if price == 0:
    print('free')
else:
    print('not free')

# Output
# free

"""
In our example above (the example at the beginning of this screen), the code within the body of the else 
clause executes only if price == 0.0 evaluates to False. If price == 0.0 is True, then the code 
app.append('free') executes and the computer moves forward without executing the else clause.

Note that we must combine an else clause with a preceding if statement. We can have an if statement 
without an else clause, but we can't have an else clause without a preceding if statement

"""
"""
else:
    print(1)

When we combine a statement with a clause, we create a compound statement - combining an if statement 
with an else clause makes up a compound statement

"""

# -------------------------------- #
#
# Practice - Exercise 
#
# -------------------------------- #

"""
1. Complete the code in the editor to label each app as "free" or "not free" depending on its price.

-- Inside the for loop, complete the following:

-- -- If the price of the app is 0.0, then label the app as "free" by appending the string 'free' to the 
current iteration variable.

-- -- Else, label the app "not free" by appending the string 'not free' to the current iteration variable. 
Don't write 'not_free' for 'not free'

-- By adding labels to the end of each row, we basically created a new column. Name this column 
"free_or_not" by appending the string 'free_or_not' to the first row of the apps_data data set. 
Do this outside the for loop


2. Print the header row and the first five rows to see some of the changes we made

"""

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

for app in apps_data[1:]:
    price = float(app[4])
    if price == 0.0:
        app.append("free")
    else:
        app.append("not free")
apps_data[0].append("free_or_not")

print(apps_data[0:5])