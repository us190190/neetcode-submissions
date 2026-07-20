class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        adj = {c:[] for word in words for c in word}
        indegree = {c:0 for c in adj}
        edges = set()

        for i in range(1,len(words)):
            w1, w2 = words[i-1], words[i]
            min_len = min(len(w1), len(w2))
            if len(w1)>len(w2) and w1[:min_len]==w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j]!=w2[j]:
                    edges.add((w1[j], w2[j]))
                    break

        for u,v in edges:
            adj[u].append(v)
            indegree[v] += 1
        
        q = deque()
        for src,count in indegree.items():
            if count==0:
                q.append(src)
        
        result = []
        while q:
            node = q.popleft()
            result.append(node)
            for dst in adj[node]:
                indegree[dst] -= 1
                if indegree[dst]==0:
                    q.append(dst)
        
        if len(result)!=len(indegree):
            return ""
        
        return "".join(result)

            


        

            

        