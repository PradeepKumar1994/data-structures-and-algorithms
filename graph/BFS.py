
'''
Time complexity: O(V^2)
Space complexity: O(V)
'''

def depth(row, matrix, stack):
    for col in range(len(matrix)):
        if(matrix[col] == 1 and col not in stack):
            stack.append(col)
    return stack

def BFS(matrix):
    stack = []
    row = len(matrix)
    if(row > 0):
        stack.append(0)
    else:
        return None
    for i in range(row):
        stack = depth(stack[i], matrix[stack[i]], stack)
        print(stack)
    return None

matrix = [[0,1,0,1,0,0,0],[1,0,1,1,0,1,1],[0,1,0,1,1,1,0],[1,1,1,0,1,0,0],[0,0,1,1,0,0,1,],[0,1,1,0,0,0,0],[0,1,0,0,1,0,0]]
print(BFS(matrix))