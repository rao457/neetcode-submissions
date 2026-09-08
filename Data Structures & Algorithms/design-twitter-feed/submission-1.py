class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = {}      # userId -> [(time, tweetId)]
        self.following = {}   # userId -> set of followees

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int):
        import heapq

        heap = []

        # Own tweets
        for time, tweetId in self.tweets.get(userId, []):
            heapq.heappush(heap, (-time, tweetId))

        # Followed users' tweets
        for followee in self.following.get(userId, set()):
            for time, tweetId in self.tweets.get(followee, []):
                heapq.heappush(heap, (-time, tweetId))

        result = []

        while heap and len(result) < 10:
            time, tweetId = heapq.heappop(heap)
            result.append(tweetId)

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)