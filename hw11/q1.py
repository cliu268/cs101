# Time Difference

# Description:
# Given two times (minutes and seconds) within the same hour, with the second time always being later than the first time.
# Please find the time difference between the two times.

# Input:
# A row of 4 integers from 0 to 59, the first two represent the minutes and seconds of the first time,
# and the last two represent the minutes and seconds of the second time.

# Output:
# An integer per line representing the time difference (in seconds) between the two times.

# Sample input:
# 0 0 1 10

# Sample output:
# 70
m1, s1, m2, s2 = map( int, input().split())
print(abs((s1 - s2) + (m1 * 60 - m2 * 60)))