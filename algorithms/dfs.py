# This file explores the graph deeply first (Depth-First Search).

def dfs(graph, start_course):
    visited = [] 
    stack = [start_course]

    while stack:
        current = stack.pop() 
        if current not in visited:
            visited.append(current)
            
            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    stack.append(neighbor)

    return visited