'''
Time complexity: O(log N)
Space complexity: O(1)
'''

def binary_search_recur(array, low, high, target):

    if(low < high):
        mid = (low + high)//2
        if(array[mid]==target):
            return True

        elif(arr[mid]<target):
            return binary_search_recur(arr, mid+1, high, target)

        else:
            return binary_search_iter(arr, mid-1, target)
        
    return False


def binary_search_iter(array, target):

    low = 0
    high = len(array)-1

    while(low<high):

        mid = (low+high)//2

        if(array[mid]==target):
            return True
        
        elif(array[mid]<target):
            low = mid + 1

        else:
            high = mid - 1

    return False

if __name__ == '__main__':

    arr = [0,1,2,3,4,5,6,7,8,9]
    low = 0
    high = len(arr)
    target = 10
    print(binary_search_recur(arr, low, high, target))
    print(binary_search_iter(arr, target))
