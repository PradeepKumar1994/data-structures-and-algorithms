"""
@date: 4/11/2021
@author: pradeep
"""

from linkedlist import LinkedList as linkedlist

class Hashtable:

    def __init__(self):

        self.sizeofhash = 15

        self.hash = {}

        self.hashaddress = {}

        print('Initializing Hash..','And Storage for Addresses..')

        for i in range(self.sizeofhash):

            self.hash[i] = i

            self.hashaddress[i] = i

        
    def list_(self, hashpos, value):

        if(self.hash[hashpos] == hashpos):

            temp = linkedlist().insert(value)

            print('temp: ', temp)

            self.hash[hashpos] = temp

            self.hashaddress[hashpos] = temp

        else:
                
            temp = linkedlist().insert(value)

            self.hash[hashpos].next_ = temp

            self.hashaddress[hashpos] = temp
    
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

        print('Printing hash address..')
              
        print(self.hashaddress[1])

        linkedlist().print_()


table = Hashtable()

table.insert(10)
table.insert(1)
table.insert(3)
table.insert(16)
table.insert(100)


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
