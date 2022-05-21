# Classification of numbers

# Time Limit：1s   Memory Limit：256M
# Description:
# Input n numbers, please find out how many positive numbers,zero,and negative numbers there are.

# Input:
# Two lines,the first line is an positive integer n.  1<=n<=1000
# The second line contains n numbers.

# Output:
# Three lines. Each line contains one integer representing the number of positve numbers,zero and negative numbers.

# Sample Input:
# 3
# 1 0 0

# Sample Output:
# 1
# 2
# 0
m = int(input())
n = list(map( int, input().split()))
pos = [x for x in n if x > 0];
neg = [x for x in n if x < 0];
zero = [x for x in n if x == 0];
print(len(pos)); print(len(zero)); print(len(neg))