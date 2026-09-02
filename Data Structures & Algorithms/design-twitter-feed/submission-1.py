from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.userfollow = defaultdict(set)
        self.newsfeed = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.newsfeed[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minheap = []
        users = self.userfollow[userId] | {userId}

        for followee in users:
            if followee in self.newsfeed:
                index = len(self.newsfeed[followee]) - 1
                count, tweetId = self.newsfeed[followee][index]
                minheap.append([count, tweetId, followee, index - 1])

        heapq.heapify(minheap)

        while minheap and len(res) < 10:
            count, tweetId, followee, index = heapq.heappop(minheap)
            res.append(tweetId)

            if index >= 0:
                count1, tweetId1 = self.newsfeed[followee][index]
                heapq.heappush(minheap, [count1, tweetId1, followee, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userfollow[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.userfollow[followerId].discard(followeeId)