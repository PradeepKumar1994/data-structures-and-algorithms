

def sort(left, right):
    sorted_arr = []
    i, j = 0, 0

    print("left: {} right:{}".format(left, right))

    while(i < len(left) and j < len(right)):

        if(left[i] < right[j]):
            sorted_arr.append(left[i])
            i = i + 1

        else:
            sorted_arr.append(right[j])
            j = j + 1

    print('Partial Sort: ', sorted_arr)
    if(i == len(left) and j < len(right)):
        for ri in range(j, len(right)):
            sorted_arr.append(right[ri])
    else:
        for le in range(i, len(left)):
            sorted_arr.append(left[le])

    print('SOrted Array: ',sorted_arr)

    return sorted_arr


def mergesort(arr):

    if(len(arr) <= 1):
        return arr

    mid = len(arr)//2

    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    return sort(left, right)

ee = mergesort([38,27,43, 3, 9, 82, 10])
print(ee)