'''
Time complexity: O(N)
Space complexity: O(N)
'''

class Data_Structure():
    def __init__(self):
        self.data_storage = []
        self.count = 0

    def insert(self, data):
        self.data_storage.append(data)
        self.count = self.count + 1

    def print_(self):
        if(self.count > -1):
            return self.data_storage
        else:
            return -1

class Stack(Data_Structure):
    def __init__(self):
        super().__init__()

    def remove(self):
        if(self.count > -1):
            self.data_storage.pop()
            self.count = self.count - 1
        else:
            return -1

class Queue(Data_Structure):
    def __init__(self):
        super().__init__()

    def remove(self):
        if(self.count>-1):
            self.data_storage.pop(0)
        return -1

queue = Queue()
queue.insert(1)
queue.insert(2)
queue.insert(3)
queue.insert(4)
queue.remove()
queue.remove()
print('Queue:  ',queue.print_())


stack = Stack()
stack.insert(1)
stack.insert(2)
stack.insert(3)
stack.insert(4)
stack.remove()
stack.remove()
print('Stack:  ',stack.print_())
