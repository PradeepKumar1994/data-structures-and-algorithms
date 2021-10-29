
'''
Time complexity: O(V^2)
Space complexity: O(V)
'''

def depth(row, matrix, queue):
    for col in range(len(matrix)):
        if(matrix[col] == 1 and col not in queue):
            queue.append(col)
    return queue

def BFS(matrix):
    queue = []
    row = len(matrix)
    if(row > 0):
        queue.append(0)
    else:
        return None
    for i in range(row):
        queue = depth(queue[i], matrix[queue[i]], queue)
        print(queue)
    return None

matrix = [[0,1,0,1,0,0,0],[1,0,1,1,0,1,1],[0,1,0,1,1,1,0],[1,1,1,0,1,0,0],[0,0,1,1,0,0,1,],[0,1,1,0,0,0,0],[0,1,0,0,1,0,0]]
print(BFS(matrix))