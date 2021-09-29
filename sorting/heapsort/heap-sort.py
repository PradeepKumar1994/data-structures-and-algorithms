
class Heapsort():

    def __init__(self):

        self.storage = []
        self.length = -1

    def printf(self):
        return self.storage
        
    def insertion(self, data):

        if(self.length == 0):
            self.storage.append(data)
            self.length = self.length + 1
            return None

        self.storage.append(data)
        self.length = self.length+1
        
        return self.sort()
        
    def sort(self):
        
        inserted_index = self.length
        
        while(inserted_index > -1):
            if(self.storage[inserted_index] > self.storage[inserted_index//2]):
                temp = self.storage[inserted_index//2]
                self.storage[inserted_index//2] = self.storage[inserted_index]
                self.storage[inserted_index] = temp
            
                inserted_index = inserted_index//2
            else:
                print(self.storage)
                return None
        print(self.storage)
        return None

    def deletion(self):

        if(self.length < 1):
            return None

        temp = self.storage[0]
        self.storage[0] = self.storage[self.length]
        self.storage[self.length] = temp
        self.length = self.length - 1
        return self._deletion()

    def _deletion(self):
        
        index = 0
        left_index = (2 * index)+1
        right_index = (2 * index)+2
        print(' {}   {} '.format(self.storage[left_index], self.storage[right_index]))
        while(index >= 0):

            if(self.storage[left_index] > self.storage[right_index]):
                max_index = left_index

            elif(self.storage[left_index] <= self.storage[right_index]):
                max_index = right_index

            if(self.storage[max_index] > self.storage[index]):
                
                temp = self.storage[max_index]
                self.storage[max_index] = self.storage[index]
                self.storage[index] = temp
                index = index - 1
            else:
                print('ARR: ',self.storage)
                return None


    def heapsort(self):

        while(self.length):
            self.deletion()
            print('--->',self.printf())
            print('length of arr: ', self.length)
            child_parent = self.length//2
            self.heapify(child_parent)
        return self.storage

    def heapify(self, parent_index):

        left_index = (2 * parent_index)+1
        right_index = (2 * parent_index)+2

        if(right_index > self.length):
            return None

        else:

            if(self.storage[left_index] > self.storage[right_index]):
                max_index = left_index

            elif(self.storage[right_index] > self.storage[left_index]):
                max_index = right_index

            else:
                max_index = left_index

            if(self.storage[parent_index] < self.storage[max_index]):
                temp = self.storage[parent_index]
                self.storage[parent_index] = self.storage[max_index]
                self.storage[max_index] = temp

        return None

    
heapsort = Heapsort()

heapsort.printf()
heapsort.insertion(15)
heapsort.insertion(5)
heapsort.insertion(20)
heapsort.insertion(1)
heapsort.insertion(17)
heapsort.insertion(10)
heapsort.insertion(30)

print('returning: ',heapsort.printf())

heapsort.heapsort()

print('returning II: ',heapsort.printf())