class Twitter:

    def __init__(self):
        self.tweets_heaps = {}
        self.time = 0
        self.followers = {}
        self.MAX_TWEETS = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets_heaps:
            self.tweets_heaps[userId] = []
        heapq.heappush(self.tweets_heaps[userId], [self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followers = self.followers[userId] if userId in self.followers else set()
        followers.add(userId)
        feed = []
        for follower_id in followers:
            if follower_id not in self.tweets_heaps:
                continue
            tweets_copy = self.tweets_heaps[follower_id].copy()
            i = 0
            while tweets_copy and i<self.MAX_TWEETS:
                tweet = heapq.heappop(tweets_copy)
                heapq.heappush(feed, tweet)
                i += 1
        
        result = []
        while feed and len(result)<self.MAX_TWEETS:
            tweet = heapq.heappop(feed)
            result.append(tweet[1])
        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = set()
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = set()
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)

        
