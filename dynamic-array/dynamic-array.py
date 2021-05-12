"""
@date: 3/25/2021
@author: pradeep
"""
class DynamicArray:

    MAX = 2
    
    def __init__(self):

        self.queue = []

        self.count = 0

        self.size_of_queue = len(self.queue)
    
    def resize(self):

        DynamicArray.MAX = DynamicArray.MAX + (self.count - 1)

        print('Value changing: ',DynamicArray.MAX)

        for i in range(self.count-1):

            self.queue.append(0)


    def printall(self):

        print(self.queue)

    def details(self):

        print("Size of the array is: ",DynamicArray.MAX)

        print("Number of elements inserted: ", self.count)

        self.printall()

    def insertion(self, position = None):

        value = input('Value enter: ')

        while(value == 0):

            value = input('Value entered: ')
        
        self.queue.insert(self.count, value)

        self.count = self.count + 1

        print('size of Array: ',DynamicArray.MAX)

        if(DynamicArray.MAX == len(self.queue)):#condition change

            print('resize initiated.')

            self.resize()
            
            print('resizing complete')

    def deletion(self, position = None):

        if(position == 'n'):

            pass

        if(self.count == 0):

            print('No elements in the array')

        if(self.count == 1):
            
            self.queue[0] = 0

            self.queue = self.queue[:-1]

            self.count = self.count - 1

            #DynamicArray.MAX = DynamicArray.MAX - 1 

        elif(self.count > 1):
            
            #self.queue = self.queue[i+1:]
            print(self.queue[1:])
            self.queue = self.queue[1:]

            self.count = self.count - 1

            #DynamicArray.MAX = DynamicArray.MAX - 1

            print('Decreased the size by one \n', len(self.queue))

            print('Count: ', self.count)


        print(self.queue)
    
    def details(self):

        print('self.count: ',self.count)
        print('Size of array: ', len(self.queue))
        print('DynamicArray.MAX', DynamicArray.MAX)
        print('Array: ',self.queue)



da_array = DynamicArray()

loop = True

while(loop):

    print("[1] - Insertion")
    print("[2] - deletion")
    print("[3] - print all element")
    print("[4] - details ")
    print("[5] - details \n")

    try:

        decision = int(input('Enter your decision: '))

        if(decision == 1):

            da_array.insertion()

            print("Value entered")

        elif(decision == 2):

            da_array.deletion()
            #position_decision = input('Would you like to enter the position: [y/n]: ')

        elif(decision == 3):

            da_array.printall()

        elif(decision == 4):

            da_array.details()

    except ValueError:

        print('Invalid input. Please try again')
        da_array.details()

    