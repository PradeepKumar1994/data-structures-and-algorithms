'''
Time complexity: 
Space complexity: 
'''

class Graph():
    def __init__(self, martix):
        self.matrix = matrix

    def dfs(self):
        if(len(matrix)<2):
            return None

        rows = len(self.matrix[0])
        cols = rows

        stack = [0]

        for i in range(rows):
            decision = self._dfs(stack, self.matrix[i], rows)
            if(decision == True):
                return True
        return False

    def _dfs(self, stack, matrix_row, rows):
        out = False
        for col_number in range(rows):
            if(matrix_row[col_number] == 1):
                if(col_number not in stack):
                    stack.append(col_number)
                    self._dfs(stack, self.matrix[col_number], rows)
                elif(col_number !=0 and col_number in stack):
                    stack.append(col_number)
                    out = self._check_loop(stack)
                    return out
        
        return out

    def _check_loop(self, stack):
        
        if(len(stack)>1):
            if(self.matrix[stack[-2]][stack[-1]]==1):
                print(stack)
                return True

        return False


matrix = [[0,1,0,0,1,0,0],[1,0,1,0,1,0,0],[0,1,0,1,0,1,1],[0,0,1,0,0,0,0],[1,1,0,0,0,0,0],[0,0,1,0,0,0,0]]

mat = Graph(matrix)
print(mat.dfs())