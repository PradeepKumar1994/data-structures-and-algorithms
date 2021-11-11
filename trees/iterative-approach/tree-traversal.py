
class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.root = None
        self.node = None
        self.count = None

    def insert(self, data):
        
        if(not self.root):
            self.root = Node(data)
        else:
            self._insert()


    def add(self, stack):

        if(len(stack)>0):
            root = stack[-1]
            if(root.right!=None):
                stack.append(root.right)

            stack.append(root)

            if(root.left!=None):
                stack.append(root.left)

            