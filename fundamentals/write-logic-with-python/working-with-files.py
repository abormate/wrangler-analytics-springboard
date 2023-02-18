# Learn
# 
# automate data ingestion
'''
We could type each data point and bundle them efficiently into a list of lists. The dataset above, however, has 7,197 rows and 16 columns, 
which amounts to 115,152 (7,197 × 16) data points — typing all that would take us days. We'd also be bound to make typing errors, 
which could lead to wrong data and false conclusions. Fortunately, we can leverage Python to store this dataset as a list of lists 
in a matter of seconds.
'''
'''
A dataset is generally stored as a file in a computer — the dataset above is stored as a file named AppleStore.csv. 
We start by opening the file using the open() function:
'''
#
#
# Open file with open() function:
#

opened_file = open('AppleStore.csv')
print(opened_file)

#
#
# Output

<_io.TextIOWrapper name='AppleStore.csv' mode='r' encoding='UTF-8'>
