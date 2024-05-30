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

    def _dfs(self, vertex, visited, stack):
        """Helper function for depth-first search."""
        visited.add(vertex)
        for neighbor in self.vertexes[vertex]:
            if neighbor not in visited:
                self._dfs(neighbor, visited, stack)
        stack.append(vertex)

    def _transpose(self):
        """Transpose the graph (reverse all edges)."""
        transposed = Graph()
        for vertex in self.vertexes:
            transposed.add_vertex(vertex)
        for vertex, neighbors in self.vertexes.items():
            for neighbor in neighbors:
                transposed.add_edge(neighbor, vertex)
        return transposed

    def _dfs_collect(self, vertex, visited, component):
        """Helper function for depth-first search to collect components."""
        visited.add(vertex)
        component.append(vertex)
        for neighbor in self.vertexes[vertex]:
            if neighbor not in visited:
                self._dfs_collect(neighbor, visited, component)

    def find_sccs(self):
        """Find strongly connected components using Kosaraju's algorithm."""
        stack = []
        visited = set()

        # Step 1: Perform DFS on the original graph and store vertices in stack by finish time
        for vertex in self.vertexes:
            if vertex not in visited:
                self._dfs(vertex, visited, stack)

        # Step 2: Transpose the graph
        transposed = self._transpose()

        # Step 3: Perform DFS on the transposed graph in the order of decreasing finish time
        visited.clear()
        sccs = []
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                component = []
                transposed._dfs_collect(vertex, visited, component)
                sccs.append(component)

        return sccs


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge("a", "b")
    graph.add_edge("b", "c")
    graph.add_edge("c", "a")
    graph.add_edge("b", "d")
    graph.add_edge("d", "e")
    graph.add_edge("e", "f")
    graph.add_edge("f", "d")
    graph.add_edge("g", "f")
    graph.add_edge("g", "h")
    graph.add_edge("h", "i")
    graph.add_edge("i", "g")
    graph.add_edge("i", "c")

    graph.print_vertexes()

    sccs = graph.find_sccs()
    print("\nStrongly Connected Components:", sccs)
