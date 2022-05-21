# Output a number in reverse sequence

# Time limit: 0.2   Memory limit：32M
# Description:
# Given a three-digit number, output the number in reverse sequence. If the reversed number contains a leading 0, 
# remove the 0 from the number (see sample 2).

# Input:
# A three-digit integer.

# Output:
# The reversed integer.

# Sample input 1:
# 123

# Sample output 1:
# 321

# Sample input 2：
# 120

# Sample output 2：
# 21
n= list(input())
n.reverse()
if n[0] == '0':n.remove(n[0])
for row in n: print(row, sep='', end='')