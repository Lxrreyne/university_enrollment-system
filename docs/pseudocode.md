ALGORITHMS PSEUDOCODE
 
Assumptions: students and courses are lists of records
(student.id, student.name, course.code, course.name, course.capacity,
course.prerequisites). The prerequisite graph is an adjacency list.

================================
MODULE: algorithms/bfs.py
================================

BFS
    START
    INPUT graph, starting course
    MARK the starting course as visited
    PUT the starting course in the waiting line
    WHILE the waiting line is not empty
        TAKE the first course out of the waiting line
        FOR each course that depends on it
            IF that course has not been visited THEN
                MARK it as visited
                PUT it at the end of the waiting line
            END IF
        END FOR
    END WHILE
    RETURN the visited courses in order
    END
 
BFS LEVELS
    START
    INPUT graph, starting course
    SET the starting course's level to 0
    PUT the starting course in the waiting line
    WHILE the waiting line is not empty
        TAKE the first course out of the waiting line
        FOR each course that depends on it
            IF that course has no level yet THEN
                SET its level to the current course's level plus 1
                PUT it at the end of the waiting line
            END IF
        END FOR
    END WHILE
    RETURN the level of every reachable course
    END
