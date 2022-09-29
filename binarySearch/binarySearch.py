

#  binary search 

#  list of items
items = [0,4,7,10,23,45,47,53]

#  value to be searched for
valueForSearch = 47

itemIndexBegin = 0
itemIndexEnd = len(items) -1

vaueFoundFlag = False


while( not vaueFoundFlag and itemIndexBegin <= itemIndexEnd):
    
    midValue =  int((itemIndexBegin + itemIndexEnd )/2)
    
    if items[midValue] == valueForSearch:
        print("Value Found at Index of " + str(midValue))
        vaueFoundFlag = True
        break
    elif items[midValue] < valueForSearch :
        # we need to forget about items to the left of mid section 
        itemIndexBegin = midValue + 1
    else:
        itemIndexEnd = midValue - 1

if not vaueFoundFlag:
    print("Items You Looking For is Not Found Here")




