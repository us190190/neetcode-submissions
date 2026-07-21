class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        words = set(wordList)
        q = deque()
        q.append(beginWord)

        steps = 0
        while q:
            steps += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node == endWord:
                    return steps
                for i in range(len(node)):
                    for c in range(ord('a'), ord('z')+1):
                        nxt_str = node[:i]+chr(c)+node[i+1:]
                        if nxt_str in words:
                            q.append(nxt_str)
                            words.remove(nxt_str)
        
        return 0
        