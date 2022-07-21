
def binarySearch(list, element):
    n = list
    b = 0
    e = len(list)-1
    while e >= b:
        middle = (e+b)//2
        if element > list[middle]:
            b = middle + 1
        elif element < list[middle]:
            e = middle - 1
        else:
            return middle
    return False

print(binarySearch([1,5,7,9,12,14,16,21], 16))
