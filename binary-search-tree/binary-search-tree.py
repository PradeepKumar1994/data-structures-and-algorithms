class Node():

    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

class BinarySearchTree():

    def __init__(self):

        self.node = None
        self.root = None

    def insertion(self, data):

        if(not self.root):

            self.root = Node(data)
            return 

        temp_root = self.root

        while(temp_root != None):
            if(data > temp_root.data):
                if(temp_root.right == None):
                    self.node = Node(data)
                    temp_root.right = self.node
                    return
                else:
                    temp_root = temp_root.right
            else:
                if(temp_root.left == None):
                    self.node = Node(data)
                    temp_root.left = self.node
                    return 
                else:
                    temp_root = temp_root.left
                    

        return "This should not be executed"
        




bst = BinarySearchTree()

bst.insertion(5)
bst.insertion(11)
bst.insertion(9)
bst.insertion(4)
bst.insertion(1)