
import queue
class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, veretx):
        self.vertices[veretx] = []

    def add_edge(self, source, target):
        self.vertices[source].append(target)

    def BFS(self,current):
        visited_vertices=list()
        bfs_queue = queue.SimpleQueue()
        bfs_queue.put(current)
        visited_vertices.append(current)
        while not bfs_queue.empty():
            val=bfs_queue.get()
            for adj in self.vertices[val]:
                if adj not in visited_vertices:
                    visited_vertices.append(adj)
                    bfs_queue.put(adj)
        return visited_vertices

    def DFS(self,visited_vertices,current):
        if current not in visited_vertices:
            print(current,end=" ")
            visited_vertices.append(current)
            for adj in self.vertices[current]:
                self.DFS(visited_vertices,adj)


graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('2')


graph.add_edge('0', '1')
graph.add_edge('0', '2')
graph.add_edge('1', '2')
graph.add_edge('1', '3')
graph.add_edge('3', '4')
graph.add_edge('2', '4')



print(graph.BFS('0'))
graph.DFS([],'0')

