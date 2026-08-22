class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        visited = defaultdict(int)

        for num in nums:
            visited[num] += 1
        
        reverse_visited = defaultdict(List[int])

        for num, freq in visited.items():
            if freq not in reverse_visited:
                reverse_visited[freq] = []
            reverse_visited[freq].append(num)
        
        frequencies = list(reverse_visited.keys())
        frequencies.sort(reverse=True)

        top_k = []
        for freq in frequencies:
            for num in reverse_visited[freq]: 
                if k:
                    top_k.append(num)
                    k -= 1
                else:
                    return top_k

        return top_k