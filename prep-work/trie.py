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
        if(length>-1):
            ascii_value = ord(string[0])
            print('ascii_value: ',ascii_value)
            if(root.array_block[ascii_value]):
                root = root.array_block[ascii_value]
                string = string[1:]
                print('rem: ',string)
                return self._insert(root, string)
            else:
                root[ascii_value]=Node()
                string = string[1:]
                print('rem: ',string)
                return self._insert(root, string)
        return None

    def test(self):
        print('--',self.root.array_block[1])
        

trie = Trie()
trie.insert('aba')