from collections import defaultdict
import heapq

class Twitter:
    # user follows followee then gets tweets
    def __init__(self):
        self.follows = defaultdict(set)    # [userId] follows: followeeId
        self.tweets = defaultdict(list)    # [userId]'s: (timestamp, tweets)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        allTweets = []
        for t in self.tweets[userId]:
            allTweets.append( (-t[0], t[1]))

        for followee in self.follows[userId]:
            for t in self.tweets[followee]:
                allTweets.append( (-t[0], t[1]))

        heapq.heapify(allTweets)
        
        result = []
        for i in range(min(10, len(allTweets))):
            _, tweet = heapq.heappop(allTweets)
            result.append(tweet)

        return result

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
