class Twitter:

    def __init__(self):
        self.tweets_max_heap = {}
        self.user_follows = {}
        self.MAX_TWEETS = 10
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets_max_heap:
            self.tweets_max_heap[userId] = []
        heapq.heappush(self.tweets_max_heap[userId], [self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followee_ids = self.user_follows[userId] if userId in self.user_follows else set()
        followee_ids.add(userId)
        result_heap = []
        for followee_id in followee_ids:
            if followee_id not in self.tweets_max_heap:
                continue
            extract_from_tweets = self.tweets_max_heap[followee_id].copy()
            i = self.MAX_TWEETS
            while len(extract_from_tweets) and i>0:
                tweet = heapq.heappop(extract_from_tweets)
                heapq.heappush(result_heap, tweet)
                i -= 1
        
        result = []
        while len(result_heap) and len(result) < self.MAX_TWEETS:
            _, tweet_id = heapq.heappop(result_heap)
            result.append(tweet_id)
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_follows:
            self.user_follows[followerId] = set()
        self.user_follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_follows:
            return None
        if followeeId not in self.user_follows[followerId]:
            return None
        self.user_follows[followerId].remove(followeeId)
