#import regular expressions library
import re

#file handler variable
fh = open("regex_sum_373677.txt")

#initial variable is 0
y = 0

#for each x inside regex, find all values that has 1 or more [0-9] characters, using fh variable.read()
for x in re.findall('[0-9]+',fh.read()):
    
    #turn x into integer since the output was initially a string, then add it to previous value
    y = int(x) + y

#print the value
print(y)