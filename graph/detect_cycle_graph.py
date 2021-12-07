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
        last_row = 0
        for i in range(rows):
            decision = self._dfs(stack, i, last_row, rows)
            if(decision == True):
                return True
        return False

#re-evaluate your logic and consider pop when necessary
    def _dfs(self, stack, current_row, last_row, rows):
        print(current_row)
        matrix_row = self.matrix[current_row]
        for col_number in range(0, rows):
            if(matrix_row[col_number] == 1):
                if(col_number not in stack):
                    stack.append(col_number)
                    print('-->',stack)
                    self._dfs(stack, col_number, current_row, rows)
                else:
                    print(stack)
                    return True
        return False


#          0,1,2,3,4,5
#matrix = [[0,1,0,0,1,0],\
#          [1,0,1,0,1,0],\
#          [0,0,0,1,0,1],\
#          [0,0,1,0,0,0],\
#          [1,1,0,0,0,0],\
#          [0,0,1,0,0,0]]

          #0,1,2,3,4,5
matrix = [[0,1,0,0,0,0],\
          [0,0,1,0,0,0],\
          [0,0,0,1,0,0],\
          [0,0,0,0,1,0],\
          [0,0,0,0,0,1],\
          [1,0,0,0,0,0]]

mat = Graph(matrix)
outcome = mat.dfs()
if(outcome==True):
    print('Graph has cycle')
elif(outcome!=None):
    print('Graph len is not sufficient')
else:
    print('Graph has no cycle')