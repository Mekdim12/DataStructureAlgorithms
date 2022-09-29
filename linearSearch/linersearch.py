#  using python searching algorithm
#  linear search

listofItems = [45,65,95,78,42,980]

valueToBeSearched = 42
flag = True

for index,i in enumerate( listofItems ):
    if i == valueToBeSearched:
        print("Item Found At Index Of "+ str(index))
        flag = False

if flag:
    print("The Item You Looking for is Not here")


#  another way

if valueToBeSearched in listofItems:
    for index,i in enumerate( listofItems ):
        if i == valueToBeSearched:
             print("Item Found At Index Of "+ str(index))
else:
    print("The Item You Looking for is Not here")




