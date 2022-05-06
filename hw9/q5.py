# Good students

# Time Limit：0.2s   Memory Limit：32M
# Description
# With all student's scores, please find the number of "good students", who has at least one class that scored top 
# among all the student.

# Input
# The first line are two integers n,m, represent the number of students and classes.  1<=n,m<=100​ 
# Followed by n lines,each line contains m scores for one student. All scores are single digit number.

# Output
# Output the number of "good students".

# Sample Input
# 3 5
# 91728
# 11828
# 11111

# ​Sample Output
# 3

# Hint
# first student has 4 classes with top score: 9 , 1,  2, and 8
# second student has 4 classes with top score: 1, 8, 2,  and 8
# third student has 1 class with top score: 1
# so all student are good students in this example
n,m = map( int, input().split())
a= [ [0]*m for i in range(n) ]
b= [False]*n
answer = 0
for i in range(n):
    a[i] = input()
     
for x in range(n):
    if b[x]:
        continue
    for j in range(m):
        is_good_student = True
        for i in range(n):
            if i==x:
                continue
            if a[x][j]<a[i][j]:
                is_good_student = False
                break
        if is_good_student:
            b[x] = True
            answer += 1
            break
print(answer)