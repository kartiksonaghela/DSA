class graph:
    def __init__(self,vertex_count):
        self.vertex_count=vertex_count
        self.adj_matrix=[[0]*vertex_count for e in range(vertex_count)]
    def add_edge(self,u,v,weight=1):
        if 0<=u< self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v]=weight
            self.adj_matrix[v][u]=weight
        else:
            print("Invalid Vertex")
    def remove_edge(self,u,v):
        if 0<=u< self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v]=0
            self.adj_matrix[v][u]=0
        else:
            print("Invalid Vertex")
    def has_edge(self,u,v):
        if 0<=u< self.vertex_count and 0<=v<self.vertex_count:
            return self.adj_matrix[u][v]!=0
        else:
            print("Invalid Vertex")
    def printadj_matrix(self):
        for row in self.adj_matrix:
            print(' '.join(map(str,row)))
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

# Print the adjacency matrix
print("Adjacency Matrix:")
g.printadj_matrix()