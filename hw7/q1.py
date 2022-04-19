# Output numbers

# Description
# Output the numbers between 1 and n which can be divided by 3 and there is one or more digits of which is 5.

# Input
# One integer.  1<=n<=100000

# Output
# Each line is a number which satisfies the conditions.

# Sample Input
# 100

# Sample Output
# 15
# 45
# 51
# 54
# 57
# 75
n= int(input())
for i in range (1, n+1):
  if i%3!=0:
    continue
  x = i
  while x!=0:
    if x%10==5:
      print (i)
      break
    else:
      x//=10