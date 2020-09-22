# a = [4, 2, 1, 3]
# i = 0

# while i < len(a):
#     min = i
#     for j in range(i, len(a)):
#         if a[j] < a[min]:
#             min = j
            
#     a[i], a[min] = a[min], a[i]
#     i += 1
# print(a)

# demonstrate the joining of two lists to one by adding them
a = [1, 2]
b = [3, 4]
c = a + b
print(c)