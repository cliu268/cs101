# Greatest common divisor

# Using the Euclidean division method to

# Find the greatest common divisor of two positive integers n, m(n, m<2^31)

# Input :
# Two positive integers n, m

# Output :
# The greatest common divisor of n,m

# Sample input:
# 26 39


# Sample output:
# 13


# time limit:
# 1000

# Memory limit:
# 65536
a,b = map( int, input().split())
while (b>0):
  a,b = b, a%b
print(a)