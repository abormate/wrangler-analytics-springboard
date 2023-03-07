# ---------------------------------- #
#
# Comparison Operators - Python
#
# ---------------------------------- #

# Learn 

"""
Previously, we used the == and != operators to check if two values are equal. When we check for 
equality, we compare one value to another to determine if they are equal. For this reason, 
we call == and != comparison operators

"""

"""
We can compare value A to value B to determine the following:

-- A is equal to B and vice versa (B is equal to A).
-- A is not equal to B and vice versa.
-- A is greater than B or vice versa.
-- A is greater than or equal to B or vice versa.
-- A is less than B or vice versa.
-- A is less than or equal to B or vice versa.

"""

# In Python, we have special operators for each of the comparison operations above
# Image screencapture >>>---->> |  https://prnt.sc/oR0GIzxX5JO2

"""
As with == and !=, comparing values using any of the comparison operators above will output a 
single Boolean value:

"""

print(8 > 1)
print(8 < 1)
print(30 >= 30)
print(20 <= 19)

# Output
True
False
True
False

"""
The fact that a comparison outputs a single Boolean value allows us to use a comparison inside 
an if statement (remember from the second screen that a Boolean value or an expression that evaluates 
to a Boolean value must follow if):

"""

app_name = 'Ulysses'
app_price = 24.99

if app_price > 20:
    print('This app is expensive!')

print(app_price > 20)

# Output
# This app is expensive!
True

# ---------------------------------- #
#
# Practice Exercise 
#
# ---------------------------------- #

"""
Convert the following statements to Python syntax:

1. If x is greater than z, print x is greater than z.
2. If y is not equal to z, print y is not equal to z.
3. If z is between x and y, print z is between x and y.


We've provided values for x, y and z in the code editor. Assume that y is bigger than x. 
Use these values to verify that only the true statements are printed. For answer checking purposes, 
do not include a period at the end of the statements.

"""

x = -6
y = 14
z = 8.5

if (x > z):
    print("x is greater than z")

if (y != z):
    print("y is not equal to z")

if (z >= x and z <= y):
    print("z is between x and y")


# ------------ END -------------- #