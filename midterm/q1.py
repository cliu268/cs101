# Swapping variables

# Time Limit: 1s   Memory Limit: 256M

# Description
# Given two integer numbers X and Y. Assign the greater value to X and smaller number to Y. ( Swapping them if necessary. )

# Input
# Two integers X and Y. 

# Output
# First X then Y in seperate lines.

# Sample Input
# 4 5

# Sample Output
# 5
# 4
n, m = map(int, input().split())
if n > m:
    print(n, m)
else:
    print(m, n)