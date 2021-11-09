
'''
Time complexity: 
Space complexity: 
'''

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Linkedlist():
    def __init__(self):
        self.root = None
        self.node = None
        self.count = 0
        self.memory = []

    def insert(self, data):
        if(self.root == None):
            self.node = Node(data)
            self.root = self.node
            self.memory.append(self.root)
            print('Data added: ', self.root.data)
        else:
            return self._insert([self.root], data)

    def print_tree(self):
        for i in self.memory:
            print(i)
        
    def _insert(self, queue, data):
        if(len(queue) <= 0):
            print('Something went wrong')
            return None

        if(queue[0].left == None):
            temp = Node(data)
            queue[0].left = temp
            self.memory.append(temp)
            self.node = temp
            print('Data added: ', data)
            return None

        elif(queue[0].right == None):
            temp = Node(data)
            queue[0].right = temp
            self.memory.append(temp)
            self.node = temp
            print('Data added: ', data)
            return None
        else:
            queue.append(queue[0].left)
            queue.append(queue[0].right)
            del queue[0]
            return self._insert(queue, data)

    def inorder(self):
        print('----')
        return self._inorder(self.root)

    def _inorder(self, root):
        if(root):
            self._inorder(root.left)
            print(root.data)
            self._inorder(root.right)

 
ll = Linkedlist()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)
ll.insert(7)
ll.insert(8)
ll.insert(9)
ll.insert(10)
ll.insert(11)
ll.inorder()
