class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        ref = {course:[] for course in range(numCourses)}
        visited = set()

        for prereq in prerequisites:
            ref[prereq[0]].append(prereq[1])

        def validate_node(course):
            if course in visited:
                return False
            if len(ref[course])==0:
                return True
            
            visited.add(course)
            for idx in range(len(ref[course])):
                req = ref[course][idx]
                if not validate_node(req):
                    return False
            
            visited.remove(course)
            return True

        for course in range(numCourses):
            if not validate_node(course):
                return False
        
        return True
            

        

        