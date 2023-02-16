# Objective: Work with a for loop to repeat a process and analyze a dataset. And read in a dataset as a list of lists. 
#
#

# For the following, we wanted to calculate the average rating of an app. 
# We currently have 7,197 rows unlike before when we only had 5 rows.
# To do this task, we do the following:

# 1. Retrieve each individual rating
# 2. Sum the ratings
# 3. Divide by the number of ratings.
#

# Sample code for 5 rows:

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Fruit Ninja Classic', 1.99, 'USD', 698516, 4.5]
row_5 = ['Minecraft: Pocket Edition', 6.99, 'USD', 522012, 4.5]

app_data_set = [row_1, row_2, row_3, row_4, row_5]
avg_rating = (app_data_set[0][-1] + app_data_set[1][-1] +
              app_data_set[2][-1] + app_data_set[3][-1] +
              app_data_set[4][-1]) / 5

print(avg_rating)

# data-set source link:
# --> https://www.kaggle.com/ramamet4/app-store-apple-data-set-10k-apps
#
#

# for loop -- contruction, logic
#
#

app_ratings = [3.5, 4.5, 4.5, 4.5, 4.5]

for element in app_ratings:
    print(element)
    
#
#
# Translate the following pattern into Python syntax: for each element in the app_names list, print the app name.
#

app_names = ['Facebook', 'Instagram', 'Clash of Clans', 'Fruit Ninja Classic', 'Minecraft: Pocket Edition']

# Determine average rating of apps in sample data of only 5 rows
# Code a3

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Fruit Ninja Classic', 1.99, 'USD', 698516, 4.5]
row_5 = ['Minecraft: Pocket Edition', 6.99, 'USD', 522012, 4.5]

app_data_set = [row_1, row_2, row_3, row_4, row_5]
avg_rating = (app_data_set[0][-1] + app_data_set[1][-1] +
              app_data_set[2][-1] + app_data_set[3][-1] +
              app_data_set[4][-1]) / 5

print(avg_rating)

# outputs --> 4.3
#
#
#
# The same could be accomplished as on Code a3 -- with for loops 
# Below, we see how we can translate that process into Python syntax and print the result of each iteration:

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Fruit Ninja Classic', 1.99, 'USD', 698516, 4.5]
row_5 = ['Minecraft: Pocket Edition', 6.99, 'USD', 522012, 4.5]

app_data_set = [row_1, row_2, row_3, row_4, row_5]

for row in app_data_set:
    rating = row[-1]
    print(rating)

#
# Output
# 3.5
# 4.5
# 4.5
# 4.5
# 4.5
#

# With only two lines of code, we printed the contents of all five lists in the dataset. 
# Compare that to the following approach with equivalent results:

app_data_set = [row_1, row_2, row_3, row_4, row_5]

print(app_data_set[0])
print(app_data_set[1])
print(app_data_set[2])
print(app_data_set[3])
print(app_data_set[4])





