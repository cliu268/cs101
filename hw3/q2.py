# List of prime numbers

# Time Limit：1s   Memory Limit：256M

# Description:

# A prime number is the number which can only be divided by 1 and itself. For example,2,3,5,7,11,13,17 are prime numbers. 
# Given an integer N,please find all the prime number between 1 and N.

# Input:
# An integer N.  1<=N<=2000

# Output:
# All the prime numbers in order, separated by spaces.

# Sample Input:
# 20

# Sample Output:
# 2 3 5 7 11 13 17 19
n= int(input())
for i in range (2, (n+1)):
  if i==2:
    print(i, end=' ')
  for x in range (2, i):
    if i%x==0:
      break
    elif x==i-1:
      #i is a valid prime number
      print(i, end=' ')