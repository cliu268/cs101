# Selection sort

# Description:
# Practice Selection Sort algorithm:
# Divide a sequence into two parts: sorted and unsorted. 
# Pick the smallest number from the unordered part, then put it to the end of the sorted part.
# Repeat this process until the the entire sequence is sorted.

# Input
# The first line, one integer N.
# The second line is the unsorted sequence contains N unsorted numbers ai. 
# 1<=N<=1000,    0<=ai<=10^9  

# Output
# The sorted sequence

# Sample Input:
# 5
# 1 4 2 3 5

# Sample Output:
# 1 2 3 4 5
n = int(input())
a = list(int(x) for x in input().split())
 
for i in range(n):
    smallest = i
    for j in range(i, n):
        if (a[j] < a[smallest]):
            smallest = j
    a[i], a[smallest] = a[smallest], a[i]
print(*a)