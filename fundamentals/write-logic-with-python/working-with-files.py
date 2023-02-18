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

'''
open('AppleStore.csv') returned the output <_io.TextIOWrapper name='AppleStore.csv' mode='r' encoding='UTF-8'>. The output is an object. 
For now, all we have to keep in mind is that the AppleStore.csv file will open once open('AppleStore.csv') has finished running.

Once we've opened the file, we read it in using a function called reader(). We import the reader() function from the csv module using 
the code from csv import reader (a module is a collection of functions and variables).
'''

opened_file = open('AppleStore.csv')

from csv import reader
read_file = reader(opened_file)
print(read_file)

#
# Output from above code
#

<_csv.reader object at 0x7f55b0a379e0>

#
'''
Just like open('AppleStore.csv'), reader(opened_file) returned an object. Now that we've read the file, we can transform it into 
a list of lists using the list() function:
'''
#
#
opened_file = open('AppleStore.csv')

from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

#
#
'''
The apps_data variable above is a list of lists, and it stores a dataset of 7,197 rows and 16 columns. Below, we print only the 
first five rows of apps_data by using list slicing (we colored the output of each list differently to help you read the output more easily):
'''
#
#
'''
Although there are 7,197 rows (apps) in our dataset, len(apps_data) indicates there are 7,198 rows because it also considers the header row, 
which describes the column names (the first row).
'''
#
#
#

opened_file = open('AppleStore.csv')

from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

print(len(apps_data))

#
# Output
#

7198

'''
As a side note, the AppleStore.csv file is currently located on our servers. In a separate lesson, we'll help you set up your own environment 
locally — you'll be able to run Python code and open the AppleStore.csv on your own local computer.
'''
