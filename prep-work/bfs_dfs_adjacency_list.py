'''
Time complexity: 
Space complexity:
'''

from collections import defaultdict

class GraphTraversals():
    def __init__(self):
        self.graph = defaultdict(list)

    def print_graph(self):
        return self.graph

    def insert(self, v1, v2):
        if(v2 not in self.graph[v1]):
            self.graph[v1].append(v2)

class BFS(GraphTraversals):
    def __init__(self):
        super().__init__()

    def bfs_traversal(self):
        queue = []
        visited = []
        
        queue.append(min(self.graph.keys()))
        while(len(queue)>0):
            for vertex in self.graph[queue[0]]:
                if((vertex not in queue) and (vertex not in visited)):
                    queue.append(vertex)
            
            visited.append(queue.pop(0))

        return visited

class DFS(GraphTraversals):
    def __init__(self):
        super().__init__()

    def dfs_(self):
        current = min(self.graph.keys())
        visited = [current]
        return self.dfs_traversal(visited, current)

    def visited_equals_graph(self, visited):
        if(len(visited)!=len(self.graph)):
            return visited

    def dfs_traversal(self, visited, current):
        if(len(visited)<len(self.graph.keys())):
            for i in self.graph[current]:
                if(i not in visited):
                    visited.append(i)
                    visited = self.dfs_traversal(visited, i)
        return visited



bfs = BFS()
bfs.insert(1, 2)
bfs.insert(1,4)

bfs.insert(2,6)
bfs.insert(2,3)

bfs.insert(3, 2)
bfs.insert(3, 4)

bfs.insert(4, 1)
bfs.insert(4, 3)
bfs.insert(4, 5)

bfs.insert(5, 4)

bfs.insert(6, 2)
bfs.insert(6, 1)

print('BFS: ',bfs.bfs_traversal())

dfs = DFS()

dfs.insert(1, 2)
dfs.insert(1,4)

dfs.insert(2,6)
dfs.insert(2,3)

dfs.insert(3, 2)
dfs.insert(3, 4)

dfs.insert(4, 1)
dfs.insert(4, 3)
dfs.insert(4, 5)

dfs.insert(5, 4)

dfs.insert(6, 2)
dfs.insert(6, 1)

print('DFS: ',dfs.dfs_())