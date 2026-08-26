class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        tickets.sort(reverse=True)
        
        adj = {}

        for u,v in tickets:
            if u not in adj:
                adj[u] = []
            adj[u].append(v)
        
        result = []

        def dfs(src):
            while src in adj and adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            result.append(src)
        
        dfs("JFK")

        return result[::-1]
        