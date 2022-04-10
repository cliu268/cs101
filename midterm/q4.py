# Max pair of numbers

# Time Limit：1s   Memory Limit：256M

# Description:
# Given two lists of integers, please find the maximum sum pair, one number from the first list and another number from 
# the second list. 

# Input:
# Three lines.
# The first line is two integers n, m.
# The second line is n integers ai .
# The third line is m integers bi.

# Output:
# An integer indicating the maximal pair sum of two integers from the two lists.

# Sample Input:
# 2 3
# 1 2
# 1 2 3

# Sample Output:
# 5

# Constraints:
# 1<=n,m<=100,1<=ai,bi<=100  

# Hint: Find maximum integer from each list and sum them together
n, m= map(int, input().split())
x= tuple(map(int, input().split()))
y= tuple(map(int, input().split()))
print(max(x)+max(y))