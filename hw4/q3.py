# Reverse order output

# Time limit: 0.2 mmeory limit: 32M

# Description of the topic:
# Given an array of integers, please output these integers in reverse order.

# Input format:
# The first line is n, indicating the number of digits;
# The second line is n integers.

# Output format:
# A row of n integers separated by space.

# Sample input:
# 3
# 11 23 45

# Sample output:
# 45 23 11 

# Range:  N≤1000
n = int(input())
#l = list(range(n))
#l = map(int, input().split())
B = list(int(x) for x in input().split())
#for x in reversed(range(n)):
for x in range(n-1, -1, -1):
    print(B[x], end=" ")