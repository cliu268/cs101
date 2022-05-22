# Replacement of a specific string

# Time limit：0.2s   Memory limit：32M
# Decription：
# Given three strings a,b,c, please replace the string b that appears in a with the string c.
 
# Input：
# A line containing three strings, the length of a, b and c <= 1000, the length after replacement<=1000.

# Output：
# A string after replcement.

# Sample input 1：
# ababa aba abc
 
# Sample output 1：
# abcba
 
# Sample input 2：
# abcabcabc abc abcabc

# Sample output 2：
# abcabcabcabcabcabc
a,b,c=input().split()
a = a.replace(b, c)
print(a)