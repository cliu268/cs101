# Walk on a grid

# Description:
# For a given grid of size n*m, please find out how many paths you can move from upper left corner to lower right corner.
# You can only walk towards down or right along the boders (only moves vertically or horizontally).
# You cannot stay without moving. For every steps, you need to make a move.

# Input format:
# One line with two positive integers n, m

# Output format:
# Number of paths

# Sample input 1:
# 6 4

# Sample output 1:
# 210

# Sample input 2:
# 2 2

# Sample output 2:
# 6

# Sample input 3:
# 1 1

# Sample output 3:
# 2

# Data range:
# 1<=n<=10, 1<=m<= 4
n, m= map( int, input().split())
s=1
s1=1
s2=1
x= n+m
for i in range(1, x+1):
    s*=i
for i in range(1, n+1):
    s1*=i
for i in range(1, m+1):
    s2*=i
print('%d' % (s/(s1*s2)))