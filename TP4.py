import numpy as np
import heapq

num_nodes = 9

adj_matrix = [[float('inf')] * num_nodes for _ in range(num_nodes)]

edges = [
    (1, 2, 4), (1, 5, 1), (1, 7, 2),
    (2, 3, 7), (2, 6, 5),
    (3, 4, 1), (3, 6, 8),
    (4, 6, 6), (4, 7, 4), (4, 8, 3),
    (5, 6, 9), (5, 7, 10),
    (6, 9, 2),
    (7, 9, 8),
    (8, 9, 1),
    (9, 8, 7)
]

for u, v, w in edges:
    adj_matrix[u - 1][v - 1] = w
    adj_matrix[v - 1][u - 1] = w


adj_matrix_np = np.array(adj_matrix)

def format_value(x):
    return ' inf' if x == float('inf') else f'{int(x):4d}'

formatted_matrix = np.array2string(
    adj_matrix_np,
    formatter={'all': format_value},
    separator=' ',
    max_line_width=120
)

print("Adjacency Matrix for Undirected and Weighted graph:")
print(formatted_matrix)

def prim_algorithm(adj_matrix, root):
    n = len(adj_matrix)
    visited = [False] * n
    min_heap = [(0, root, -1)]  # (weight, current_node, parent_node)
    mst_edges = []
    total_weight = 0

    while min_heap:
        weight, node, parent = heapq.heappop(min_heap)
        if visited[node]:
            continue
        visited[node] = True
        total_weight += weight

        if parent != -1:
            mst_edges.append((parent + 1, node + 1, weight))

        for neighbor in range(n):
            if not visited[neighbor] and adj_matrix[node][neighbor] != float('inf'):
                heapq.heappush(min_heap, (adj_matrix[node][neighbor], neighbor, node))

    return mst_edges, total_weight

def kruskal_algorithm(adj_matrix):
    n = len(adj_matrix)
    edges = [
        (adj_matrix[i][j], i, j)
        for i in range(n)
        for j in range(i + 1, n)
        if adj_matrix[i][j] != float('inf')
    ]
    edges.sort()

    parent = list(range(n))
    rank = [0] * n
    mst_edges = []
    total_weight = 0

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1

    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst_edges.append((u + 1, v + 1, weight))
            total_weight += weight

    return mst_edges, total_weight

root_node = int(input("\nEnter the root node for Prim's algorithm: ")) - 1

prim_edges, prim_weight = prim_algorithm(adj_matrix, root_node)
kruskal_edges, kruskal_weight = kruskal_algorithm(adj_matrix)

print("\nPrim's Algorithm MST:")
for edge in prim_edges:
    print(f"Edge: {edge[0]} - {edge[1]}, Weight: {edge[2]}")
print(f"Total weight of MST: {prim_weight}")

print("\nKruskal's Algorithm MST:")
for edge in kruskal_edges:
    print(f"Edge: {edge[0]} - {edge[1]}, Weight: {edge[2]}")
print(f"Total weight of MST: {kruskal_weight}")
