# Even or odd

# Time Limit: 0.2s   Memory Limit: 32M
 
# Description
# Lately, Little C has been learning about numbers and has gained the ability to tell if one is even or not. Given an integer n, 
# please output 1 if it is even and 0 if it is odd.

# Input
# An integer.

# Output
# 0 or 1

# Sample Input 1
# 50

# Sample Output 1
# 1
 
# Constraints
# 1 <= n <= 100

# Challenge
# Solve the problem without an if statement. 
a = input()
print((int(a)+1) %2)