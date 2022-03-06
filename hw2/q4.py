# Coin

# Description:
# There are four coins on Maoge's desk, some facing up and some facing down. Now Maoge wants to turn all these coins into the 
# same side, but you can only can flip three coins at a time. Please find out the minimum number of flips.

# Input:
# Enter a line with four digits of 0/1 to indicate the initial state of each coin.

# Output:
# One number to indicate the answer.

# Sample input:
# 1 0 1 1
# Sample output:
# 1
a,b,c,d = map(int, input().split())
x = a+b+c+d
if x == 0 or x == 4:
    print(0)
elif x == 1 or x == 3:
    print(1)
else:
    print(2)