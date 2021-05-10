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
    

    def traverse(self, user_pos):

        print(self.hash)

        temp_traverse = self.hashaddress[user_pos]

        print('Element in the list: ')

        try:

            while(temp_traverse!= None):

                print('  ',temp_traverse.data_)

                temp_traverse = temp_traverse.next_

        except KeyError:

            print(self.hash[user_pos])



loop_condition = True

print('Please refer the list for options: ')
print('----------------------------------')
print('1: Insert new element')
print('2: Traverse for a position')


hashtable = Hashtable()


while(loop_condition):

    user_input = int(input('Enter your choice: '))

    if(user_input == 1):

        value = int(input('Enter the value to be inserted: '))

        hashtable.insert(value)

    elif(user_input == 2):

        user_pos = int(input('Please enter the position in the hashtable: '))

        hashtable.traverse(user_pos)



table = Hashtable()

table.insert(10)
table.insert(1)
table.insert(3)
table.insert(16)
table.insert(100)
table.insert(1000)



table.print_table()

table.traverse()


