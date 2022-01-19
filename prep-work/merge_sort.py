'''
Time complexity: O(N log N)
Space complexity: O(N)
'''

def merge_sort(array):
    if(len(array) > 1):
        mid = len(array)//2
        array1 = array[:mid]
        array2 = array[mid:]
        array1 = merge_sort(array1)
        array2 = merge_sort(array2)
        array = merge(array1, array2)
    return array

def merge(first_, second_):
    i,j  = 0, 0
    len_first, len_second = len(first_), len(second_)
    final = []

    while(i < len_first and j < len_second):
        if(first_[i] <= second_[j]):
            final.append(first_[i])
            i = i + 1
        else:
            final.append(second_[j])
            j = j + 1


    while(j<len_second):
        final.append(second_[j])
        j = j + 1
    while(i<len_first):
        final.append(first_[i])
        i = i + 1
    
    return final

if __name__ == "__main__":
    print('Name: ', __name__)
    array = [38,27,43, 3, 9, 82, 10]
    print(merge_sort(array))