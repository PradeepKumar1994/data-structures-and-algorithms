class Binarytree:    def __init__(self):        self.array = [0 for i in range(15)]        self.count = 0    def traverse(self, value, root = None):        if(root == None):            root = 0        if(self.array[root]!= 0):            if(value > self.array[root]):                root = root + root + 2                return self.traverse(value, root)            elif(value < self.array[root]):                root = root + root + 1                return self.traverse(value, root)        elif(self.array[root] == 0):            return root        print(value)        return "This shouldn't be returned"    def insert(self, value):        location = self.traverse(value)        self.array[location] = value        print(self.array)    def print_(self):        print(self.array)binarytree = Binarytree()binarytree.insert(21)binarytree.insert(41)binarytree.insert(51)binarytree.insert(61)binarytree.insert(1)binarytree.insert(5)binarytree.print_()