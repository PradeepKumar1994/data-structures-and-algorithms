

class Node:
    
    #Nodes are created here

    def __init__(self, data):

        self.data_ = data

        self.next_ = None


class LinkedList:

    def __init__(self):

        self.head = None

        self.node = None

        self.count = 0

        self.last = None

    def print_(self, init_address = None):

        temp = init_address

        print('---------')
        while temp != None:

            print('This is data: ',temp.data_)

            temp = temp.next_

            print('THis is address:',temp)
            
            #print('this is address: ', temp.next_)


    def insert(self, value, option = None):

        if(self.head == None):

            self.head = Node(value)
            print('=------=')
            print(self.head.data_)

            self.last = self.head

        elif(self.node == None):

            self.node = Node(value)        
            
            self.head.next_ = self.node
            
            print('Data inserted:',self.node.data_)

            self.last = self.node

        else:
            
            temp_node = Node(value)
        
            self.node.next_ = temp_node

            print('Previous Node for next address: ',self.node.next_)

            self.node = temp_node
            
            print('While insertion data ',self.node.data_)
            
            self.last = self.node

        self.count = self.count + 1

        return self.last







#linkedlist = LinkedList()

#linkedlist.insert(9)
#linkedlist.insert(91)
#linkedlist.insert(91)
#linkedlist.insert(911)
#linkedlist.insert(19)

#linkedlist.insert(119)

#linkedlist.print_()
