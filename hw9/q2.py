# Print Pascals Triangle

# Description:
# Print an Yang Hui (Pascal) triangle
# You can search internet for the definition: https://www.mathsisfun.com/pascals-triangle.html
 
# Input format:
# A single number n indicating the levels of the triangle
 
# Output format:
# n layers(lines) of Pascal triangle.
 
# Sample input:
# 4

# Sample output:
# 1
# 1 1
# 1 2 1
# 1 3 3 1

# Time limit:
# 1000
# Memory limit
# 65536
n = int(input())
a= [ [0]*n for i in range(n) ]
for i in range (n):
    for j in range (i+1):
        if j==0 or j==i:
            a[i][j]=1     
        else:
            a[i][j]=a[i-1][j]+a[i-1][j-1]
        print(a[i][j], end=' ')
    print(end= '\n')