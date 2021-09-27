
class Heapsort():

    def __init__(self):

        self.storage = []
        self.length = -1

    def printf(self):

        for i in self.storage:
            print('element: ',i)

    def insertion(self, data):

        if(self.length == 0):
            self.storage.append(data)
            self.length = self.length + 1

        self.storage.append(data)
        self.length = self.length+1
        return self.sort()
        
    def sort(self):

        inserted_index = self.length
        
        while(inserted_index > 0):
            if(self.storage[inserted_index] > self.storage[inserted_index]):
                print(self.storage[inserted_index])
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

        self.storage[0] = self.storage[self.length]
        self.storage[self.length] = temp
        self.length = self.length - 1
        print(self.storage)
        self._deletion()

    def _deletion(self):

        index = self.length
        left_index = (2 * max_length)+1
        right_index = (2 * max_index)+2

        while(index <= self.length):

            if(left_index > self.length):
                return None

            elif(right > self.length):
                max_index = left_index

            else:
        
                if(self.storage[left_index] > self.storage[right_index]):
                    max_index = left_index

                elif(slef.storage[left_index] < self.storage[right_index]):
                    max_index = right_index

                else:
                    mex_index = left_index

                if(self.storage[max_index] > self.storage[index]):
                    
                    temp = self.storage[max_index]
                    self.storage[max_index] = self.storage[index]
                    self.storage[index] = temp
                else:
                    return None

    def heapsort(self):

        while(self.length):
            self.delete()
            child_parent = self.length/2
            self.heapify(child_parent)
        return self.storage

    def heapify(self, parent_index):

        left_index = (2 * parent_index)+1
        rigth_index = (2 * parent_index)+2

        if(right_index > self.length):
            max_index = left_index

        else:

            if(self.storage[left_index] > self.storage[right_index]):
                max_index = left_index

            elif(self.storage[right_index] > self.storage[left_index]):
                max_index = right_index

            else:
                max_index = left_index

        if(self.storage[parent_index] < self.storage[max_index]):
            temp = self.storage[parent_index]
            self.storage[parent_index] = self.storage[main_index]
            self.storage[max_index] = temp

            return None

    
heapsort = Heapsort()

heapsort.printf()
heapsort.insertion(15)
heapsort.insertion(20)
heapsort.insertion(7)
heapsort.insertion(9)
heapsort.insertion(30)

heapsort.printf()