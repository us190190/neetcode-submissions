class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        tickets.sort(reverse=True)
        adj = defaultdict(list)

        for u,v in tickets:
            adj[u].append(v)
        
        result = []
        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            result.append(src)

        dfs("JFK")
        return result[::-1]


        