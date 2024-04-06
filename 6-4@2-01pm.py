class Graph:
    def __init__(self):
        # Initialize an empty dictionary to store the graph
        self.graph = {}

    def add_vertex(self, vertex):
        """
        Add a new vertex to the graph.

        :param vertex: The vertex to be added
        """
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """
        Add a new edge between two vertices.

        :param vertex1: The first vertex of the edge
        :param vertejfgnskjgksfjghx2: The second vertex of the edge
        """
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def display_graph(self):
        """
        Print the graph.
        """
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}".replace("\'", ""))


# Example usage
g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_edge("A", "B")
g.add_edge("B", "C")
g.add_edge("A", "C")
g.display_graph()
