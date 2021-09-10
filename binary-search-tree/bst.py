# Logic is obtained from
#https://www.youtube.com/watch?v=Zaf8EOVa72I&t=0s


class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

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
                root.left.parent = root
                return None
            else:
                return self._insertion(root.left, data)
        elif(data > root.data):
            if(root.right == None):
                root.right = Node(data)
                root.right.parent = root
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
            return self._find(self.root, data)
    
    def _find(self, current_node, data):
        if(current_node.data == data):
            return current_node
        elif(data < current_node.data and current_node.left != None):
            return current_node.left
        elif(data > current_node.data and current_node,right != None):
            return current_node.right
        return None

    def delete(self, data):
        if(self.root == None):
            return "Tree empty"
        else:
            target = self.find(data)
            if(target):
                return self._delete_node(target, data)
        return "Element not found"

    def _delete_node(self, target_node, data):
        
        def number_children(root):
            if(root.left != None and root.right != None):
                return 2
            elif(root.left or root.right):
                return 1
            elif(root.left == None and root.right == None):
                return 0

        def inorder_successor(current_node):
            if(current_node != None):
                current_node = current_node.left
            return current_node

        num_children = number_children(target_node)

        if(num_children == 0):
            if(target_node.parent.left == target_node):
                target_node.parent.left = None
            else:
                target_node.parent.right = None

        elif(num_children == 1):
            if(target_node.left): #equal node exists
                child_node = target_node.left
            else:
                child_node = target_node.right
            
            if(target_node.parent.left == node):
                target_node.parent.left = child_node
            else:
                target_node.parent.right = child_node

        else:
            successor_node = inorder_successor(target_node.right)
            target_node.data = successor_node.data
            return self.deletion(successor, successor.data)
                


bst = BinarySearchTree()
bst.insertion(2)
bst.insertion(5)
bst.insertion(10)
bst.insertion(7)
bst.insertion(1)
bst.insertion(12)
bst.insertion(21)
bst.insertion(33)

bst.traverse()

bst.delete(1)
print()
bst.traverse()
