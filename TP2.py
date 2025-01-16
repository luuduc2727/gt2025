def find_components(graph, is_directed=True):
    def dfs(node, visited, component, graph):
        stack = [node]
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                component.add(current + 1)  # +1 to match 1-based indexing in output
                for neighbor in range(len(graph[current])):
                    if graph[current][neighbor] == 1 and neighbor not in visited:
                        stack.append(neighbor)

    def create_undirected_graph(directed_graph):
        size = len(directed_graph)
        undirected_graph = [[0] * size for _ in range(size)]
        for i in range(size):
            for j in range(size):
                if directed_graph[i][j] == 1 or directed_graph[j][i] == 1:
                    undirected_graph[i][j] = 1
                    undirected_graph[j][i] = 1
        return undirected_graph

    visited = set()
    components = []

    # Perform DFS to find components
    for node in range(len(graph)):
        if node not in visited:
            component = set()
            dfs(node, visited, component, graph)
            components.append(component)

    if is_directed:
        # Create undirected graph for weakly connected components
        undirected_graph = create_undirected_graph(graph)
        weak_components = find_components(undirected_graph, is_directed=False)
        return components, weak_components
    else:
        return components


if __name__ == "__main__":
    directed_graph = [
        [0, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 1],
        [0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 1, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    strong_components, weak_components = find_components(directed_graph)


    print("Strongly Connected Components (Strong):", strong_components)
    print("Weakly Connected Components (Weak):", weak_components)
