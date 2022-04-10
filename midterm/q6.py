# Golden-fairy Numbers

# Time limit: 0.2 memory limit: 32M
# Description:
# X is a golden-fairy number if it satisfies the following properties:
# The sum of all the digits is greater than or equal to 20, and the product of all the digits is greater than or equal to 162.
# Given N , find the number of golden-fairy numbers not greater than N.

# Input format:
# A positive integer N.

# Output format:
# The number of golden-fairy numbers.

# Sample input 1:
# 299

# Sample output 1:
# 1
# Data Range:
# 1<=N<=100000
n= int(input())
answer = 0
for x in range(1, n+1):
    l = map(int, str(x))
    sum = 0
    product = 1
    for i in l:
        sum += i
        product *= i
    #print(x, sum, product)
    if sum >= 20 and product >= 162:
        answer += 1

print(answer)