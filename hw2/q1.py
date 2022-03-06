# Chicken and rabbit in one cage

# Time limit: 1000 Memory limit: 65536
# Description:
# Several chickens and several rabbits are kept in the same cage.

# There are x heads, and y feets. How many chickens and rabbits there are ?

# Input:
# Two integers: x heads and y feets.

# Output:
# Two integers: chickens number in first line and rabbits number in second line. 

# Sample input:
# 40 100

# Sample output:
# 30
# 10
x, y = map(int, input().split())
print(int(x - (y - 2*x) / 2))
print(int((y - 2*x) / 2))