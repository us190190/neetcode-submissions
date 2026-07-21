class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        indegree = [0 for _ in range(numCourses)]
        adj = [[] for _ in range(numCourses)]

        for dst, src in prerequisites:
            adj[src].append(dst)
            indegree[dst] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        
        visited = set()
        while q:
            node = q.popleft()
            if node in visited:
                return False
            visited.add(node)
            for nbr in adj[node]:
                if nbr in visited:
                    return False
                indegree[nbr] -= 1
                if indegree[nbr]==0:
                    q.append(nbr)
        
        return len(visited) == numCourses


        