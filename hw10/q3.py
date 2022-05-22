# Period String

# Time limit:1000 Memory Limit:512000
# Description:
# If a string is concatenated with one or more repeating strings with length of k, then the string is called a string of period k.
# E.g:
# The string 'abcabcabcabc' has a period of 3 because it consists of 4 cycles of 'abc'. It is also in cycle of 6 
# (two repeated 'abcabc') and cycle of 12 cycle (one cycle 'abcabcabcabc').
# Write a program, read a string, and measure its minimal period.

# Input:
# A string of up to 100 without spaces.

# Output:
# An integer represents the minimum period of the input string.

# Sample input:
# HoHoHo

# Sample output:
# 2

# Hint:
# For a non repeating string, the period is the total length
# e.g. The period of string 'abfxh' is 5
n = input()
answer = len(n)
for i in range(1, len(n)):
    if n[0] != n[i]:
        continue
    elif (len(n) % i == 0):
        sub = n[0:i]
        ok = True
        for j in range(i, len(n), i):
            if (n[j:j+i] != sub):
                ok = False
                break
        if ok:
            answer = i
            break
print(answer)

# shortest sample answer
# a = input()
# for i in range(1, len(a)+1):
#     if (a[:i] * (len(a)//i) == a):
#         print(i)
#         break