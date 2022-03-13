# Rule-Seeking I

# Time limit: 0.2 memory limit: 32M
# Description:
# Find the pattern, please output the first n items of the sequence.

# 2,1,4,3,6,5,...

# Input:
# An integer n.

# Output:
# n integers seperated by spaces.

# Sample input:
# 2

# Sample output:
# 2 1

# Constraints:
# 1<=n<=100
n=int(input())
p=0
for i in range (1, (n+1)):
  if i==1:
    p=i+1
    print(p, end=" ")
  elif i%2==0:
    p-=1
    print(p, end=" ")
  else:
    p+=3
    print(p, end=" ")