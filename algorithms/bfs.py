# This file explores the graph level by level (Breadth-First Search).

def bfs(graph, start_course):
    visited = [start_course]  
    queue = [start_course]

    while queue:
        current = queue.pop(0)  
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

    return visited

def bfs_levels(graph, start_course):
    levels = {start_course: 0}
    queue = [start_course]

    while queue:
        current = queue.pop(0)
        for neighbor in graph.get(current, []):
            if neighbor not in levels:
                levels[neighbor] = levels[current] + 1
                queue.append(neighbor)

    return levels