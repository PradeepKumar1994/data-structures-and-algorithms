'''
Time complexity: O(log N)
Space complexity: O(N)
'''

class Node():
    def __init__(self,data):
        self.data=data
        self.left = None
        self.right = None
    
class BinarySearch():
    def __init__(self):
        self.node = None
        self.queue = []
        self.root = None
        
    def insert(self,data):
        if(len(self.queue) == 0):
            self.node = Node(data)
            self.queue.append(self.node)
            self.root = self.node
        else:
            return self._insert(data)

    def _insert(self, data):
        if(self.node.left==None):
            self.node.left = Node(data)
            self.queue.append(self.node.left)
        elif(self.node.right==None):
            self.node.right = Node(data)
            self.queue.append(self.node.right)
            del self.queue[0]
            self.node = self.queue[0]
        return None

    def inorder(self):
        #Time complexity: O(N)
        return self._inorder(self.root)

    def _inorder(self, root):
        if(root):
            self._inorder(root.left)
            print(root.data)
            self._inorder(root.right)

    def pre_order(self):
        #Time complexity: O(N)
        return self._preorder(self.root)

    def _preorder(self, root):
        if(root):
            print(root.data)
            self._preorder(root.left)
            self._preorder(root.right)

    def post_order(self):
        #Time complexity: O(N)
        return self._postorder(self.root)

    def _postorder(self, root):
        if(root):
            self._postorder(root.left)
            self._postorder(root.right)
            print(root.data)

bs = BinarySearch()
bs.insert(1)
bs.insert(2)
bs.insert(3)
bs.insert(4)
bs.insert(5)
bs.insert(6)
print('Inorder: ')
bs.inorder()
print('Preorder: ')
bs.pre_order()
print('Postorder: ')
bs.post_order()