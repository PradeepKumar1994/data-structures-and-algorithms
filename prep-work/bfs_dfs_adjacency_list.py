'''
Time complexity: O(N)
Space complexity: O(N)
'''

class Graph():
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list
        self.vertices = self.determine_vertices()

    def determine_vertices(self):
        vertices = len(adjacency_list)
        return vertices

    def dfs(self):
        visited = [0]
        visited = self._dfs(visited, visited[0])
        return visited

    def add_visited(self, visited, i):
        visited.append(i)
        return visited

    def _dfs(self, visited, current_vertices):
        if(len(visited) < self.vertices):
            for i in self.adjacency_list[current_vertices]:
                if(i not in visited):
                    self.add_visited(visited, i)
                    visited = self._dfs(visited, i)
        return visited

    def bfs(self):
        current_vertex = 0
        visited, queue = [], [current_vertex]
        while(len(visited)<self.vertices):
            for i in self.adjacency_list[current_vertex]:
                if(i not in queue and i not in visited):
                    queue.append(i)
            visited.append(queue.pop(0))
            if(len(queue)>0):
                current_vertex = queue[0]
            else:
                return visited
        return visited

adjacency_list = [[1,2],[0,2,4],[0,1,3],[2],[1]]

graph = Graph(adjacency_list)
print(graph.dfs())
print(graph.bfs())