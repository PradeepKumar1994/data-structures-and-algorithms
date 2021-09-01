
class Minheap():

    def __init__(self):
        
        self.storage = []
        
    def insertion(self, data):

        self.storage.append(data)

        self.sort()

    def sort(self):

        if(len(self.storage) == 0):

            return None

        elif(len(self.storage) == 1):

            return self.storage

        new = len(self.storage)-1

        while(self.storage[new] < self.storage[(new-1)/2]):

            temp = self.storage[new]
            self.storage[new] = self.storage[(new-1)/2]
            self.storage[(new-1)/2] = temp
            new = (new-1)/2
            if(new == 0):
                return 
        return 

    def getMin(self):

        if(self.storage):
            return self.storage[0]

        return None

    def extractMin(self):

        extract_min = self.storage[0]
        self.storage[0] = self.storage[len(self.storage)-1/2]
        self.storage.pop()
        potential_max = 0
        while(potential_max < len(self.storage) \
                and(self.storage[potential_max] > self.storage[(2 * potential_max)+1] \
                or self.storage[potential_max] > self.storage[(2 * potential_max)+2])):
            if(self.storage[potential_max] > self.storage[(2 * potential_max)+1]):
                temp = self.storage[potential_max]
                self.storage[potential_max] = self.storage[(2 * potential_max) + 1]
                self.storage[(2 * potential_max) + 1] = temp
    
                potential_max = (2 * potential_max) + 1
            
            elif(self.storage[potential_max] > self.storage[(2 * potential_max)+2]):
                
                temp = self.storage[potential_max]
                self.storage[potential_max] = self.storage[(2 * potential_max) + 2]
                self.storage[2*(potential_max)+2] = temp

                potential_max = (2 * potential_max)+ 2

        return extract_min
        