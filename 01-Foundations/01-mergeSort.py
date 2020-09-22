# def num2binary(num):
#     if num == 0:
#         return ""
#     else:
#         return num2binary(num // 2) + str(num%2)

# number = 8
# print(num2binary(number))


def merge(left, right):
    l = 0
    r = 0
    n = len(left) + len(right)
    c = [0]*n
    for i in range(n):
        if len(left) != 0 and len(right) != 0:
            if left[l] < right[r]:
                c[i] = left[l]
                left.pop(l)
            else:
                c[i] = right[r]
                right.pop(r)
        elif len(left) == 0 and len(right) != 0:
            c[i] = right[r]
            right.pop(r)
        elif len(left) != 0 and len(right) == 0:
            c[i] = left[l]
            left.pop(l)
        else:
            break

    return c

def mergeSort(aList):
    if len(aList) == 1:
        #sorted
        return aList

    else:
        n = len(aList) // 2
        left = mergeSort(aList[:n])
        right = mergeSort(aList[n:])
        return merge(left, right)

print(mergeSort([4, 2, 1, 3]))