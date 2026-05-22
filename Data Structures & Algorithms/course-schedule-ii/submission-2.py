class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        req = {course:[] for course in range(numCourses)}

        for edge_s, edge_e in prerequisites:
            req[edge_s].append(edge_e)
        
        order, visited = [], set()

        def validate_node(course):
            if course in visited:
                return False
            if course in order:
                return True
            
            visited.add(course)
            for p in req[course]:
                if not validate_node(p):
                    return False
            visited.remove(course)
            order.append(course)
            # print(f"course:{course}, order:{order}")
            return True
        
        for course in range(numCourses):
            if not validate_node(course):
                return []
        
        return order
            
        