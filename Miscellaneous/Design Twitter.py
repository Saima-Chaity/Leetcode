'''Design Twitter - https://leetcode.com/problems/design-twitter/

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see
the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.
void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this
function will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in
the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered
from most recent to least recent.
void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID
followeeId.

Example 1:

Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should
precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer
following user 2.
'''

from collections import deque, defaultdict
from heapq import *

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = 0
        self.user_tweets = defaultdict(deque)
        self.followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.time += 1
        tweets = self.user_tweets[userId]
        tweets.append(((self.time), tweetId))
        if len(tweets) > 10:
            tweets.popleft()

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        heap = []
        tweets = self.user_tweets[userId]
        heap.extend(tweets)
        heapify(heap)
        for user in self.followers[userId]:
            followers_tweets = self.user_tweets[user]
            for i in range(len(followers_tweets) - 1, -1, -1):
                if len(heap) < 10:
                    heappush(heap, followers_tweets[i])
                else:
                    if heap[0][0] < followers_tweets[i][0]:
                        heappushpop(heap, followers_tweets[i])
                    else:
                        break
        return [heappop(heap)[1] for _ in range(len(heap))][::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followers[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)