# Polynomial evaluation Ⅱ

# Time Limit：0.2s   Memory Limit：32M
 
# Description
# Input an integer n. Calculate 1 + 1/(1-3) + 1/(1-3+5) + ...... + 1/(1-3+5-...+2n-1).

# Input
# An integer n.

# Output
# A floating number, leaving 3 digits after the decimal point.

# Sample Input
# 1

# Sample Output
# 1.000
n = int(input())
s = 0
d = 0
for i in range(1, n+1):
    if i % 2 == 1:
        d += 2*i - 1
    else:
        d -= 2*i - 1
    s += 1/d
print('%.3f' %s)