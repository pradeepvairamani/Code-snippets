def bfs(graph, start, path=[]):
    '''use double ended queue from collections'''
    from collections import deque
    visited = set()
    q = deque([start])
    while q:
        new_root = q.popleft()
        if new_root in visited:
            continue
        path = path + [new_root]
        for node in graph[new_root]:
            q.append(node)
            visited.add(new_root)
    return path


def dfs(graph, start, path=[]):
    '''recursive depth first search from start node'''
    path = path + [start]
    for node in graph[start]:
        if node not in path:
            path = dfs(graph, node, path)
    return path


graph = {'A': ['B', 'C'], 'B': ['D', 'E'],
         'C': ['D', 'E'], 'D': ['E'], 'E': ['A']}
print 'recursive dfs ', dfs(graph, 'A')
print bfs(graph, 'A')
