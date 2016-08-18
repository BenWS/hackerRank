#HackerRank challenge: https://www.hackerrank.com/challenges/compare-the-triplets

a_score = 0
b_score = 0

#initializing index
i = 0

a0,a1,a2 = input().strip().split(' ')
a = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b = [int(b0),int(b1),int(b2)]

while i < len(a):
    if a[i] > b[i]:
        a_score += 1
    elif a[i] < b[i]:
        b_score += 1
    i += 1
    
print(str(a_score) + " " + str(b_score))