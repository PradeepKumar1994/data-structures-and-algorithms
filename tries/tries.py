
class Node():
    def __init__(self, data):
        self.data = data
        self.children = {}
        self.is_end = False

class Tries():
    def __init__(self):
        self.root = Node('*')

    def insertion(self, word):
        current = self.root
        for letter in word:
            if(letter not in current.children):
                current.children[letter] = Node(letter)
            current = current.children[letter]
        current.is_end = True
        return False

    def find_word(self, word):
        
        if(len(word) < 1):
            return False

        current = self.root
        for letter in word:
            if(letter not in current.children):
                return False
            current = current.children[letter]
        return True


trie = Tries()

words = ['wait','Fami','waiter','waiting']
for word in words:
    trie.insertion(word)

print(trie.find_word("wait"))
print(trie.find_word("Fami"))
print(trie.find_word("waitee"))
print(trie.find_word("waiting"))