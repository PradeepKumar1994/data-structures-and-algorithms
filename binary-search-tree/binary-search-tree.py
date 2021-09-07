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
            return self.root

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
        
    def traversal(self, root):
        #inorder
        
        if(root):

            self.traversal(root.left)
            print(root.data)
            self.traversal(root.right)

    def Inordersuccessor(self, current):
        
        while(current):
            if(current.left == None):
                tmp = current
                current.left = None
                if(current.right is not None):
                    return tmp.data, current.right
                else:
                    return tmp.data, None
            
            current = current.left

        return None

    def deletion(self, data):

        if(self.root == None):

            return not None

        current, previous = self.root, self.root

        while(current):
            
            if(data == current.data):
                #case 1: no children
                if(not current.left and not current.right):
                    if(current == self.root):
                        self.root = None
                    else:
                        if(data < previous.data):
                            previous.left = None
                            return None
                        else:
                            previous.right = None
                            return None
                #case 2: two children
                elif(current.left is not None and current.right is not None):
                    print('Two children case')
                    temp = current.data
                    current.data, right_node = self.Inordersuccessor(current.right)
                    print("Data to be deleted {} replaced with {} ".format(temp, current.data))
                    if(right_node):
                        print('right node', right_node)
                        previous.left = right_node
                        return None

                #case 3: one child
                else:
                    #This logic is flawed
                    if(not current.left):

                        if(data < previous.data):
                            
                            previous.left = current.right
                            return None
                        else:

                            previous.right = current.right
                            return None

                    else:
                        if(data < previous.data):
                            previous.left = current.left
                            return None
                        else:
                            previous.right = current.left
                            return None
            else:
                previous = current
                if(data < current.data):
                    current = current.left
                else:
                    current = current.right

        return "Does not exist"


bst = BinarySearchTree()

root = bst.insertion(50)
bst.insertion(30)
bst.insertion(20)
bst.insertion(40)
bst.insertion(70)
bst.insertion(60)
bst.insertion(80)
print(bst.deletion(1))
print(bst.deletion(20))
print(bst.deletion(30))
print(bst.deletion(50))


bst.traversal(root)

