
class QuickSort():

    def __init__(self, arr):

        self.arr = arr
        
    def swap(self,a, b):

        temp = a
        a = b
        b = temp

        return a, b

        

    def partition(self, lower, upper):

        pivot = self.arr[lower]
        start = lower
        end = upper

        while(start < end):

            while(self.arr[start] <= pivot and start < len(self.arr)-1):
                start = start + 1

            while(self.arr[end] > pivot and end > -1):
                end = end - 1

            if(start < end):
                
                temp = self.arr[start]
                self.arr[start] = self.arr[end]
                self.arr[end] = temp
                print('----->',self.arr)
        print('before: ',self.arr)
        self.arr[lower], self.arr[end] = self.swap(self.arr[lower], self.arr[end])
        print('After: ',self.arr)
        print('lower: {} upper: {}, end: {}'.format(lower, upper, end))
        print()
        return end

    def quicksort(self, lower, upper):

        if(lower < upper):

            location = self.partition(lower, upper)
            self.quicksort(lower, location-1)
            self.quicksort(location+1, upper)
            print(self.arr)


#arr = [7, 6, 10, 5, 9, 2, 1, 15, 7]

arr = [1,2,3,4,5,6,7,8,9,10]

qq = QuickSort(arr)
qq.quicksort(0, len(arr)-1)
