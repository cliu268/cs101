# Sum of string digits

# Time limit: 0.2 memory limit: 32M
# Description:
# Given an integer N, please find the sum of all the digits of N.
# Try to calculate it with string processing.

# Input:
# An integer N.

# Output:
# An integer.

# Sample input 1:
# 12345

# Sample output 1:
# 15

# Constraints:
# The length of N is less than or equal to 100.
n = tuple(input())
sum = int(0)
for i in n:
    sum += int(i)
print(sum)