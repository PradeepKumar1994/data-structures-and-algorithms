
class ArrayList():
    def __init__(self, data = None):
        self.MAX_SIZE = 1
        if(data==None):
            self.storage = [None]
            self.length = 0
        else:
            self.storage = [data]
            self.length = 1
            self.storage = self.storage_resize()

    def increase_length(self):
        self.length = self.length + 1

    def decrease_length(self):
        self.length = self.length - 1

    def storage_resize(self):
        temp = self.length
        self.MAX_SIZE = self.length * 2
        new_storage = [None] * self.MAX_SIZE
        for i in range(0,self.length):
            new_storage[i] = self.storage[i]
        return new_storage

    def append(self, data):
        if(self.length == self.MAX_SIZE):
            self.storage = self.storage_resize()
        self.storage[self.length] = data
        self.increase_length()

    def pop(self, index = None):
        if(self.length < 1):
            return 'Empty ArrayList'
        else:
            return self._pop(index)
    
    def _pop(self, index):
        if(index == None):
            self.storage[self.length-1] = None
        elif(index < -1 and index > self.length-1):
            return "Please provide valid index"
        else:
            self.storage[index] = None
        self.decrease_length()

    def print_(self, first=None, last=None):
        if(first==None and last==None):
            return self.storage[0:self.length]
        elif(first < 0 and last > self.length):
            return 'IndexOutOfBounds'
        else:
            return self.storage[first:last]

list_ = ArrayList()
list_.append(1)
list_.append(2)
list_.append(4)
list_.append(3)
list_.append(7)
list_.append(1)
print(list_.print_())
list_.pop()
print(list_.print_())
