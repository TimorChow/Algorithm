def dfs_search(graph, start_point):
    stack = []
    stack .append(start_point)
    seen = set()  # save the point that we have already push into the stack
    seen.add(start_point)
    while len(stack) > 0:
        vertex = stack.pop(-1)
        child_nodes = graph[vertex]
        for node in child_nodes:
            if node not in seen:
                stack.append(node)
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
    dfs_search(graph, 'D')
