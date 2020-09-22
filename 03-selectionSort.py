def selectionSort(inputArray):
    i = 0
    while i < len(inputArray):
        minIndex = i
        for j in range(i, len(inputArray)):
            if inputArray[j] < inputArray[minIndex]:
                minIndex = j
                
        inputArray[i], inputArray[minIndex] = inputArray[minIndex], inputArray[i]
        i += 1
    return inputArray
a = [7, 3, 4, 5, 1, 2, 9,8, 6, 0]

print(selectionSort(a))