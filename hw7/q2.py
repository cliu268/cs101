# Collatz conjecture
 
# Description
# A Simple Math Problem Human Still Can’t Solve：

# Just pick any positive integer: If the number is even, cut it in half; if it’s odd, triple it and add 1.
# Take that new number and repeat the process, again and again. If you keep this up, you’ll eventually reach value 1.
# At least, that’s what we think will happen.

# Given a number, calculate how many steps you will need until it reaches 1.

# Input
# An positive integer n.(1<=n<=100)

# Output
# An integer.

# Sample Input
# 3

# Sample Output
# 7

# Hint
# begin with 3:
# 3 x 3 + 1 = 10
# 10 / 2 = 5
# 5 x 3 + 1 = 16
# 16 / 2 = 8
# 8 / 2 = 4
# 4 / 2 = 2
# 2 / 2 = 1
# It took 7 steps to become 1, so the answer is 7
n = int(input())
count = 0
while (n != 1):
    if (n % 2):
        n = n * 3 + 1
    else:
        n /= 2
    count += 1
print(count)