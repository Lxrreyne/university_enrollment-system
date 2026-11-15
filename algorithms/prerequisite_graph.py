# This file builds a graph showing which course needs which course first.

def build_prerequisite_graph(courses_dict):
    graph = {}

    for course_code in courses_dict:
        graph[course_code] = []

    for course_code, info in courses_dict.items():
        for prereq in info["prerequisites"]:
            if prereq in graph:
                graph[prereq].append(course_code)

    return graph