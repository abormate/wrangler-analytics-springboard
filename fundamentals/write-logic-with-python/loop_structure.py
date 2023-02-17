# For Loop structure
#
#
'''
Now that we know how to use for loops to print list elements, let's learn how to use for loops to sum values in a list and store the result. 
To store the results from iterating over a list, we need to learn more about for loop structure. These are the structural parts of a for loop:
'''
# example a-01

a_list = [1, 3, 5]      # iteration variable

for value in a_list:    # iterable variable
  print(value)
  print(value - 1)      # body of the loop


'''
The indented code in the body gets executed the same number of times as elements in the iterable variable. If the iterable variable is a list containing three elements, the indented code in the body gets executed three times. We call each code execution an iteration, so there will be three iterations for a list that has three elements. For each iteration, the iteration variable will take a different value, following this pattern:

For the first iteration, the value is the first element of the iterable (if the iterable is the list [1, 3, 5], then the value will be 1).

For the second iteration, the value is the second element of the iterable (if the iterable is the list [1, 3, 5], then the value will be 3).

For the third iteration, the value is the third element of the iterable (if the iterable is the list [1, 3, 5], then the value will be 5).
''''

# outputs for code example above a-01 
# 1
# 0
# 3
# 2
# 5
# 4

'''
The code outside the loop body can interact with the code inside the loop body. For instance, in the code below, we do the following:

-- Initialize a variable a_sum with a value of zero outside the loop body.
-- We loop (or iterate) over a_list. For every iteration of the loop, we do the following:

-- -- Perform an addition (inside the loop body) between the current value of the iteration variable value and the current value stored in a_sum (a_sum was defined outside the loop body).
-- -- Assign the result of the addition back to a_sum (inside the loop body).
-- -- Print the value of the a_sum variable (inside the loop body). Notice that the value of a_sum changes after each addition. At the end of the loop, a_sum has the value 9, which is equivalent to the sum of the numbers in a_list (1 + 3 + 5).
'''



