# Chebyshev distance

# Time limit: 0.2s        memory limit: 32M
# Description:
# The Chebyshev distance calculation, commonly known as the "maximum metric" in mathematics, measures distance between 
# two points as the maximum difference over any of their axis values.
# In a 2D grid, for instance, if we have two points (x1, y1), and (x2, y2), the Chebyshev distance between is max(y2 - y1, x2 - x1).

# Input format:
# Four integers, a, b, c, D. Coordinates are (a, b) and (c, d)

# Output format:
# Output the Chebyshev distance of these two points.

# Sample input:
# 0 0 3 4

# Sample output:
# 4

# Data Range:
# 0<=a, b, c, d<=100
a,b,c,d= map( int, input().split())
def distance(a,b,c,d):
    if c>=a and d>=b:
        return(max((c-a),(d-b)))
    elif a>=c and d>=b:
        return(max((a-c),(d-b)))
    elif c>=a and b>=d:
        return(max((c-a),(b-d)))
    elif a>=c and b>=d:
        return(max((a-c),(b-d)))
 
print(distance(a,b,c,d))