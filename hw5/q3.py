# Perfect number

# For a given positive integer N ,output all the perfect numbers between 1 and N, one number in each line.
# In number theory, a perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the 
# number itself.
# For instance, 6 has divisors 1, 2 and 3 (excluding itself), and 1 + 2 + 3 = 6, so 6 is a perfect number.

# Sample Input ：
# 10

# Sample Output ：
# 6

# Data Range ： 1<=N<=10000
# Time Limit ： 1000 ms
# Memory space Limit ： 65536 kb

def is_perfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return True
    else:
        return False

n = int(input())
for i in range(2, n):
    if is_perfect(i):
        print(i)