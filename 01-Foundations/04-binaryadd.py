def binadd(x, y, rem=0):
    bin = {
        "00":[0,0],
        "01":[1,0],
        "10":[1,0],
        "11":[0,1]
    }

    [binSum1, rem1] = bin[str(x)+str(y)]
    [binSum2, rem2] = bin[str(binSum1)+str(rem)]
    rem = bin[str(rem1)+str(rem2)][0]

    return binSum2, rem


def binaryadd(binArray1, binArray2):
    # Make them same length
    while len(binArray1) > len(binArray2):
        binArray2.insert(0, 0)
    while len(binArray2) > len(binArray1):
        binArray1.insert(0, 0)
    outputBinArray = []
    i = len(binArray1) - 1
    rem = 0
    while i > -1:
        binSum, rem = binadd(binArray1[i], binArray2[i], rem)
        
        outputBinArray.insert(0, binSum)
        i -= 1
    outputBinArray.insert(0, rem)

    return outputBinArray


a = [1, 0, 1]
b = [1, 1, 0, 1]
print(binaryadd(a, b))  