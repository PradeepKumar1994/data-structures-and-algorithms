
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

                if(self.array[root] not in self.result['preorder']):

                    self.result['preorder'].append(self.array[root])
                
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

        self.stack = [0]

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
                    
                if(self.array[left] != 0):
                    print('Current element: ',self.array[left])
                    self.stack.append(self.array[left])
                    self.postorder(left)
                else:
                    self.result['postorder'].append(self.stack[-1])
                    self.stack.pop()

                if(self.array[right] !=0):
                    print('Current right element: ', self.array[right])
                    self.postorder(right)
                else:
                 self.result['postorder'].append(self.array[root])

                if(self.array[root] != 0):
                    
                    self.result['postorder'].append(self.array[root])
                    

            except IndexError:

                print('------------')
                print('Left: ', left)
                print('Right: ', right)
                print('Root: ', root)

        return self.result['postorder']

    def inorder(self, root = None):

        if(root == None):

            root = 0

            if(self.array[root] != 0):
                
                self.result['inorder'].append(self.array[root])

                print('This should only execute if root = None',self.result['inorder'])

            elif(self.array[root] == 0):

                return 'Empty Tree'


        if(len(self.stack) != 0):

            left = root + root + 1

            right = root + root + 2

            try:
                
                if((self.array[left]!= 0)):

                    if(self.array[left] not in self.result['inorder']):

                        self.stack.append(left)
                        self.inorder(left)
                        print('Left code block')
                        print('Element to be addded: ', self.array[left])
                        print('Result: ', self.result['inorder'])
                        self.result['inorder'].append(self.array[left])
                        print('Element Added: ', self.result['inorder'])
                        print()

                elif(self.array[root] not in self.result['inorder']):

                    print('Root code block')
                    print('Element to be added', self.array[root])
                    print('Result', self.result['inorder'])
                    self.result['inorder'].append(self.array[root])
                    print('Element added: ',self.result['inorder'])
                    print()
  
                if(self.array[right] != 0):

                    if(self.array[right] not in self.result['inorder']):

                        self.stack.append(right)
                        self.inorder(right)
                        print('Right code block')
                        print('Element to be added',self.array[right])
                        print('Result', self.result['inorder'])
                        self.result['inorder'].append(self.array[right])
                        print('Element Added: ',self.result['inorder'])
                        print()

            except IndexError:

                print()

        print('All function executed: ',self.result['inorder'])

        return self.result['inorder']

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

    def search_(self, search_val, location=0):

        if(location >= len(self.array)):
        
            return "Element not found"

        elif(search_val == self.array[location]):
    
            str_ = "Found at: ", + location

            return str_

        else:

            if(search_val < self.array[location]):

                location = location + location + 1

                return self.search_(search_val, location)
            
            location + location + 2
    
            return self.search_(search_val, location)
        

    def search_linear(self, search_element):

        str_ = "Element not found"

        for i in self.array:

            if(search_element == i):

                str_ = "Element found {}".format(self.array.index(i))

                return str_

        return str_

    
    def binary_tree_search(self, search_element, root = 0):

        if(root >= len(self.array)):

            print('Element not found')

        elif(self.array[root] == search_element):

            print('Element Found!')

            return

        elif(search_element < self.array[root]):

            left = root + root + 1

            self.binary_tree_search(search_element, left)

            return

        else:

            right = root + root + 2

            self.binary_tree_search(search_element, right)

        return "This should not happen"



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
#binarytree.print_()




result = binarytree.postorder(root = 0)
print('-------- POST-ORDER TRAVERSAL -----------')
print(result)
#binarytree.inorder_preprocess()

result = binarytree.preorder(root = 0)
print('-------- PRE-ORDER TRAVERSAL -----------')
print(result)

print('------- IN-ORDER TRAVERSAL--------')
result = binarytree.inorder(root = 0)
print(result)

print('---- Binary Tree Search ----')
print(binarytree.search_(2))



result = binarytree.search_linear(7)
print(result)


print('-----------------------------')

result = binarytree.binary_tree_search(6)
print(result)


