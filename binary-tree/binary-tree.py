
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

        return self.result['preorder']


    def postorder(self, root = None):

        print('--------POST ORDER TRAVERSAL -----------')

        print('Current root is: ', root)

        if(root == None):

            root = 0

            if(self.queue[root] == 0):

                return "Empty tree, please insert elements"

        else:

            left = root + root + 1

            right = root + root + 2

            try:
                if(self.array[left] == 0 and self.array[right] == 0):

                    self.result['postorder'].append(self.array[root])

                elif((self.array[left] in self.result['postorder'] and self.array[right] in self.queue[right]) \
                        or (self.array[left] in self.result['postorder'] and self.array[right] == 0) \
                        or (self.array[right] in self.result['postorder'] and self.array[left] == 0)):

                    self.result['postorder'].append(self.array[root])

                if(self.array[left] != 0):
                
                    self.stack.append(left)
                    print(self.stack)
                    self.postorder(left)

                if(self.array[right] != 0):
                    
                    print('Current root is: ', root)
                    self.stack.append(right)
                    print(self.stack)
                    self.postorder(right)

            except IndexError:

                
                self.result['postorder'].append(self.array[root])
                
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

result = binarytree.postorder(root = 0)
print(result)
#binarytree.inorder_preprocess()