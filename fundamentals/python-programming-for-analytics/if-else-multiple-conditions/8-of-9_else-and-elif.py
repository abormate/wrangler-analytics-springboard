# ----------------------------------- #
#
# Else vs Elif
#
# ----------------------------------- #

# Learn 

"""
It's possible to replace the final elif clause with an else clause. For our data, the output would 
be identical. As a reminder, here is what the code looks like with elif as the final clause

"""

apps_data = [['Facebook', 0.0], ['Notion', 14.99], ['Astropad Standard', 29.99], ['NAVIGON Europe', 74.99]]

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