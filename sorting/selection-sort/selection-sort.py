
#Runtime(O(n^2))

class SelectionSort():
    def __init__(self, arr):
        self.arr = arr

    def swap(self, min, i):
        temp = self.arr[min]
        self.arr[min] = self.arr[i]
        self.arr[i] = temp
        
    def sorting(self):
        n = len(self.arr)
        for i in range(n-1):
            min = i
            for j in range(i+1,n):
                if(self.arr[min] > self.arr[j]):
                    min = j
            if(min!=i):
                self.swap(min, i)
        return self.arr

ss = SelectionSort([7,4,10,8,3,1])
print(ss.sorting())