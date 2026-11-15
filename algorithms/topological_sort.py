# This file arranges courses in a valid order - lahat ng prerequisite.

def topological_sort(graph):
    visited = [] 
    result = []

    def visit(course):
        if course in visited:
            return
        visited.append(course)
        
        for neighbor in graph.get(course, []):
            visit(neighbor)
        
        result.insert(0, course)

    for course in graph:
        visit(course)

    return result