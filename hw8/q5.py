# Print double-deck pyramid

# Descripition：
# Output double-deck Pyramid. 

# Iutput：
# Multiple test data, each input is one integer n( 2 <= n <= 9).
# Multiple inputs ended by entering EOF (Ctrl+D on Mac, Ctrl-Z on Win)

# Output：
# One double-deck pyramid for each input

# Sample input：
# 2
# 5

# Sample output：
#  *
# ***
#  *
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

# Note：
# Use while (cin>>n) to keep receiving input until EOF is entered.
lines = []
while True:
    try:
        line = int(input())
        lines.append(line)
    except EOFError:
        break

def pyramid(lines):
  for i in lines:
    for j in range(1, i+1):
        output =  ' ' * (i-j) + '*' * (2*j - 1)
        print(output)
    for j in range(i-1, 0, -1):
        output =  ' ' * (i-j) + '*' * (2*j - 1)
        print(output)

pyramid(lines)