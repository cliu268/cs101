# Sum of a row

# Time Limit：1s   Memory Limit：65535 k
# Description
# Calculate 1！+2！+3！+…+N！

# Input
# A natural number N.   1<=N<=10

# Output
# output the sum of the factorial(s)

# Sample Input
# 2

# Sample Output
# 3
n = int(input())
sum = 0
for i in range(1, n+1):
    result = 1
    for j in range (1, i+1):
        result *= j
    sum += result
print(sum)