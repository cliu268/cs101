# Bubble sort

# Description:
# Practice the bubble sort algorithm:
# Input n numbers. Compare two adjacent numbers, if the former is smaller, then swap them, so that you can bubble the 
# largest number to the end of sequence. Repeat until all the number in sequence s is in order. Output it from small to large. 

# Input:
# One positive integer N
# The second line contains N numbers ai. 
# 1<=N<=1000    and   0<=ai<=10^9  

# Output:
# N integers.

# Sample Input:
# 5
# 1 4 2 3 5

# Sample Output:
# 1 2 3 4 5
n = int(input())
a = list(int(x) for x in input().split())
 
for i in range(n):
    for j in range(n-1-i):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            # a[j], a[j+1] = a[j+1], a[j]
print(*a)
