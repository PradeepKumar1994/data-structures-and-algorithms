
class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.root = None
        self.node = None
        self.count = 0
        self.memory = []

    def insert(self, data):
        
        if(not self.root):
            self.root = Node(data)
            self.memory.append(self.root)
            self.count = self.count + 1
        else:
            self._insert([self.root], data)

    def _insert(self, queue, data):

        if(len(queue)>0):

            if(queue[0].left == None):
                queue[0].left = Node(data)
                self.count = self.count + 1
                self.memory.append(queue[0].left)
                #print('Data: {} is inserted'.format(data))
                return None
                
            elif(queue[0].right == None):
                queue[0].right = Node(data)
                self.count = self.count + 1
                self.memory.append(queue[0].right)
                #print('Data is {} inserted'.format(data))
                return None

            else:
                queue.append(queue[0].left)
                queue.append(queue[0].right)
                del queue[0]
                self._insert(queue, data)

    def add(self, stack):

        if(len(stack)>0):
            root = stack[-1]
            if(root.right!=None):
                stack.append(root.right)

            stack.append(root)

            if(root.left!=None):
                stack.append(root.left)

        return stack

    def inorder_traversal(self):
        return self._inorder_traversal(self.root)

    def _inorder_traversal(self, root):
        
        stack = [root]
        visited = []
        while(len(visited)-1 == self.count):
            while(stack[-1].left!=None and stack[-1].data not in visited):
                stack = self.add(stack)
                
            if(stack[-1].left == None):
                temp = stack.pop().data
                visited.append(temp)

            if((stack[-1].left).data in self.visited):
                temp = stack.pop().data
                print('Visiting: {}'.format(temp))
                visited.append(temp)

            if(stack[-1].right == None):
                temp = stack.pop().data
                print('Visiting: {}'.format(temp))
                visited.append(temp)

            elif(stack[-1].right != None):
                stack = self.add(stack[-1])

        return visited

bs = BinaryTree()
bs.insert(1)
bs.insert(2)
bs.insert(3)
bs.insert(4)
bs.insert(5)
bs.insert(6)
bs.insert(7)
bs.insert(8)
bs.insert(9)
bs.insert(10)
bs.insert(11)

print(bs.inorder_traversal())