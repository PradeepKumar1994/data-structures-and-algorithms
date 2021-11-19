'''
E -> Nodes / number of elements
Time complexity: O(E)
Space complexity: O(E)
'''

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.root = None
        self.node = None
        self.count = 0
        self.memory = []

    def insert(self, data):
        
        if(not self.root):
            self.root = Node(data)
            self.memory.append(self.root)
            self.count = self.count + 1
        else:
            self._insert([self.root], data)

    def _insert(self, queue, data):

        if(len(queue)>0):

            if(queue[0].left == None):
                queue[0].left = Node(data)
                self.count = self.count + 1
                self.memory.append(queue[0].left)
                #print('Data: {} is inserted'.format(data))
                return None
                
            elif(queue[0].right == None):
                queue[0].right = Node(data)
                self.count = self.count + 1
                self.memory.append(queue[0].right)
                #print('Data is {} inserted'.format(data))
                return None

            else:
                queue.append(queue[0].left)
                queue.append(queue[0].right)
                del queue[0]
                self._insert(queue, data)

    def inorder_traversal(self):
        return self._inorder_traversal(self.root)

    def print_data(self, data):
        return_stack = []
        for i in data:
            return_stack.append(i.data)

        return return_stack

    def _inorder_traversal(self, root):
        
        stack = [root]
        visited = []
        current = root

        while(current!= None or len(stack) > 0):
            while(current.left!=None):
                current = current.left
                stack.append(current)

            if(len(stack) > 0):
                temp_node = stack.pop()
                visited.append(temp_node.data)

            else:
                return visited

            if(temp_node.right!=None):
                current = temp_node.right
                stack.append(current)

            if(current==None):
                current = stack[-1]

        return visited


    def preorder_traversal(self):
        return self._preorder_traversal(self.root)

    def _preorder_traversal(self, root):
    
        stack = [root]
        current_node = root
        visited = []

        while(len(stack)>0):
    
            current_node = stack.pop()

            visited.append(current_node.data)

            if(current_node.right!=None):
                stack.append(current_node.right)

            if(current_node.left!=None):
                stack.append(current_node.left)

        return visited


bs = BinaryTree()
bs.insert(1)
bs.insert(2)
bs.insert(3)
bs.insert(4)
bs.insert(5)
bs.insert(6)
bs.insert(7)
bs.insert(8)
bs.insert(9)
bs.insert(10)
bs.insert(11)

print('Inorder_traversal: ',bs.inorder_traversal())
print('Preorder_traversal: ',bs.preorder_traversal())