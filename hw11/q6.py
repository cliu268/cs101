# Binary Search

# Time limit:1000 Memory limit:65536
# Description:
# Binary search:
# Given N numbers (N <= 10 ^ 6) that are already sorted in ascending order. Please use binary search to find whether 
# a given number M exists or not. If there is this number, output the position of first occurrence (counted start from 
# 1 and from left to right). If there is no such a number output 0.

# Input:
# In the first line there are two integer numbers N and M.
# The second line has N integers.

# Output:
# The postion when M appears for the first time (count from left to right). Output 0 if there is no such a number.

# Sample input:
# 7 4
# 1 2 4 4 5 7 9

# Sample output:
# 3
n,m = map( int, input().split())
l= list(map(int, input().split()))

def binary_search(start, end, value):
    while (end > start):
        mid = (start + end) // 2
        if (l[mid] >= value):
            end = mid
        else:
            start = mid + 1
    if l[start] == value:
        return start+1
    else:
        return 0

def bi_search(start, end, value):
    if (l[start] == value):
        return start + 1
    if (start >= end):
        return 0    
    mid = (start + end) // 2
    if (l[mid] < value):
        return bi_search(mid+1, end, value)
    else:
        return bi_search(start, mid, value)

def bi3_search(start, end, value):
    if (l[start] == value):
        return start + 1
    if start >= end:
        return 0
    mid = (start + end) // 2
    if l[mid] >= value:
        return bi3_search(start, mid, value)
    else:
        return bi3_search(mid + 1, end, value)

print(binary_search(0, n-1, m))
print(bi_search(0, n-1, m))
print(bi3_search(0, n-1, m))