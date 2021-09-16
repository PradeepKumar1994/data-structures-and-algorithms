

class Adjacency_Matrix():
    def __init__(self, v):
        self.storage = [[0 for i in range(v)]] * v
        self.vertices = v

    def insertion(self):
        
        for i in range(self.vertices):
            for j in range(self.vertices):
            
                data = int(input('Please enter the value: {} {}'.format(i, j)))

                if(data):
                    self.storage[i][j] = 1
                else:
                    self.storage[i][j] = 0

        return None


    def _print_(self):
        return self.storage


am = Adjacency_Matrix(6)
print(am._print_())
am.insertion()#enter some values
print(am._print_())