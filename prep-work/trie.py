'''
Time complexity: O()
Space complexity: O(N)
'''

class Node():
    def __init__(self):
        self.array_block = [None] * 26

class Trie():
    def __init__(self):
        self.root = Node()

    def insert(self, string):
        root = self.root
        return self._insert(root, string)

    def _insert(self, root, string):
        length = len(string)
        if(length>0):
            ascii_value = ord(string[0]) - 97
            print('ascii_value: ',ascii_value)
            if(root.array_block[ascii_value]):
                root = root.array_block[ascii_value]
                string = string[1:]
                print('rem: ',string)
                return self._insert(root, string)
            else:
                root.array_block[ascii_value] = Node()
                string = string[1:]
                print('rem: ',string)
                return self._insert(root, string)
        return None

    def test(self):
        print('--',self.root.array_block[1])
        

    def exists(self, string):
        if(len(string)>-1 and string[0]!= ' '):
            return self._exists(string, self.root)
        return None

    def _exists(self, string, root):
        if(len(string)>0):
            ascii_value = ord(string[0])-97
            if(root.array_block[ascii_value]!=None):
                string = string[1:]
                root = root.array_block[ascii_value]
                self._exists(string, root)
            else:
                return False
        return True
                

trie = Trie()
trie.insert('pradeep')
print(trie.exists('pradeep'))