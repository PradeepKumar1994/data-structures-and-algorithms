'''
Space complexity: O(N)
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
        if(not self.head.next):
            self.node = Node(data)
            self.head.next = self.node
        else:
            self.node.next = Node(data)
            self.node = self.node.next

    def traverse_(self):
        temp_node = self.head.next

        while(temp_node!=None):
            print('Data: ',temp_node.data)
            temp_node = temp_node.next
        return None

    def reverse_linkedlist(self):
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