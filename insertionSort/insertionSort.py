

items = [18,-32,-110,6,68,20,-34]


for index, i in enumerate(items):

    j = index - 1

    temp = items[index]

    while j>=0 and items[j] > temp:

        items[j+1] = items[j]
 
        j -= 1

    items[j+1] = temp


print(items)





