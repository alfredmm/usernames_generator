# Creating User Names from First and Last Names
# Using Files
# Add random int (100 to 999) at the end of each user name

import random

infile = open("names.txt", "r")
outfile = open("usernames.txt", "w")

for line in infile:
    first, last = line.split()
    username= (first+last).lower()+str(random.randint(100,999))
    print(username, file=outfile)

infile.close()
outfile.close()
    
