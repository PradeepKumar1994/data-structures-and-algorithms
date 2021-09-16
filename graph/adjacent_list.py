
class Adjacency_List():
    def __init__(self, v):
        self.storage = [[] for i in range(v)]
        self.vertices = v

    def insertion(self):
    
        for i in range(self.vertices):
            for j in range(self.vertices):
                data = int(input("Enter input for {} {}: ".format(i, j)))
                if(data):
                    self.storage[i].append(data)
                
        return None

    def _print_(self):

        return self.storage


al = Adjacency_List(4)
print(al._print_())
al.insertion()#enter some values
print(al._print_())