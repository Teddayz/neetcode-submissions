from heapq import heappush_max, heappop_max

class Twitter:

    def __init__(self):
        self.time = 0
        self.follow_table = defaultdict(set)
        self.tweets = defaultdict(list)
        self.NUMOFTWEETS = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        heappush_max(self.tweets[userId], (self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []
        for tweet in self.tweets[userId]:
            heappush_max(heap, tweet)
        followings = self.follow_table.get(userId, [])
        for following in followings:
            for tweet in self.tweets[following]:
                heappush_max(heap, tweet)
        res = []
        for _ in range(self.NUMOFTWEETS):
            if heap:
                time, tweetId = heappop_max(heap)
                res.append(tweetId)
            else:
                break
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follow_table[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_table[followerId]:
            self.follow_table[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)