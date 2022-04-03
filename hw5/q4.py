# Pyramid graphics

# Time limit：0.2   Memory limit：32M
# Description：
# Please write a program to output Pyramid shape graphics.

# Input：
# Multiple test data, each input is an integer n (1 < = n < 9).

# Output：
# Pyramid made of  *, with the size n, as in the samples

# Sample input：
# 1
# 3

# Sample output：
# *
#   *
#  ***
# ***** 

# Hint：
# This sample has 2 tests.
# First one is 1, so the output is a pyramid of size 1 using *
# the second test is 3, so the output is a pyramid of size 3
lines = []
while True:
    try:
        line = int(input())
        lines.append(line)
    except EOFError:
        break

# lines = list(int(x) for x in input().split('\n'))
for x in lines:
    for i in range(1, x+1):
        line = ' ' * (x-i) + '*' * (2*i - 1)
        print(line)
