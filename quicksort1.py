#allow input for:
#size of array
#array with p as the first element of array

#creating three subarrays
#for each element of array:
    #if element > p, then right
    #if element < p, then left
    #if element = p, then equals
    
size = int(input())
array = input().split(" ")

p = int(array[0]);

#dynamic arrays
left = []
right = []
equals = []

for elm in array:
    if (int(elm) < p):
        left.append(int(elm))
    if (int(elm) == p):
        equals.append(int(elm))
    if (int(elm) > p):
        right.append(int(elm))

for elm in left:
    print(elm, end = ' ')
for elm in equals:
    print(elm, end = ' ')
for elm in right:
    print(elm, end = ' ')