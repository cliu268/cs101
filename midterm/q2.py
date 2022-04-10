# Tens digit of an integer

# Time Limit: 0.2s   Memory Limit: 32M
 
# Description
# Input an integer, please output the tens digit of this integer.

# Input
# An integer.

# Output
# An integer.

# Sample Input
# 123

# Sample Output
# 2
n = int(input())
n %= 100
print(n//10)