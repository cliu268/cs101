# Rule-Seeking IV

# Time limit: 0.2 memory limit: 32M
# Description:
# Find the pattern, please output the first n items of the sequence.

# 1,1,1,2,3,4,6,9,13,19

# Input:
# An integer n.

# Output:
# n integers seperated by spaces.

# Sample input:
# 2

# Sample output:
# 1 1

# Constraints:
# 1<=n<=50
n=int(input())
p1=1
p2=1
p3=1
p4=2
for i in range (1, (n+1)):
  if i==1:
    print(p1, end=" ")
  elif i==2:
    print(p2, end=" ")
  elif i==3:
    print(p3, end=" ")
  elif i==4:
    print(p4, end=" ")
  else:
    print((p1+p2+p3), end=" ")
    p5= p1+p2+p3
    p1=p2
    p2=p3
    p3=p4
    p4=p5