


def guthrieIndex(inputN):
    iterationNumberCounter = 0
    # checking whether if its a positive integer nuber
    if inputN > 0:
        # so it goes unitl its one
        while inputN  != 1:
            if inputN % 2 == 0: # cheking parity  true even false odd
                inputN = inputN/2
            else: # odd
                inputN = (inputN * 3) +1
            # print("-"+str(inputN)) // for checking the sequence
            iterationNumberCounter += 1

    # returns the guthrieIndex of the the input
    return iterationNumberCounter


print(guthrieIndex(42))