class Graph:
    def __init__(self):
        self.vertexes = {}

    def add_vertex(self, name):
        if name in self.vertexes:
            return
        self.vertexes.update({name: set()})

    def add_edge(self, from_name, to_name):
        self.add_vertex(from_name)
        self.add_vertex(to_name)
        self.vertexes[from_name].add(to_name)
        self.vertexes[to_name].add(from_name)

    def print_vertexes(self):
        for vertex, neighbors in self.vertexes.items():
            print(f"{vertex}: {neighbors}")

    def find_loops(self):
        """Find all loops (self-loops) in the graph. A loop is an edge that starts and ends at the same vertex."""
        loops = []
        for vertex, neighbors in self.vertexes.items():
            if vertex in neighbors:
                loops.append(vertex)
        return loops

    def find_isolated(self):
        """Find all isolated vertices in the graph. An isolated vertex is one that has no connections (degree 0)."""
        isolated = [vertex for vertex, neighbors in self.vertexes.items() if not neighbors]
        return isolated


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge("a", "a")
    graph.add_edge("a", "b")
    graph.add_edge("b", "a")
    graph.add_edge("b", "d")
    graph.add_edge("b", "e")
    graph.add_vertex("c")
    graph.add_edge("d", "b")
    graph.add_edge("d", "e")
    graph.add_edge("e", "b")
    graph.add_edge("e", "d")
    graph.print_vertexes()

    loops = graph.find_loops()
    isolated = graph.find_isolated()

    print("\nLoops (self-loops) in the graph:", loops)
    print("Isolated vertices in the graph:", isolated)
