class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        q = deque()
        finish = 0

        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)
        
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        
        while q:
            src = q.popleft()
            finish += 1
            for nbr in adj[src]:
                indegree[nbr] -= 1
                if indegree[nbr]==0:
                    q.append(nbr)
        
        return finish==numCourses


        