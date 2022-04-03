# Print all the scores below average

# Time Limit：0.2s   Memory Limit：32M
# Description
# Print out all scores below average among n scores, 1<=n<=100.

# Input
# Multiple test data set, finished by entering end-of-file, a.k.a., EOF (CTRL-D on Mac, CTRL-Z on Windows).
# Each test is a line, with integer n followed by n scores. 

# Output
# For each line of test data, output all the scores below the average in the input order, separated by one space. If nothing 
# is below the average then output an empty line.
 
# Sample Input
# 3 40 50 60
# 2 90 80
# 5 10 10 90 80 80
 
# Sample Output
# 40
# 80
# 10 10

# Hint
# Use while loop till EOF is entered.
# There are 3 tests in the sample. First test has one score 40 which is below the average. In the second test, 
# 80 is below average. And in the last test, two scores 10 and 10 are below average.

lines = []
while True:
    try:
        line = tuple(map(int, input().split()))
        lines.append(line)
    except EOFError:
        break

for line in lines:
    sum = 0
    for x in range(1, line[0] + 1):
        sum += line[x]
    avg = sum/line[0]
    for x in range(1, line[0] + 1):
        if (line[x] < avg):
            print(line[x], end=" ")
    print(end="\n")
