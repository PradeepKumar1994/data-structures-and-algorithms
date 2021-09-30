
def binary_searching(arr, low, high, target):
    print('low: {} high: {}'.format(low, high))
    if(low <= high):
    
        mid = (low + high)//2

        if(arr[mid] == target):
            return 'found'

        elif(arr[mid] > target):

            return binary_searching(arr, low, mid-1, target)

        else:

            return binary_searching(arr, mid+1, high, target)

    return 'not found'


arr = [1,3,7,8,9,11,12,14,20]
print(binary_searching(arr, 0, len(arr)-1, 10))