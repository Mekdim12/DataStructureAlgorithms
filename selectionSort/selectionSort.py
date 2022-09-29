item= [12, 6,-5, 8, 10, 20, -2]

currentMinimum = 0
temp = 0

for index,i in enumerate(item):
    
    currentMinimum = index
    
    for j in range(index+1, len(item)):
        
        if( item[currentMinimum] > item[j] ):
            currentMinimum = j
    
    temp = item[index]
    item[index] = item[currentMinimum]
    item[currentMinimum] = temp

   
    # print(item)

print(item)