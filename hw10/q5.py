# Histogram 

# Description:
# Write a program to read four lines of text, then output the histogram for the number of times
# each letter appears in the input. Make sure the output format is same as the sample output.

# Input format:
# Four lines of text,all uppercase, no more than 100 characters per line.

# Output format:
# Consists of a number of lines with spaces and asterisks. The last line is spaces and letters.

# Do not print extra spaces at the end of any line. Do not print any blank lines.

# Sample input:
# THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG.
# THIS IS AN EXAMPLE TO TEST FOR YOUR
# HISTOGRAM PROGRAM.
# HELLO!

# Sample output :
#                             *
#                             *
#         *                   *
#         *                   *     *   *
#         *                   *     *   *
# *       *     *             *     *   *
# *       *     * *     * *   *     * * *
# *       *   * * *     * *   * *   * * * *
# *     * * * * * *     * * * * *   * * * *     * *
# * * * * * * * * * * * * * * * * * * * * * * * * * *
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

# Hint:
# The string may include non-letter character(s). Your program should only count the letters.
A = [0] * 26
for i in range(4):
    line = input()
    for x in range(0, len(line)):
        if (line[x].isalpha()):
            A[ord(line[x])-ord('A')] += 1
mm = max(A)
while mm >= 0:
    output = ''
    for i in range(26):
        if mm == 0:
            output += chr(i + ord('A'))
        elif A[i] == mm:
            output += '*'
            A[i] -= 1
        else:
            output += ' '
        if i < 25:
            output += ' '
    mm -= 1
    print(output)
