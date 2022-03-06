# Leap year

# Time Limit：0.2s   Memory Limit：32M
 
# Description
# Determine whether a number is a leap year.

# Input
# An integer n. 1<=n<=2018

# Output
# If the number is leap year,ouput "yes",else,ouput "no".

# Sample Input 1
# 2000 
# Sample Output 1
# yes

# Sample Input 2
# 1900 
# Sample Output 2
# no
integer = int(input())
if integer % 400 == 0:
    print("yes")
elif integer % 100 == 0:
    print("no")
elif integer % 4 == 0:
    print("yes")
else:
    print("no")