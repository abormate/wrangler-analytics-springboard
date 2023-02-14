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
