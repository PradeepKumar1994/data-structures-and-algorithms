
'''
Time complexity: O(log N)
Space complexity: O(1)
'''

class Search():

    def __init__(self, arr, target):
        self.arr = arr
        self.target = target

    def binary_search(self):#wrapper function
        return self._binary_search(0, len(self.arr)-1)

    def _binary_search(self, low, high):

        if(low > high):
            return False

        mid = (low + high) //2

        if(self.arr[mid] == self.target):
            return True

        if(self.arr[mid] > self.target):
            return self._binary_search(low, mid-1)

        else:
            return self._binary_search(mid+1, high)

        return self.arr

arr = [1,2,3,5,6,7,11,15,18]
target = 7

bs = Search(arr, target)
print(bs.binary_search())