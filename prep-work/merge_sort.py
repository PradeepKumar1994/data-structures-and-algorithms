'''
Time complexity: O(N log N)
Space complexity: O(N)
'''

def merge_sort(array):
    if(len(array) > 1):
        print('-0',array)
        mid = len(array)//2
        array1 = array[:mid]
        array2 = array[mid:]
        array1 = merge_sort(array1)
        array2 = merge_sort(array2)
        print(array1, array2)
        array = merge(array1, array2)
        return array
    print(array)
    return array

def merge(first_, second_):
    i,j  = 0, 0
    len_first, len_second = len(first_), len(second_)
    final = []

    while(i < len_first and j < len_second):
        print('..')
        if(first_[i] < second_[j]):
            final.append(first_[i])
            i = i + 1
        elif(first_[i] > second_[j]):
            final.append(second_[j])
            j = j + 1

    if(i == len_first and j < len_second):
        while(j<len_second):
            final.append(second_[j])
            j = j + 1
    elif(j == len_second and i < len_first):
        while(i<len_first):
            final.append(first_[i])
            i = i + 1
    
    return final

array = [38,27,43, 3, 9, 82, 10]
print(merge_sort(array))