# Manhattan distance

# Time limit: 0.2 memory limit: 32M
# Description:
# Little C came to Manhattan and wanted to visit the Metropolitan Museum of Art.
# Since Manhattan's roads run perpendicular to each other and the XY axes, they can be seen as gridlines in the coordinate 
# plane. The Manhattan distance is the distance between two points given that you can only travel along these perpendicular roads.
# Given Little C's starting coordinates (a, b) and their destination coordinates (c, d), find the Manhattan distance between these 
# two points.

# Input:
# The four integers a, b, c, d where the coordinates are (a, b) and (c, d).

# Output:
# Output the Manhattan distance between these two points.

# Sample input:
# 0 0 3 4

# Sample output:
# 7

# Constraints:
# 0 <= a, b, c, d <=100
a,b,c,d= map( int, input().split())
def distance(a,b,c,d):
    if c>=a and d>=b:
        return((c-a)+(d-b))
    elif a>=c and d>=b:
        return((a-c)+(d-b))
    elif c>=a and b>=d:
        return((c-a)+(b-d))
    elif a>=c and b>=d:
        return((a-c)+(b-d))
 
print(distance(a,b,c,d))
