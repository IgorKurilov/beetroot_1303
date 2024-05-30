from collections import deque, defaultdict

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

    def bfs_shortest_path(self, start):
        """Find the shortest path from start vertex to all other vertices using BFS."""
        distances = {vertex: float('inf') for vertex in self.vertexes}
        distances[start] = 0
        queue = deque([start])

        while queue:
            current = queue.popleft()
            for neighbor in self.vertexes[current]:
                if distances[neighbor] == float('inf'):
                    distances[neighbor] = distances[current] + 1
                    queue.append(neighbor)

        return distances

    def all_pairs_shortest_path(self):
        """Compute the shortest path between all pairs of vertices using BFS."""
        all_pairs = {}
        for vertex in self.vertexes:
            all_pairs[vertex] = self.bfs_shortest_path(vertex)
        return all_pairs

if __name__ == "__main__":
    graph = Graph()
    graph.add_edge("a", "b")
    graph.add_edge("a", "c")
    graph.add_edge("b", "d")
    graph.add_edge("c", "d")
    graph.add_edge("d", "e")
    graph.add_edge("e", "f")
    graph.add_edge("f", "g")

    graph.print_vertexes()

    all_pairs_distances = graph.all_pairs_shortest_path()
    print("\nAll Pairs Shortest Path Distances:")
    for start_vertex, distances in all_pairs_distances.items():
        print(f"{start_vertex}: {distances}")
