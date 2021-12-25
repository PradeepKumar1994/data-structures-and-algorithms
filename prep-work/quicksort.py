'''
Time complexity: O()
Space complexity: O(1)
'''

class Quick_sort():
    def __init__(self, array):
        self.array = array

    def Quicksort(self, start, end):

        if(start < end):
            loc = self._quicksort(start, end)
            self.Quicksort(start, loc-1)
            self.Quicksort(loc+1, end)
            print(self.array)
        return self.array

    def swap(self,a, b):
        return b, a

    def _quicksort(self, start, end):
        begin_array = start
        pivot = self.array[start]
        length = len(self.array)-1
        while(start<end):

            while(start < length and self.array[start]<=pivot):
                start = start+1

            while(end > -1 and self.array[end]>pivot):
                end = end-1

            if(start<end):
                print('Before: {} Pivot: {}'.format(self.array, pivot))
                self.array[start], self.array[end] = self.swap(self.array[start], self.array[end])
                print('After: ',self.array)
                
        print('Before: {} Pivot: {}'.format(self.array, pivot))
        self.array[begin_array], self.array[end] = self.swap(self.array[begin_array], self.array[end])
        print('After: ',self.array)
        return end

array = [7, 6, 10, 5, 9, 2, 1, 15, 7]
qs =Quick_sort(array)
print('final-->',qs.Quicksort(0, len(array)-1))