'''
Time complexity: O(N^2)
Space complexity: O(N)
'''

def Quicksort(array, start, end):

    if(start < end):
        loc = _quicksort(array, start, end)
        array = Quicksort(array, start, loc-1)
        array = Quicksort(array, loc+1, end)
    return array

def swap(a, b):
    return b, a

def _quicksort(array, start, end):
    begin_array = start
    pivot = array[start]
    length = len(array)-1
    while(start<end):

        while(start < length and array[start]<=pivot):
            start = start+1

        while(end > -1 and array[end]>pivot):
            end = end-1

        if(start<end):
            array[start], array[end] = swap(array[start], array[end])
            
    array[begin_array], array[end] = swap(array[begin_array], array[end])
    return end

array = [7, 6, 10, 5, 9, 2, 1, 15, 7]
print('final-->',Quicksort(array, 0, len(array)-1))