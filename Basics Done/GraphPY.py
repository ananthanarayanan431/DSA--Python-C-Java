class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, veretx):
        self.vertices[veretx] = []

    def add_edge(self, source, target):
        self.vertices[source].append(target)


graph = Graph()
graph.add_vertex('Anantha')
graph.add_vertex('Narayanan')
graph.add_vertex('Anand')

graph.add_edge('Anantha', 'Narayanan')
graph.add_edge('Anantha', 'Anand')
graph.add_edge('Anand', 'Narayanan')
