# The surface area and volume of a cuboid

# Time limit: 0.2   Memory limit: 32M
# Description:
# Given the length, width, and height of a cuboid, please output the surface area and volume of the cuboid.

# Input:
# Three positive integers not exceeding 100, representing the cuboid's length, width, and height.

# Output:
# Two integers representing the cuboid's surface area and volume.

 # Sample input:
# 10 10 10

# Sample output:
# 600 1000 
l,w,h= map( int, input().split())
print((l*w*2)+(l*h*2)+(w*h*2) ,(l*w*h))
