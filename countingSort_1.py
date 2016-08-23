#https://www.hackerrank.com/challenges/countingsort1
import array

i = 0

#take length of number list as input
listSize = int(input())

#take list as input
integerList = input().split(' ')

#initialize list for counting integers
countingList = array.array('i',(0,)*100)

#convert each elm of list input to int while adding to countingList
while i < len(integerList):
    integerList[i] = int(integerList[i])
    #for each element in list, increase respective element in counting list by one
    countingList[integerList[i]] = countingList[integerList[i]] + 1
    i = i + 1
    
for elm in countingList:
    print (elm, end = ' ')