# Character converting

# Description:
# Input 5 lowercase letters. Write a Function  to shift each letter by two position. For example, 
# a is converted to c, c to e, etc.
# Output the 5 new letters.

# Input format:
# Enter 5 lowercase letters. The letters are in the range a, b,..., x. ( No y or z )

# Output format:
# Output 5 new lowercase letters.

# Sample input 1:
# abcde

# Sample output 1:
# cdefg

# Sample input 2:
# aacca

# Sample output 2:
# cceec
a,b,c,d,e= input()
def alphabet(a,b,c,d,e):
    v1= chr(ord(a)+2)
    v2= chr(ord(b)+2)
    v3= chr(ord(c)+2)
    v4= chr(ord(d)+2)
    v5= chr(ord(e)+2)
    return(v1,v2,v3,v4,v5)
   
a1, a2, a3, a4, a5 = alphabet(a,b,c,d,e)
print(a1+a2+a3+a4+a5)