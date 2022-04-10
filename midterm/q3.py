# Sum of reciprocals

# Time Limit：1s   Memory Limit：256M

# Description
# Given an integer N, output 1+1/2+1/3+...+1/N.（the result should have six digits after decimal point.）

# Input
# An integer N.（1<=N<=1000）

# Output
# One floating number, leaving 6 digits after decimal point.

# Sample Input
# 2

# Sample Output
# 1.500000
n = int(input())
s = 0
for i in range(1, n+1):
    s += 1/i
print("%.6f" %s)