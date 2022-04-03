# Election

# Time Limit：1s   Memory Limit：256M
# Description:
# Choose a squad leader among three candidates A (with ID 1), B (with ID 2), and C (with ID 3). Please count the votes for 
# each candidate. Whoever gets more than half of the total votes is elected. Output the vote counts for each candidate, total 
# votes, and the elect result. If candidate A is elected then output "A-yes". If none of the candidates got more than half votes 
# then output "all-NO".

# Input:
# One line of integers, each number is one vote for the candidate with that ID value. Input ends with value -1 indicating the 
# input is finished.

# Output:
# Total five lines as in the sample.

# Sample Input:
# 1 1 3 2 1 3 2 1 3 3 1 2 4 1 4 1 2 1 2 1 1 -1

# Sample Output:
# A=10 
# B=5 
# C=4 
# Tot=19 
# A-yes

# Hint :
# This is an exercise of following the sample input and output. Pay attention to the formats and values, for example, is there 
# any invalid ID value in the votes? How are the invalid votes counted?
m = tuple(map(int, input().split()))
A=0
B=0
C=0
for i in m:
    if i==1:
        A+=1
    if i==2:
        B+=1
    if i==3:
        C+=1
    if i==-1:
        break
    print(f"A={A}")
    print(f"B={B}")
    print(f"C={C}")
    Tot= A+B+C
    print(f"Tot={Tot}")
    if A>=(Tot/2):
        print("A-yes")
    elif B>=(Tot/2):
        print("B-yes")
    elif C>=(Tot/2):
        print("C-yes")
    else:
        print("all-NO")