class DynamicArray:    MAX = 1        def __init__(self):        self.queue = []        self.count = 0        def resize(self):        if(len(self.queue) - self.count > 3):            return ""        else:            DynamicArray.MAX = DynamicArray.MAX + 1            temp = self.queue            self.queue = [0] * DynamicArray.MAX            print('DynamicArray.Max', DynamicArray.MAX)            try:                for i in range(len(temp)):                                        self.queue[i] = temp[i]                print('After resizing: ', self.queue)            except IndexError:                print(self.queue)    def printall(self):        print(self.queue)    def details(self):        print("Size of the array is: ",DynamicArray.MAX)        print("Number of elements inserted: ", self.count)        self.printall()    def insertion(self):        value = input('Value entered: ')        self.queue.insert(self.count, value)        self.count = self.count + 1        print('\n')        self.resize()    def deletion(self, position = None):        if(position == None):            if(self.count == 0):                print('No elements in the array')            if(self.count == 1):                                self.queue[0] = 0                self.queue = self.queue[:-1]                self.count = self.count - 1                DynamicArray.MAX = DynamicArray.MAX - 1             elif(self.count > 1):                                #self.queue = self.queue[i+1:]                print(self.queue[1:])                self.queue = self.queue[1:]                self.count = self.count - 1                DynamicArray.MAX = DynamicArray.MAX - 1                print('Decreased the size by one \n', len(self.queue))                print('Count: ', self.count)        else:            pass        print(self.queue)da_array = DynamicArray()loop = Truewhile(loop):    print("[1] - Insertion")    print("[2] - deletion")    print("[3] - print all element")    print("[4] - details ")    print("[5] - details \n")    try:        decision = int(input('Enter your decision: '))        if(decision == 1):            da_array.insertion()            print("Value entered")        elif(decision == 2):            da_array.deletion()        elif(decision == 3):            da_array.printall()    except ValueError:        print('Invalid input. Please try again')        da_array.details()    