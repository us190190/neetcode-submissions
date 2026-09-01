class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        tickets.sort(reverse=True)
        adj = {}

        for src, dst in tickets:
            if src not in adj:
                adj[src] = []
            adj[src].append(dst)

        self.result = []

        def dfs(src):

            while src in adj and adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            
            self.result.append(src)
        
        dfs("JFK")

        return self.result[::-1]
            
        