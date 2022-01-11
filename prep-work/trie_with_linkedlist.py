'''
Time complexity: O(S)
Space complexity: O(S)
'''

class Node():
    def __init__(self, char):
        self.char = char
        self.hashtable = {}

class Head():
    def __init__(self):
        self.hashtable = {}

class Trie():
    def __init__(self):
        self.root = Head()

    def insert(self, string_):
        if(len(string_)<1):
            return "Please enter a valid string"
        else:
            return self._insert(string_, self.root)

    def create_node(self, char):
        node = Node(char)
        return node

    def _insert(self, string_, root):
        if(len(string_)>0):
            print('string: ',string_)
            char = string_[0]
            string_ = string_[1:]
            if(char in root.hashtable.keys()):
                return self._insert(string_, root.hashtable[char])
            else:
                node = self.create_node(char)
                root.hashtable[char] = node
                return self._insert(string_, root.hashtable[char])

    def find(self, string_):
        if(len(string_)==0):
            return "Valid string, please"
        else:
            return self._find(string_, self.root)

    def _find(self, string_, root):
        if(string_!=''):
            char = string_[0]
            string_ = string_[1:]
            if(char in root.hashtable.keys()):
                return self._find(string_, root.hashtable[char])
            else:
                return False
        return True

trie = Trie()
trie.insert('pradeep')
trie.insert('naren')
trie.insert('sheshu')
trie.insert('praneeth')
print('--',trie.find('shesh'))