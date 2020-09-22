def insertionSort(inputArray):
    """
    Sorts the input array in increasing order
    input: inputArray
    output: outputArray
    """
    # initialize output array
    outputArray = []
    while len(inputArray) > 0:
        if len(outputArray) == 0:
            outputArray.append(inputArray.pop())
        else:
            value = inputArray.pop()
            
            # non decreasing order
            # start from the right of outputArray and identify index location to insert value from inputArray
            i = len(outputArray) - 1
            
            while i > -1 and outputArray[i] > value:
                i -= 1
            outputArray.insert(i+1, value)
    return outputArray



def insertionSort2(inputArray):
    """
    Sorts the input array in increasing order
    input: inputArray
    output: outputArray
    """
    # initialize output array
    outputArray = []
    while len(inputArray) > 0:
        if len(outputArray) == 0:
            outputArray.append(inputArray.pop())

        else:
            value = inputArray.pop()
            
            # non increasing order
            # start from the left of outputArray and identify index location to insert value from inputArray
            i = 0
            
            while i < len(outputArray) and outputArray[i] < value:
                i += 1
            outputArray.insert(i, value)
    return outputArray


a = [31, 41, 59, 26, 41, 58]
e = [31, 41, 59, 26, 41, 58]
b = insertionSort(a)
c = insertionSort2(e)                           
print(b)
print(c)