'''
Time complexity: O(N)
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
        return None

    def traverse(self, current_node):
        while(current_node!=None):
            if(current_node.next!=None):
                current_node = current_node.next
            else:
                return current_node

class Hashtable():
    def __init__(self):
        self.hashtable = [None]*10
        
    def hash_func(self, data):
        hash_ = int(data % 10)
        return hash_

    def print_all(self):
        print(self.hashtable)

class Hashtable_chaining(Hashtable):
    def __init__(self):
        super().__init__()

    def _hash_func(self, data):
        hash_ = super().hash_func(data)
        return hash_

    def _traverse(self, hash_):
        last_node = Linkedlist().traverse(self.hashtable[hash_])
        return last_node

    def _print(self):
        super().print_all()

    def insert(self, data):
        hash_ = self._hash_func(data)
        if(self.hashtable[hash_]==None):
            chain = Linkedlist()
            chain.insert(data)
            self.hashtable[hash_] = chain.head
        else:
            print('Data {} already exits for hash: {}'.format(data, hash_))
            self._print()
            print('\n')
            last_node = self._traverse(hash_)
            new_node = Node(data)
            last_node.next = new_node
            self._print()            


hc = Hashtable_chaining()
hc.insert(1)
hc.insert(2)
hc.insert(3)
hc.insert(4)
hc.insert(6)
hc.insert(11)
hc._print()

