# Matrix and Count

# Description:
# Input a n*m matrix with binary value and output the number of number 1 in each column.

# Input:
# The first row is two integers n, m.
# Then n rows, m integers per row of value 0 or 1

# Output:
# m integers, one per line. Each number represents the count of 1 in the corresponding column.

# Sample input 1:
# 3 5
# 0 0 1 1 0
# 0 1 1 0 1
# 1 0 0 1 0

# Sample output 1:
# 1
# 1
# 2
# 2
# 1

# Sample input 2:
# 5 8
# 1 1 1 0 0 1 0 1
# 0 0 1 1 1 0 1 1
# 1 0 0 1 1 0 1 0
# 0 0 0 0 1 1 1 1
# 0 0 1 1 1 1 1 0

# Sample output 2:
# 2
# 1
# 3
# 3
# 4
# 3
# 4
# 3

# Constraints:
# 1<=n, m<=500
n,m = map( int, input().split())
a= [ [0]*m for i in range(n) ]
for i in range(n):
  x= input().split()
  for j in range(m):
    a[i][j]= int(x[j])
for j in range(m):
  answer=0
  for i in range(n):
    if a[i][j]==1:
      answer+=1
    else:
      continue
  print(answer)