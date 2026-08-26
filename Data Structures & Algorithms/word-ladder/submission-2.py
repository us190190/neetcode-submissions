class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        words = set(wordList)
        q = deque()

        q.append(beginWord)

        steps = 0
        while q:
            steps += 1
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return steps
                for idx in range(len(word)):
                    for ch in range(ord('a'), ord('z')+1):
                        new_word = word[:idx] + chr(ch) + word[idx+1:]
                        if new_word!=word and new_word in words:
                            words.remove(new_word)
                            q.append(new_word)
        
        return 0


        
