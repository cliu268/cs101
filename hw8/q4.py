# Polynomial evaluation Ⅰ

# Time Limit：0.2s   Memory Limit：32M 
# Description
# Given an integer n, calculate  1 + (1+2) + (1+2+3) + ... + (1+2+3+...+n) using recursive function(s)

# Input:
# An integer.

# Output:
# An integer.

# Sample Input:
# 4

# Sample Output:
# 20

# Hint:
# for input 4, the result is:
# 1 +
# 1+2 +
# 1+2+3 +
# 1+2+3+4
# = 1 + 3 + 6 + 10
# = 20
n= int(input())
def math(n):
  if n<=1:
    return 1
  else:
    return math(n-1) + (n+1)*n//2
 
print(math(n))