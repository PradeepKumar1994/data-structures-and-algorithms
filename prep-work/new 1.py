
class ArrayList():
    def __init__(self, data = None):
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
        for i in range(self.length):
            new_storage[i] = self.storage[i]
        return new_storage

    
            
        