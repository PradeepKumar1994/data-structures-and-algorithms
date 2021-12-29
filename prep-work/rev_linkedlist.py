'''
Space complexity: O(N) for holding all elements
reversing a linkedlist: O(1) since no additional storage is used
'''

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Head():
    def __init__(self):
        self.next = None

class Linkedlist():
    def __init__(self):
        self.head = Head()
        self.node = None

    def insert(self, data):
        #time complexit: O(1) for one element
        #for n elements it would be O(N)
        if(not self.head.next):
            self.node = Node(data)
            self.head.next = self.node
        else:
            self.node.next = Node(data)
            self.node = self.node.next

    def traverse_(self):
        #time complexit: O(N)
        temp_node = self.head.next

        while(temp_node!=None):
            print('Data: ',temp_node.data)
            temp_node = temp_node.next
        return None

    def reverse_linkedlist(self):
        #time complexit: O(N)
        previous = None
        current = self.head.next
        next = current.next
        
        while(next!=None):
            if(previous==None):
                current.next = None #setting first node next to none
                previous = current
                current = next
                next = next.next
            else:
                current.next = previous #current node to previous node

                previous = current
                current = next
                next = next.next

        current.next = previous
        self.head.next = current

linkedlist = Linkedlist()
linkedlist.insert(1)
linkedlist.insert(2)
linkedlist.insert(3)
linkedlist.insert(4)
linkedlist.insert(5)
linkedlist.insert(6)
linkedlist.traverse_()
print('--Afer Reversing--')
linkedlist.reverse_linkedlist()
linkedlist.traverse_()
print('--Afer Reversing--')
linkedlist.reverse_linkedlist()
linkedlist.traverse_()