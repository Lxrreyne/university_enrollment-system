ALGORITHMS PSEUDOCODE

======================================================================
BREADTH-FIRST SEARCH (bfs.py)
======================================================================
 
BFS
    START
    INPUT graph, starting course
    CREATE a visited list containing the starting course
    PUT the starting course in the waiting line
    WHILE the waiting line is not empty
        TAKE the first course out of the waiting line
        FOR each next course of this course (none if it has no entry)
            IF the next course has not been visited THEN
                ADD it to the visited list
                PUT it at the end of the waiting line
            END IF
        END FOR
    END WHILE
    RETURN the visited list
    END
 
BFS LEVELS
    START
    INPUT graph, starting course
    SET the starting course's level to 0
    PUT the starting course in the waiting line
    WHILE the waiting line is not empty
        TAKE the first course out of the waiting line
        FOR each next course of this course (none if it has no entry)
            IF the next course has no level yet THEN
                SET its level to the current course's level plus 1
                PUT it at the end of the waiting line
            END IF
        END FOR
    END WHILE
    RETURN the level of every reachable course
    END
    
======================================================================
SEARCHING (searching.py)
======================================================================
 
LINEAR SEARCH BY NAME
    START
    INPUT list of records, name to find
    FOR each record in the list
        IF the record's name matches the name to find (ignore upper/lower case) THEN
            RETURN that record
        END IF
    END FOR
    RETURN nothing (not found)
    END
 
LINEAR SEARCH BY ID
    START
    INPUT records stored by ID, ID to find
    LOOK UP the ID in the records
    RETURN the record if found, otherwise RETURN nothing
    END
 
SEARCH COURSES BY KEYWORD
    START
    INPUT courses stored by course code, keyword
    CREATE an empty list of results
    FOR each course code and its course information
        IF the keyword appears in the course name (ignore upper/lower case) THEN
            ADD the course code and its information to the results
        END IF
    END FOR
    RETURN the results
    END
 
======================================================================
SORTING (sorting.py) - own bubble sort, no built-in sort
======================================================================
 
BUBBLE SORT BY NAME
    START
    INPUT list of records
    MAKE a copy of the list
    COUNT how many records are in the copy
    REPEAT once for each record
        FOR each pair of neighboring records up to the part not yet sorted
            IF the first name comes after the second name alphabetically
               (ignore upper/lower case) THEN
                SWAP the two records
            END IF
        END FOR
    END REPEAT
    RETURN the sorted copy
    END
 
BUBBLE SORT COURSES BY CAPACITY
    START
    INPUT list of courses (each course is a code with its information)
    MAKE a copy of the list
    COUNT how many courses are in the copy
    REPEAT once for each course
        FOR each pair of neighboring courses up to the part not yet sorted
            IF the first course's capacity is greater than the second's THEN
                SWAP the two courses
            END IF
        END FOR
    END REPEAT
    RETURN the sorted copy
    END
 
======================================================================
PREREQUISITE GRAPH (prerequisite_graph.py)
======================================================================
 
BUILD PREREQUISITE GRAPH
    START
    INPUT courses stored by course code
    CREATE an empty graph
    FOR each course code
        ADD the course code to the graph with an empty list of next courses
    END FOR
    FOR each course code and its course information
        FOR each prerequisite listed in the course information
            IF the prerequisite exists in the graph THEN
                ADD this course code to the prerequisite's list of next courses
            END IF
        END FOR
    END FOR
    RETURN the graph
    END

======================================================================
DEPTH-FIRST SEARCH (dfs.py)
======================================================================
 
DFS
    START
    INPUT graph, starting course
    CREATE an empty list of visited courses
    PUT the starting course on the stack
    WHILE the stack is not empty
        TAKE the top course off the stack
        IF the course has not been visited THEN
            ADD it to the visited list
            FOR each next course of this course
                IF the next course has not been visited THEN
                    PUT it on the stack
                END IF
            END FOR
        END IF
    END WHILE
    RETURN the visited list
    END

======================================================================
TOPOLOGICAL SORT (topological_sort.py) - depth-first version
======================================================================
 
TOPOLOGICAL SORT
    START
    INPUT graph
    CREATE an empty visited list
    CREATE an empty result list
    FOR each course in the graph
        VISIT the course
    END FOR
    RETURN the result list
    END
 
VISIT a course
    IF the course is already visited THEN
        STOP
    END IF
    ADD the course to the visited list
    FOR each next course of this course (none if it has no entry)
        VISIT the next course
    END FOR
    PLACE the course at the FRONT of the result list
    END
