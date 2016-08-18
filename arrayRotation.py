#Hacker Rank challenge: https://www.hackerrank.com/challenges/circular-array-rotation

#initializing count
count = 0
index = 0

#accept input for size, # of rotations, number of 'tests'
paramArray = input().split(' ')
paramArray = [int(paramArray[0]), int(paramArray[1]), int(paramArray[2])]

n = paramArray[0]
k = paramArray[1]
q = paramArray[2]

#accept input for size of array
elmArray = input().split(' ')

#convert all elements of elm array to numbers
while index < len(elmArray):
    elmArray[index] = int(elmArray[index])
    index = index + 1

#if input not n-size array

if (len(elmArray) != n):
    while (len(elmArray) != n):
        elmArray = input('\nProvided array is not ' + str(n) +' element(s) in length. Please provide ' + str(n) +' element(s).\n').split(' ')
        while index < len(elmArray):
            elmArray[index] = int(elmArray[index])
            index = index + 1
    
#perform tests
while (count < q):
    pos = int(input())
    print(elmArray[(pos - k)%n])
    count = count + 1