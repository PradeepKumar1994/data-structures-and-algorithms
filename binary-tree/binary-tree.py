
"""

@author: Pradeep

"""

class Binarytree:

    def __init__(self):

        self.array = [0 for i in range(15)]

        self.count = 0

        self.queue = []
        self.result = {'preorder': [], 'postorder': [], 'inorder':[]}
        self.stack = []
 
    def preorder(self, root = None):

        if(root == None):

            root = 0

            if(self.array[root] != 0):
                
                self.result['preorder'].append(self.array[root])

                print(self.result['preorder'])

            elif(self.array[root] == 0):

                return 'Empty Tree'

        if(len(self.stack) != 0):

            left = root + root + 1

            right = root + root + 2

            try:
                
                print('left root value: ', left)
                
                if(self.array[left]!= 0):
                    self.stack.append(left)
                    self.result['preorder'].append(self.array[left])
                    self.preorder(left)

                print('right root value: ', right)

                if(self.array[right] != 0):

                    self.stack.append(right)

                    self.result['preorder'].append(self.array[right])

                    self.preorder(right)

            except IndexError:

                print('root exception value: ', root)

        print('Stack: ',self.stack)

        self.stack = []

        return self.result['preorder']


    def postorder(self, root = None):

        if(root == None):

            root = 0

            if(self.queue[root] == 0):

                return "Empty tree, please insert elements"

        else:

            left = root + root + 1

            right = root + root + 2

            if(right >= len(self.array)):

                return None

            try:
                    
                print('left :', left)
                print('right: ', right)

                if(self.array[left] != 0):
                    print('Current element: ',self.array[left])
                    self.postorder(left)
                #else:
                    #self.result['postorder'].append(self.array[root])

                if(self.array[right] !=0):
                    print('Current right element: ', self.array[right])
                    self.postorder(right)
                #else:
                 #   self.result['postorder'].append(self.array[root])

                if(self.array[root] != 0):
                    
                    self.result['postorder'].append(self.array[root])
                    
                print('')

            except IndexError:

                print('------------')
                print('Left: ', left)
                print('Right: ', right)
                print('Root: ', root)

        return self.result['postorder']


    def traverse(self, value, root = None):

        if(root == None):

            root = 0

        if(self.array[root]!= 0):

            if(value > self.array[root]):

                root = root + root + 2

                return self.traverse(value, root)

            elif(value < self.array[root]):

                root = root + root + 1

                return self.traverse(value, root)

        elif(self.array[root] == 0):

            return root

        print(value)

        return "This shouldn't be returned"


    def insert(self, value):

        location = self.traverse(value)

        self.array[location] = value

        print(self.array)

        if(location == 0):

            self.stack.append(location)

    def print_(self):

        print(self.array)


        




binarytree = Binarytree()

binarytree.insert(7)
binarytree.insert(20)
binarytree.insert(5)
binarytree.insert(15)
binarytree.insert(10)
binarytree.insert(4)
binarytree.insert(33)
binarytree.insert(2)
binarytree.insert(25)
binarytree.insert(6)
binarytree.print_()

#result = binarytree.preorder()
#print(result)

print('--------POST ORDER TRAVERSAL -----------')

result = binarytree.postorder(root = 0)
print(result)
#binarytree.inorder_preprocess()