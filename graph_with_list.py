class graph:
    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.adj_dict = {v: [] for v in range(vertex_count)}
    
    def add_edge(self, u, v, weight=1):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_dict[u].append((v, weight))
            self.adj_dict[v].append((u, weight))  # Ensures the edge is bidirectional
        else:
            print("Invalid vertices")
    
    def remove_edge(self, u, v):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_dict[u] = [(vertex, weight) for vertex, weight in self.adj_dict[u] if vertex != v]
            self.adj_dict[v] = [(vertex, weight) for vertex, weight in self.adj_dict[v] if vertex != u]
        else:
            print("Invalid vertices")
    
    def has_edge(self, u, v):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            return any(vertex == v for vertex, _ in self.adj_dict[u])
        else:
            print("Invalid vertices")
            return False
    
    def print_adj_dict(self):
        for vertex, neighbors in self.adj_dict.items():
            print(f"{vertex}: {neighbors}")

# Testing the graph class

# Create a graph with 4 vertices
g = graph(4)

# Add edges
g.add_edge(0, 1, 2)  # Add an edge between vertex 0 and 1 with weight 2
g.add_edge(1, 2, 3)  # Add an edge between vertex 1 and 2 with weight 3
g.add_edge(2, 3, 4)  # Add an edge between vertex 2 and 3 with weight 4
g.add_edge(3, 0, 5)  # Add an edge between vertex 3 and 0 with weight 5

# Remove an edge
g.remove_edge(1, 2)  # Remove the edge between vertex 1 and 2

# Check if edges exist
print("Edge between 0 and 1:", g.has_edge(0, 1))  # Should return True
print("Edge between 1 and 2:", g.has_edge(1, 2))  # Should return False after removing the edge

# Print the adjacency list
print("Adjacency List:")
g.print_adj_dict()
