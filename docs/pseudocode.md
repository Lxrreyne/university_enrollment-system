**ALGORITHMS PSEUDOCODE**

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




**DATA STRUCTURES PSEUDOCODE**
 
======================================================================
COURSE DICTIONARY (stores all course records)
======================================================================
 
CREATE COURSE DICTIONARY
    START
    CREATE an empty collection of courses, stored by course code
    END
 
ADD COURSE
    START
    INPUT course code, name, capacity, prerequisites (optional)
    IF the course code already exists THEN
        RETURN false
    END IF
    IF no prerequisites were given THEN
        SET prerequisites to empty
    END IF
    SAVE the course under its course code with:
        the name
        the capacity
        an empty set of enrolled students
        the set of prerequisites
    RETURN true
    END
 
GET COURSE
    START
    INPUT course code
    RETURN the course record, or nothing if the code does not exist
    END
 
COURSE EXISTS
    START
    INPUT course code
    RETURN true if the code is in the collection, otherwise false
    END
 
HAS SLOT
    START
    INPUT course code
    FIND the course
    IF the course does not exist THEN
        RETURN false
    END IF
    RETURN true if the number of enrolled students is less than the capacity,
        otherwise false
    END
 
ENROLL STUDENT
    START
    INPUT course code, student ID
    FIND the course
    IF the course does not exist THEN
        RETURN false
    END IF
    IF the course has no free slot THEN
        RETURN false
    END IF
    ADD the student ID to the course's enrolled students
    RETURN true
    END
 
DROP STUDENT
    START
    INPUT course code, student ID
    FIND the course
    IF the course does not exist THEN
        RETURN false
    END IF
    REMOVE the student ID from the course's enrolled students
        (no error if the student was not enrolled)
    RETURN true
    END
 
MEETS PREREQUISITES
    START
    INPUT course code, student's completed courses
    FIND the course
    IF the course does not exist THEN
        RETURN false
    END IF
    FOR each prerequisite of the course
        IF the prerequisite is not in the completed courses THEN
            RETURN false
        END IF
    END FOR
    RETURN true
    END
 
GET ALL COURSES
    START
    RETURN every course record
    END
 
======================================================================
ENROLLMENT LIST (log of all enrollment transactions)
======================================================================
 
CREATE ENROLLMENT LIST
    START
    CREATE an empty list of records
    END
 
ADD RECORD
    START
    INPUT student ID, course code, timestamp (optional)
    CREATE a record containing the student ID, course code and timestamp
    ADD the record to the end of the list
    RETURN the record
    END
 
GET ALL RECORDS
    START
    RETURN the whole list of records
    END
 
FILTER BY STUDENT
    START
    INPUT student ID
    CREATE an empty list of results
    FOR each record in the list
        IF the record's student ID matches THEN
            ADD the record to the results
        END IF
    END FOR
    RETURN the results
    END
 
FILTER BY COURSE
    START
    INPUT course code
    CREATE an empty list of results
    FOR each record in the list
        IF the record's course code matches THEN
            ADD the record to the results
        END IF
    END FOR
    RETURN the results
    END
 
======================================================================
ENROLLMENT SET (prevents duplicate enrollment)
======================================================================
 
CREATE ENROLLMENT SET
    START
    CREATE an empty set of (student ID, course code) pairs
    END
 
IS DUPLICATE
    START
    INPUT student ID, course code
    RETURN true if the pair is already in the set, otherwise false
    END
 
ADD ENROLLMENT
    START
    INPUT student ID, course code
    IF the pair is already in the set THEN
        RETURN false
    END IF
    ADD the pair to the set
    RETURN true
    END
 
REMOVE ENROLLMENT
    START
    INPUT student ID, course code
    IF the pair is in the set THEN
        REMOVE the pair from the set
        RETURN true
    END IF
    RETURN false
    END
 
GET COURSES OF STUDENT
    START
    INPUT student ID
    CREATE an empty set of course codes
    FOR each pair in the set
        IF the pair's student ID matches THEN
            ADD the pair's course code to the results
        END IF
    END FOR
    RETURN the results
    END
 
GET STUDENTS OF COURSE
    START
    INPUT course code
    CREATE an empty set of student IDs
    FOR each pair in the set
        IF the pair's course code matches THEN
            ADD the pair's student ID to the results
        END IF
    END FOR
    RETURN the results
    END
 
======================================================================
STUDENT DICTIONARY (stores all student records)
======================================================================
 
CREATE STUDENT DICTIONARY
    START
    CREATE an empty collection of students, stored by student ID
    END
 
ADD STUDENT
    START
    INPUT student ID, name
    IF the student ID already exists THEN
        RETURN false
    END IF
    SAVE the student under their ID with:
        the name
        an empty set of completed courses
    RETURN true
    END
 
GET STUDENT
    START
    INPUT student ID
    RETURN the student record, or nothing if the ID does not exist
    END
 
STUDENT EXISTS
    START
    INPUT student ID
    RETURN true if the ID is in the collection, otherwise false
    END
 
ADD COMPLETED COURSE
    START
    INPUT student ID, course code
    FIND the student
    IF the student does not exist THEN
        RETURN false
    END IF
    ADD the course code to the student's completed courses
    RETURN true
    END
 
HAS COMPLETED
    START
    INPUT student ID, course code
    FIND the student
    IF the student does not exist THEN
        RETURN false
    END IF
    RETURN true if the course code is in the student's completed courses,
        otherwise false
    END
 
DELETE STUDENT
    START
    INPUT student ID
    IF the student ID exists THEN
        REMOVE the student record
        RETURN true
    END IF
    RETURN false
    END
 
GET ALL STUDENTS
    START
    RETURN every student record
    END
