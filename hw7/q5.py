# Merge Array

# Merge two ordered arrays A and B into a large ordered array.
# Input will be 4 lines, size of array A and the numbers of A; size of array B and the numbers of B.
# Output all the numbers from A and B in ascending order.
# Be aware, the size of array A and B can be different !

# Sample input:
# 5
# 1 3 5 7 9
# 5
# 2 4 6 8 10

# Sample output:
# 1 2 3 4 5 6 7 8 9 10

# time limit:
# 1000

# memory limit:
# 65536
n = int(input())
a = list(int(x) for x in input().split())
m = int(input())
b = list(int(x) for x in input().split())
# create the result list called c
# i is the index for a and j is the index for b
# x is the index for c. all i, j, x start from 0
c = a+b
i = 0
j = 0 
x = 0
while (i < n and j < m):
    if a[i] <= b[j]:
        c[x] = a[i]
        x += 1
        i += 1
    else:
        c[x] = b[j]
        x += 1
        j += 1
if i == n:
    # move all the remaining items in b over to c
    while (j < m):
        c[x] = b[j]
        x += 1
        j += 1
else:
    # move all the remaining items in a over to c
    while (i < n):
        c[x] = a[i]
        x += 1
        i += 1
print(*c)