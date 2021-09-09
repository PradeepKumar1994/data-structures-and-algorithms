
class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insertion(self, data):
        if(self.root == None):
            self.root = Node(data)
            return None
        else:
            return self._insertion(self.root, data)

    def _insertion(self, root, data):
        if(data < root.data):
            if(root.left == None):
                root.left = Node(data)
                return None
            else:
                return self._insertion(root.left, data)
        elif(data > root.data):
            if(root.right == None):
                root.right = Node(data)
                return None
            else:
                return self._insertion(root.right, data)
        else:
            print("This value already exists")

    def traverse(self):
        if(self.root == None):
            return None
        else:
            return self._traverse(self.root)

    def _traverse(self, current_node):
        if(current_node != None):
            self._traverse(current_node.left)
            print(current_node.data)
            self._traverse(current_node.right)
    
    def find(self, data):
        if(self.root == None):
            return None
        else:
            self._find(self.root, data)
    
    def _find(self, current_node, data):
        if(current_node.data == data):
            return current_node
        elif(data < current_node and current_node.left != None):
            return current_node.left
        elif(data > current_node and current_node,right != None):
            return current_node.right
        else:
            return None

    def delete(self, data):
        if(self.root == None):
            return "Tree empty"
        else:
            return self._delete_node(self.find(self.root, data), data)

    def _delete_node(self, current_node, data):
        
        def number_children(root):
            if(root.left != None and root.right != None):
                return 2
            elif(root.left or root.right):
                return 1
            elif(root.left == None and root.right == None):
                return 0

        def inorder_successor(current_node):
            if(curren_node != None):
                current_node = current_node.left
            return current_node

        num_children = number_children(current_node)
        target_node = self.find(data)

        if(num_children == 0):
            pass

bst = BinarySearchTree()
bst.insertion(2)
bst.insertion(5)
bst.insertion(10)
bst.insertion(7)
bst.insertion(1)

bst.traverse()