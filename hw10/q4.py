# String Sorting

# Time Limit：1s   Memory Limit：65536KB
# Description:
# Take N names of students and output them in dictionary order.

# Input:
# The first line is an integer N.
# Followed by N lines, each line contains one string.

# Output:
# N lines of sorted names.

# Sample Input:
# 3
# abd
# abc
# bcd

# Sample Output:
# abc
# abd
# bcd

# Hint: The string may contain space.
n = int(input())
L = []
while n:
    L.append(input())
    n-=1
L.sort()
for i in L:
    print(i)
