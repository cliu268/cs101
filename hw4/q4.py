# Dyeing

# Time limit: 1 memory limit: 256M

# Description of the topic:
# Little A wants to dye the fence of his home. The fence is divided into n segments. At the beginning, each fence has 
# a color of 0. Each time, Small A will dye the fence into a certain color. Ask for the color of the final fence.

# Input format:
# The first line is an integer n indicating the length of the road.
# The second line is an integer m indicating the number of times of dyeing.
# The next m lines are three integers l, r, b for each line, indicating that the interval l to r are dyed to the color b.

# Output format:
# A number of m rows, indicating what color each segment is.

# Sample input:
# 3
# 2
# 1 2 1
# 2 3 2

# Sample output:
# 1 2 2

# Note: All numbers do not exceed 1000.
n = int(input())
m = int(input())
#fence = list(range(n))
fence = [0] * n
#print(fence)
for i in range(m):
    l,r,b = map(int, input().split())
    for x in range(l-1, r):
        fence[x] = b

for i in range(n):
    print(fence[i], end=" ")
