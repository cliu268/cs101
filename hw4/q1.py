# Hundred chickens problem 

# Time limit: 1000, Memory limit: 65536
# Description:
# Hundred chickens problem: a rooster is worth 5 yuan, a hen is worth 3 yuan. And 1 yuan can buy 3 chicks. 
# Find the number of chickens you can buy with x yuan, answer the numbers of roosters, hens, and chicks?
# Total number of rooster, hen and chicks must also be x

# Input:
# One decimal number x.

# Output:
# The integers for the number of roosters, hens and chicks.

# Sample input:
# 100
# Sample output:
# 0 25 75
# 4 18 78
# 8 11 81
# 12 4 84
x= int(input())
for c in range(0, (3*x)+1):
  H= (4*x-((14*c)/3))
  r= x-c-(H/2)
  if ((14*c)%3)!=0:
    continue
  elif (H%2)!=0:
    continue
  elif r<0 or H<0:
    continue
  else:
    print(int(r), int(H/2), int(c))

# 5r + 5h + 5c  = 5x
# 5r + 3h + c/3 = x
# 2h + 14c/3 = 4x