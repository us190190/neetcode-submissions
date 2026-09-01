class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        indegree = {c:0 for word in words for c in word}
        adj = {c:set() for c in indegree.keys()}
        edges = set()

        for i in range(1, len(words)):
            w1, w2 = words[i-1], words[i]
            intersecting_word_len = min(len(w1), len(w2))
            if len(w1)>len(w2) and w1[:intersecting_word_len]==w2:
                return ""
            for j in range(intersecting_word_len):
                if w1[j]==w2[j]:
                    continue
                edges.add((w1[j], w2[j]))
                break

        for u,v in edges:
            adj[u].add(v)
            indegree[v] += 1
        
        q = deque()
        for ch, i in indegree.items():
            if i == 0:
                q.append(ch)

        result = []
        while q:
            ch = q.popleft()
            result.append(ch)
            for nbr in adj[ch]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    q.append(nbr)
        
        return "".join(result) if len(result)==len(indegree) else ""




        