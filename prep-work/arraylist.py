'''
Space complexity: O(N)
'''
import ctypes

class ArrayList():
    def __init__(self):
        self.current_index = 0
        self.MAX = 1
        self.arraylist = (self.MAX*ctypes.py_object)()

    def insert(self, data):
        if(self.current_index==self.MAX):
            #time complexity: O(N)
            self.arraylist = self.increase_capacity()
            return self.insert(data)
        else:
            #armortised time complexity: O(1)
            self.arraylist[self.current_index]=data
            self.current_index = self.current_index + 1

    def resize_arraylist_check(self):
        if(self.current_index==self.MAX):
            self.arraylist = self.increase_capacity()
            print(self.arraylist._objects.values())
        return None

    def increment_current_index_insertAt(self, last_index):
        if(last_index == self.current_index-1):
            self.current_index = self.current_index + 1
        
    def insertAt(self, index, data):
        #time complexity: O(N)
        print('last',self.current_index)
        if(index<0):
            return "Please insert element greater than -1 index"
        elif(index==self.current_index):
            self.insert(data)
        elif(index>self.current_index):
            return 'Please appropriate enter index same or less than: {}'.format(self.MAX)
        else:#less than length of the array
            for i in range(self.current_index-1,index-1,-1):
                self.resize_arraylist_check()
                self.arraylist[i+1] = self.arraylist[i]
                self.increment_current_index_insertAt(i)
            self.arraylist[index] = data

    def increase_capacity(self):
        #time complexity: O(N)
        increase_cap = 2* self.MAX
        resized_array = (increase_cap*ctypes.py_object)()
        for i in range(self.current_index):
            resized_array[i] = self.arraylist[i]
        self.MAX = increase_cap
        return resized_array

    def removeAt(self, index):
        #time complexity: O(N)
        if(index<0):
            return "Please insert element greater than -1 index"
        else:
            for i in range(index,self.current_index):
                self.resize_arraylist_check()
                self.arraylist[i-1] = self.arraylist[i]
            self.arraylist[self.current_index-1]=0
            self.decrement_current_index()

    def decrement_current_index(self):
        self.current_index= self.current_index-1

    def removeEnd(self):
        self.remove()

    def print_array(self):
        print(self.arraylist[0])

array = ArrayList()
array.insert(1)
array.insert(2)
array.insert(3)
array.insert(4)
array.insert(6)
array.insert(7)
array.insert(8)
print(array.arraylist._objects.values())
array.insertAt(4,5)
print(array.arraylist._objects.values())
array.insertAt(4,5)
print(array.arraylist._objects.values())
array.removeAt(5)
print(array.arraylist._objects.values())