# ----------------------- #
#
# "If" Conditional Statements
#
# ----------------------- #

# Learn 
# ------------------------# 

'''
To isolate only the ratings of the free apps, we need to add a condition to our code. Specifically, 
we want to add a rating to the ratings list only if the price equals 0.0:
'''

# Follow link: Image screenshot from learning module --->> https://prnt.sc/tEtesNX9ruP2

'''
To implement the condition above (If the price equals 0.0, then do:) in our code, 
we can use an if statement:
'''

# Follow Link: Screencapture ---->> https://prnt.sc/9Y-sUqA2mwaa 

# In the example above, we iterate over the apps_data[1:], and for each iteration, 
# complete the following:

'''
-- -- Assign the rating as a float to a variable named rating.

-- -- Assign the price as a float to a variable named price. (The price also comes as a string, 
so we need to convert it to a float.)

-- -- If the price equals 0.0, we append the rating to the ratings list (if the price is 0.0, 
then it means the app must be free). Whenever price doesn't equal 0.0, the code ratings.append(rating) 
doesn't execute.
'''

# Here are a few things to notice about the if statement: