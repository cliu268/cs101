# Statistics of characters

# Time Limit：1s   Memory Limit：256M
# Description
# Enter a string of characters ended with “?”. Count the number of letters, numbers, and other symbols.

# Input
# Enter a line containing several characters ended with “?”.

# Output
# Three lines, show the number of letters,  numbers and other symbols, exactly as the format in the sample below.

# Sample Input
# ab123!?

# Sample Output
# Letters=2
# Digits=3
# Others=1

# Hint: A space is also counted as a character.
n= input()
l=0
d=0
o=0
for i in n:
    if i!="?":
        if i.isalpha():
            l+=1
        elif i.isdigit():
            d+=1
        else:
            o+=1
print("Letters=%d"%l)
print("Digits=%d"%d)
print("Others=%d"%o)