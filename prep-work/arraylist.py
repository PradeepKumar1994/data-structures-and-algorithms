'''
Space complexity: O(N)
'''
import ctypes

class ArrayList():
    def __init__(self):
        self.current_index = 0
        self.MAX = 1
        self.arraylist = (self.MAX*ctypes.bject)()

    def _insert(self, data):
        if(self.current_index):
            self.arraylist[]=data

    def insert(self, data):
        if(self.current_index==self.MAX):
            #time complexity: O(1)
            self.arraylist = increase_capacity()
        else:
            #auxilarated time complexity: O(1)
            if(self.current_index):
                self.arraylist[self.current_index]=data

    def insertAt(self, index, data):
        if(index<0):
            return "Please insert element greater than -1 index"
        elif(index==self.current_index):
            self.insert(data)
        elif(index>self.current_index):
            return 'Please appropriate enter index same or less than: {}'.format(self.MAX)
        else:
            pass

    def increase_capacity(self):
        increase_cap = 2* self.MAX
        resized_array = (increase_cap*ctypes.bject)()
        for i in range(self.current_index):
            resized_array[i] = self.arraylist[i]
        self.MAX = increase_cap
        return resized_array

    def removeAt(self, index):
        pass

    def remove(self)
        pass

    def removeEnd(self):
        self.remove()