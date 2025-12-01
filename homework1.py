
list = [7,3,8,9,1,0]

high = 0
for item in list:
    if item > high:
        high = item


print(high)

list2 = [3,6,13,17,25,27,33,36,38,46]

i = 0
for item in list2 :
    if item == 13 :
        itemIdx = i
    i = i+1

print(itemIdx)
    