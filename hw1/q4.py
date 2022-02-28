# Operators
# Time limit: 0.2   Memory limit: 32M

# Description
# Given the formula a + b = c, where a and c are known, write your own program to find and output b. 

# Input
# Two integers a and c in a line

# Output
# The integer b

# Sample input:
# 1 3

# Sample output：
# 2
a,c = input().split()
print(int(c) - int(a))