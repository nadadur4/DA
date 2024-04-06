class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def remove_vertex(self, vertex):
        """
        Remove a vertex from the graph.

        :param vertex: The vertex to be removed
        """
        if vertex in self.graph:
            del self.graph[vertex]
            for v in self.graph:
                if vertex in self.graph[v]:
                    self.graph[v].remove(vertex)

    def remove_edge(self, vertex1, vertex2):
        """
        Remove an edge between two vertices.

        :param vertex1: The first vertex of the edge
        :param vertex2: The second vertex of the edge
        """
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex2 in self.graph[vertex1]:
                self.graph[vertex1].remove(vertex2)
            if vertex1 in self.graph[vertex2]:
                self.graph[vertex2].remove(vertex1)

    def get_friends(self, vertex):
        """
        Get the friends (adjacent nodes) of a vertex.

        :param vertex: The vertex to get friends for
        :return: A list of friends
        """
        if vertex in self.graph:
            return self.graph[vertex]
        else:
            return []

    def display_graph(self):
        """
        Print the graph.
        """
        for vertex in self.graph:
            print(vertex, "->", ', '.join(self.graph[vertex]))


# Example usage
g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_edge("A", "B")
g.add_edge("B", "C")
g.add_edge("A", "C")
g.display_graph()
print(g.get_friends("A"))
g.remove_edge("A", "B")
g.display_graph()
g.remove_vertex("B")
g.display_graph()
