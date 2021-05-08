"""
@date: 4/11/2021
@author: pradeep
"""

from linkedlist import LinkedList as linkedlist

class Hashtable:

    def __init__(self):

        self.sizeofhash = 15

        self.head = None

        self.hash = {}

        self.hashaddress = {}

        print('Initializing Hash..','And Storage for Addresses..')

        for i in range(self.sizeofhash):

            self.hash[i] = i

            self.hashaddress[i] = i
        
    def list_(self, hashpos, value):

        if(self.hash[hashpos] == hashpos):

            temp = linkedlist().insert(value)

            self.hashaddress[hashpos] = temp

            print('temp: ', temp) #This is a lesson, the temp will always be the same

            self.hash[hashpos] = temp

            print(self.hashaddress[hashpos])

        else:
                
            temp = linkedlist().insert(value)

            print('temp data: ',temp.data_)

            self.hash[hashpos].next_ = temp

            self.hash[hashpos] = temp
    
    def print_table(self):
        
        print(self.hash)

    def insert(self, value = None):
        
        if(value == None):

            value = int(input("Please enter your value"))
        
        def hashfunc(key):

            hashpos = key % 15

            return hashpos 

        hashpos = hashfunc(value)

        self.list_(hashpos, value)
    

    def traverse(self):

        temp_traverse = self.hashaddress[10]

        while(temp_traverse!= None):

            print('New elements: ',temp_traverse.data_)

            temp_traverse = temp_traverse.next_

        print('-----')

        print('Printing hash address..')
              
        print(self.hash[10].__dict__)

        linkedlist.print_(self.hash[10].next_)

        print(self.hashaddress[10].__dict__)

        linkedlist.print_(self.hash[10].next_)



table = Hashtable()

table.insert(10)
table.insert(1)
table.insert(3)
table.insert(16)
table.insert(100)
table.insert(1000)



table.print_table()

table.traverse()





#linkedlist = LinkedList()

#linkedlist.insert(9)
#linkedlist.insert(91)
#linkedlist.insert(91)
#linkedlist.insert(911)
#linkedlist.insert(19)

#linkedlist.insert(119)

#linkedlist.print_()
