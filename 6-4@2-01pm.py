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

    def delete_vertex(self, vertex):
        """
        Delete a vertex from the graph.

        :param vertex: The vertex to be deleted
        """
        if vertex in self.graph:
            del self.graph[vertex]
            for adjacent_vertices in self.graph.values():
                if vertex in adjacent_vertices:
                    adjacent_vertices.remove(vertex)

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

    def display_graph(self):
        for vertex in self.graph:
            print(vertex, "->", ', '.join(self.graph[vertex]))

    def show_friends(self, vertex):
        """
        Show the friends (adjacent nodes) of a vertex.

        :param vertex: The vertex whose friends you want to show
        """
        if vertex in self.graph:
            print("Friends of", vertex, ":", ', '.join(self.graph[vertex]))


# Example usage
g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_edge("A", "B")
g.add_edge("B", "C")
g.add_edge("A", "C")
g.display_graph()
g.show_friends("A")
g.remove_edge("A", "B")
g.display_graph()
g.delete_vertex("C")
g.display_graph()
