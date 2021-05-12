
class Queue_:

    queue = []

    def __init__(self):

        self.MAX = 10

    def printall(self):

        print(Queue_.queue)

    def insertion(self):

        if(len(Queue_.queue) < self.MAX):

            value = input("Please enter the value: ")
            print('\n')

            Queue_.queue.append(value)

            print('Inserted', Queue_.queue)

        if(len(Queue_.queue) == self.MAX):

            print('---- Queue is full. Please delete few elements ----\n')
    
    def deletion(self):

        if(len(Queue_.queue) == 0):
            
            print('Queue has no elements')

        elif(len(Queue_.queue) == 1):
                
            Queue_.queue.pop()

        elif(len(Queue_.queue)>0):            
            
            for i in range(len(Queue_.queue)-1):
                
                Queue_.queue[i] = Queue_.queue[i+1]

                if(i+1 == len(Queue_.queue)-1):

                    Queue_.queue.pop()

        return None

    def details(self):

        print("\n")
        self.printall()
        print('Length of queue: ', len(Queue_.queue))



queue_ds = Queue_()

loop = True
while(loop):

    print('Enter [1] - input')
    print('Enter [2] - delete')
    print('Enter [3] - print')
    print('Enter [4] - details\n')
    
    try:
        
        decision = int(input('Enter your decision: '))

    except ValueError:

        decision = -1
        print('Invalid input \n')

    if(decision == 1):
        
        queue_ds.insertion()

    elif(decision == 2):
        
        print('Dequeue-ing: \n')
        queue_ds.deletion()
        print(queue_ds.queue)

    elif(decision == 3):

        print('Print all elements..\n')
        queue_ds.printall()

    elif(decision == 4):

        queue_ds.details()

    elif(decision == 5):
        
        print('Exiting..\n')
        loop = False

    else:
         
        print('Please enter the valid input \n')

