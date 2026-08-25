class Twitter:

    def __init__(self):
        self.user_follows = defaultdict(set)
        self.user_tweets_max_heap = defaultdict(list)
        self.clock = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.user_tweets_max_heap[userId], (-self.clock, tweetId))
        self.clock += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        user_follows = self.user_follows.get(userId, set())
        user_follows.add(userId)

        all_top_tweets = []

        for followId in user_follows:
            if followId not in self.user_tweets_max_heap:
                continue
            tweets_copy = self.user_tweets_max_heap[followId].copy()
            count = 10
            while count and tweets_copy:
                heapq.heappush(all_top_tweets, heapq.heappop(tweets_copy))
                count -= 1
        
        result = []
        while all_top_tweets:
            result.append(heapq.heappop(all_top_tweets)[1])
            if len(result)==10:
                return result
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_follows[followerId]:
            self.user_follows[followerId].remove(followeeId)
