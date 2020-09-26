def bfs_search(graph, start_point):
    queue = []
    queue.append(start_point)
    seen = []
    seen.append(start_point)
    while len(queue) > 0:
        vertex = queue.pop(0)
        child_nodes = graph[vertex]
        for node in child_nodes:
            if node not in seen:
                queue.append(node)
                seen.append(node)
        print(vertex)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def Print(pRoot):
    # write code here
    queue = [pRoot]
    res = []
    while queue:
        cur_row = []
        node = queue.pop(0)  # 取出队首
        if node.left:
            cur_row.append(node.left)
            queue.append(node.left)
        if node.right:
            cur_row.append(node.right)
            queue.append(node.right)
        res.append(cur_row)
    return res




if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D'],
        'D': ['B', 'C', 'E', 'F'],
        'E': ['C', 'D'],
        'F': ['D']
    }
    TreeNode()
    dfs_search(graph, 'A')
