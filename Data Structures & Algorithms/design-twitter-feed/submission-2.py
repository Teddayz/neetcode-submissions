class Twitter:

    def __init__(self):
        self.time = 0
        self.followers = {}
        self.tweets = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        currTweetsList = self.tweets.get(userId)
        if not currTweetsList:
            currTweetsList = []
            heapq.heapify_max(currTweetsList) # currTweetList contains tuple(time, tweetId)
        heapq.heappush_max(currTweetsList, (self.time, tweetId))
        self.time += 1
        self.tweets[userId] = currTweetsList

    def getNewsFeed(self, userId: int) -> List[int]:
        uniqueFollowing = self.followers.get(userId)
        result = []
        if not uniqueFollowing:
            tweets = self.tweets.get(userId) # returns a heap of tweets ordered by recentcy, each popped item contains (time, tweetId)
            dummy = tweets.copy() if tweets else None
            for i in range(10):
                if dummy:
                    tweetId = heapq.heappop_max(dummy)[1]
                    result.append(tweetId)
                else:
                    break
        else:
            allTweets = []
            for following in uniqueFollowing:
                # Get all the heaps of the following and merge all into one heap
                tweets = self.tweets.get(following, [])
                allTweets += tweets
            if userId not in uniqueFollowing:
                allTweets += self.tweets.get(userId, [])
            heapq.heapify_max(allTweets) # Get all the tweets
            dummy = allTweets.copy() if allTweets else None
            for i in range(10):
                if dummy:
                    tweetId = heapq.heappop_max(dummy)[1]
                    result.append(tweetId)
                else:
                    break
            
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        followers = self.followers.get(followerId, set())
        followers.add(followeeId)
        self.followers[followerId] = followers
        self.time += 1
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        followers = self.followers.get(followerId, set())
        if followeeId in followers:
            followers.remove(followeeId)
        self.time += 1
