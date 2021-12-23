'''
Time complexity: O()
Space complexity: O(1)
'''

def Quicksort(array, start, end):

    if(start < end):
        array_left = Quicksort(array[:end], start, end-1)
        array_right = Quicksort(array[end:], start, end+1)
        array = array_left + array_right

def swap(a, b):
    return b, a

def _quicksort(array, start, end):
    pivot = array[0]
    length = len(array)-1
    while(start<=end):
        print('start: {} end: {}'.format(start, end))
        print('---',start <= length and array[start]<=pivot)
        print(array)
        while(start <= length and array[start]<=pivot):
            start = start+1
            print('start incr',start)

        while(end > -1 and array[end]>pivot):
            end = end-1
            print('end incr',end)

        if(start<end):
            array[start], array[end] = swap(array[start], array[end])
            print(start, end)

    array[0], array[end] = swap(array[0], array[end])
    print('after swap: ',array)
    return array, end

array = [7, 6, 10, 5, 9, 2, 1, 15, 7]
print(Quicksort(array, 0, len(array)-1))