"""@date: 4/11/2021@author: pradeep"""#import linkedlistclass Hashtable:    def __init__(self):        self.sizeofhash = 15        self.hash = {}        for i in range(self.sizeofhash):            self.hash[i] = None            def list_(self, hashpos, value):        #if('list' in str(type(self.hash[hashpos])).split(' ')[1]):            #self.hash[hashpos].append(value)        if(self.hash[hashpos] == None):            temp = self.hash[hashpos]            if(temp == None):                self.hash[hashpos] = value            else:                                self.hash[hashpos] = temp        else:                            def insert(self, value = None):        if(value == None):            value = int(input("Please enter your value"))        def hashfunc(key):            hashpos = key % 15            return hashpos         hashpos = hashfunc(value)        self.list_(hashpos, value)           def print_table(self):        print(self.hash)#linkedlist = LinkedList()#linkedlist.insert(9)#linkedlist.insert(91)#linkedlist.insert(91)#linkedlist.insert(911)#linkedlist.insert(19)#linkedlist.insert(119)#linkedlist.print_()table = Hashtable()table.insert(10)table.insert(1)table.insert(3)table.insert(16)table.print_table()