
'''
Time complexity: O(V^2)
Space complexity: O(V)
'''

def DFS(matrix):

    row = len(matrix)
    cols = len(matrix[0]) 
    if(row < 1):
        print(row)
        return None
    stack = [0]
    for i in range(row):
        stack = depth(matrix, i, stack)
        if(len(stack) == cols):
            return stack

    return stack

def depth(matrix, row, stack):
    
    if(len(stack) == len(matrix[row])):
        return stack

    for i in range(len(matrix[row])):
        if(matrix[row][i] > 0 and i not in stack):
            stack.append(i)
            return depth(matrix, i, stack)

    return stack


matrix = [[0,1,0,1,0,0,0],[1,0,1,1,0,1,1],[0,1,0,1,1,1,0],[1,1,1,0,1,0,0],[0,0,1,1,0,0,1,],[0,1,1,0,0,0,0],[0,1,0,0,1,0,0]]
print(DFS(matrix))
print(len(matrix[0]))