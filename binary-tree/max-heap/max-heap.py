
class Maxheap():

    def __init__(self):
        self.storage = []

    def sort(self):

        new = len(self.storage)-1

        parent = (new-1)//2

        while(self.storage[new] > self.storage[parent]):

            temp = self.storage[new]
            self.storage[new] = self.storage[parent]
            self.storage[parent] = temp

            new = parent
            parent = (new-1)//2           
    
    def insertion(self, data):

        self.storage.append(data)

        self.sort()

    def getMax(self):

        return self.storage[0]

    def extractMax(self):

        extractMax = self.storage[0]
        self.storage[0] = self.storage[-1]
        self.storage.pop()

        potential_low = 0
        left_child = (2 * potential_low) + 1
        right_child = (2 * potential_low) + 2

        while(right_child < len(self.storage) and \
            (self.storage[potential_low] < self.storage[left_child] or \
             self.storage[potential_low] < self.storage[right_child])):

            if(self.storage[potential_low] < self.storage[left_child]):

                temp = self.storage[potential_low]
                self.storage[potential_low] = self.storage[left_child]
                self.storage[left_child] = temp

                potential_low = left_child
                left_child = (2 * potential_low) + 1
                right_child = (2 * potential_low) + 2

            elif(self.storage[potential_low] < self.storage[right_child]):

                temp = self.storage[potential_low]
                self.storage[potential_low] = self.storage[right_child]
                self.storage[right_child] = temp

                potential_low = left_child
                left_child = (2 * potential_low) + 1
                right_child = (2 * potential_low) + 2

        return extractMax


maxheap = Maxheap()
maxheap.insertion(37)
maxheap.insertion(1)
maxheap.insertion(23)
maxheap.insertion(2)
maxheap.insertion(27)
maxheap.insertion(3)
maxheap.insertion(6)
maxheap.insertion(7)

print(maxheap.storage)
print(maxheap.getMax())
print(maxheap.extractMax())
print(maxheap.getMax())
print(maxheap.storage)       