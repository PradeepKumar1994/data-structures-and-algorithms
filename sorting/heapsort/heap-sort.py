
class Heapsort():

    def __init__(self):

        self.storage = []
        self.length = -1

    def insertion(self, data):

        if(self.length == 0):
            self.storage.append(data)

        self.storage.append(data)
        self.sort()
        
    def sort():

        inserted_index = self.length

        while(inserted_index > -1):

            temp = self.storage[inserted_index/2]
            self.storage[inserted_index/2] = self.storage[inserted_index]
            self.storage[inserted_index] = temp
        
            inserted_index = inserted_index/2


            