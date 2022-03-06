# Math Test 

# Description:
# Maoge encountered a problem in his math test that he thought was very difficult. It was about a piecewise function.

# The function is defined as below:
# y = x          if (x<2)
# y = x^2 + 1    if (2 <= x < 6)
# y = sqrt(x+1)  if (6 <= x < 10)
# y = 1/(x+1)    if (10 <= x)

# Given an x, please calucate y. 

# Input:
# Enter an integer x (0<=x<=20).

# Output:
# A single decimal y representing the function answer, with two decimal places.

# Sample input:
# 3
# Sample output:
# 10.00
x = int(input())
if x < 2:
    print("%.2f" % x)
elif 2 <= x and x < 6:
    print("%.2f" % (x**2 + 1))
elif 6 <= x and x < 10:
    print("%.2f" % ((x+1)**0.5))
elif 10 <= x:
    print("%.2f" % (1 / (x+1)))