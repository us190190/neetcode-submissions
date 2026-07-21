class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        indegree = {c:0 for word in words for c in word}
        adj = {c:set() for c in indegree}
        edges = set()

        for i in range(1,len(words)):
            w1, w2 = words[i-1], words[i]
            min_len = min(len(w1), len(w2))
            if len(w1)>len(w2) and w1[:min_len]==w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] == w2[j]:
                    continue
                edges.add((w1[j], w2[j]))
                break
        
        for src, dst in edges:
            adj[src].add(dst)
            indegree[dst] += 1
        
        q = deque()
        for c,v in indegree.items():
            if v==0:
                q.append(c)
        
        visied = set()
        result = []
        while q:
            node = q.popleft()
            result.append(node)
            for nbr in adj[node]:
                indegree[nbr] -= 1
                if indegree[nbr]==0:
                    q.append(nbr)
        
        return "".join(result) if len(result)==len(indegree) else ""



        