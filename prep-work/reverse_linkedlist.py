
class Head():
    def __init__(self):
        self.next = None

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist():
    def __init__(self):
        self.head = Head()
        self.node = None
        self.arraylist = []
        self.count = 0

    def add_element(self, data):
        if(not self.head.next):
            self.node = Node(data)
            self.head.next = self.node
            self.count = self.count + 1
            self.arraylist.append(self.node)
        else:
            self.node.next = Node(data)
            self.node = self.node.next
            self.count = self.count + 1
            self.arraylist.append(self.node)

    def reverse_linkedlist(self):
        temp_count = self.count - 1
        while(temp_count > -1):
            if(temp_count==0):
                self.arraylist[temp_count].next = None
                self.node = self.arraylist[temp_count]
            elif(temp_count == self.count - 1):
                self.head.next = self.node
                self.arraylist[temp_count].next = self.arraylist[temp_count-1]                
            else:
                self.arraylist[temp_count].next = self.arraylist[temp_count-1]
            temp_count = temp_count - 1
        self.arraylist = self._rev_arraylist()

        return None
        
    def _rev_arraylist(self):
        stack = []
        temp_count = self.count - 1
        while(temp_count>-1):
            stack.append(self.arraylist[temp_count])
            temp_count = temp_count - 1

        return stack

    def print_data(self):
        temp_node = self.head.next 
        print('HEAD: ',temp_node)
        while(temp_node):
            print('Next: {} Data: {}'.format(temp_node.next, temp_node.data))
            if(temp_node.next != None):
                temp_node = temp_node.next
            else:
                return None
        
    def print_next(self):

        temp_node = self.head.next
        while(temp_node):
            print(temp_node.next)
            temp_node = temp_node.next
        return None

    def print_details(self):
        for i in self.arraylist:
            print(i.data)
        return None

ll = Linkedlist()
ll.add_element(1)
ll.add_element(2)
ll.add_element(3)
ll.add_element(4)
ll.add_element(5)
ll.reverse_linkedlist()
ll.print_data()
print('---')
print(ll.node)
print(ll.head.next)
print('---')
ll.reverse_linkedlist()
ll.print_data()
print('---')
ll.reverse_linkedlist()
ll.print_data()