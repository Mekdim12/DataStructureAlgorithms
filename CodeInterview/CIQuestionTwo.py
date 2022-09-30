

# finding the number of squares from the aread given

#  for using sqrt fucntion 
import math


def squareNumberFinder(areaoftheSquare):
    forReturningListOfSquare = []

    copyOfAreaOfTheSquare = areaoftheSquare # copyinh area so that i don't lost it while computing the sqrs

    while areaoftheSquare > 0 : # reapear until the area reaches 0

        copyOfAreaOfTheSquare =int(math.sqrt(areaoftheSquare)) ** 2  #12 3.4 == 3   then 3**2 == 9 so   
        
        forReturningListOfSquare.append(copyOfAreaOfTheSquare) # just appending for returning the result

        # print(areaoftheSquare)  before reducing for checing

        areaoftheSquare -= copyOfAreaOfTheSquare # after getting the sqrt value i need to minimze the area 12 - 9 = 3, 3 = 9 
        # print(areaoftheSquare)  after reducing checking 


    # returning the list of squares 
    return forReturningListOfSquare


print(squareNumberFinder(56))