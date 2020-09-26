def bfs_search(graph, start_point):
    queue = []
    queue.append(start_point)
    seen = []
    seen.add(start_point)
    while len(queue) > 0:
        vertex = queue.pop(0)
        child_nodes = graph[vertex]
        for node in child_nodes:
            if node not in seen:
                queue.append(node)
                seen.add(node)
        print(vertex)


if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D'],
        'D': ['B', 'C', 'E', 'F'],
        'E': ['C', 'D'],
        'F': ['D']
    }
    bfs_search(graph, 'A')
