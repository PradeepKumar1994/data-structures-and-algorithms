'''
Time complexity: 
Space complexity:
'''
class Binary_Search():
    def __init__(self, data):
        self.data = data

    def binary_search_recur(self, target, low, high):
        if(low<=high):
            mid = (low+high)//2
            if(self.data[mid]==target):
                return True
            elif(self.data[mid]>target):
                return self.binary_search_recur(target, low, mid-1)
            elif(self.data[mid]<target):
                return self.binary_search_recur(target, mid+1, high)
        return False

    def binary_search_iter(self, target, low, high):
        while(low<=high):
            mid = (low+high)//2
            if(self.data[mid]==target):
                return True
            elif(self.data[mid]>target):
                high = mid - 1 
            elif(self.data[mid]<target):
                low = mid + 1
        return False


array = [0,1,2,3,4,5,6,7,8,9]
bs=Binary_Search(array)
print(bs.binary_search_recur(11, 0, 9))
print(bs.binary_search_iter(10, 0, 9))
