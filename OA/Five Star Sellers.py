'''Five Star Sellers

Given the number of five-star and total reviews for each product a company sells, as well as the threshold percentage,
what is the minimum number of additional five-star reviews the company needs to become five star seller.

public static int fiveStarReviews(List<List<Integer>> productRatings, int ratingsThreshold){

}
Examples
Example 1:
Input:
noOfProduct = 3

productRatings = [[4,4],[1,2],[3,6]] -> here, [1,2] indicates => [1 (five star reviews) ,2 (total reviews)].

threshold = 77

Output: 3
Explanation :
We need to get the seller reach the threshold with minimum number of additional five star reviews.

Before we add more five star reviews, the percentage for this seller is ((4/4) + (1/2) + (3/6))/3 = 66.66%

If we add a five star review to 2nd product, ((4/4) + (2/3) + (3/6))/3 = 72.22%

If we add another five star review to 2nd product, ((4/4) + (3/4) + (3/6))/3 = 75%

If we add a five star review to 3rd product, ((4/4) + (3/4) + (4/7))/3 = 77.38%

At this point, 77% (threshold) is met. Therefore, answer is 3 (because that is the minimum five star reviews we need
to add, to get the seller reach the threshold).

Constraints:
1 <= productRatings.size() <=200

In product ratings, [fivestar, total], fivestar <= 100, total <= 100

1 <= ratingsThreshold < 100

productRatings contains only non negative integers.
'''

from __future__ import annotations
import heapq
class Rating:
    def __init__(self, numOfFiveStars, reviewCount):
        self.numOfFiveStars = numOfFiveStars
        self.reviewCount = reviewCount

    def __float__(self):
        return self.numOfFiveStars / self.reviewCount

    def __lt__(self, other: Rating):
        return self.gain > other.gain

    @property
    def increaseReview(self):
        return Rating(self.numOfFiveStars + 1 , self.reviewCount + 1)

    @property
    def gain(self):
        return float(self.increaseReview) - float(self)

class Solution:
    def fiveStarSeller(self, productRatings, threshold):
        numOfRatings = len(productRatings)
        ratings = [Rating(n, d) for n, d in productRatings]
        heapq.heapify(ratings)
        diff = threshold / 100 - (sum(float(review) for review in ratings)) / 3
        count = 0
        print(ratings)
        while diff > 0:
            item = heapq.heappop(ratings)
            heapq.heappush(ratings, item.increaseReview)
            diff -= item.gain / numOfRatings
            count += 1
        return count

productRatings = [[4,4],[1,2],[3,6]]
threshold = 77
print(Solution.fiveStarSeller((), productRatings, threshold))


# Same approach with creating different class
import heapq
class Solution:
    def fiveStarSeller(self, productRatings, threshold):

        def gainRating(rating, count, prevRating, prevRatingCount):
            return (rating/count) - (prevRating/prevRatingCount)

        def increaseRatings(rating, ratingCount):
            return rating+1, ratingCount+1

        def float(rating, count):
            return rating/count

        def setNewValueAfterChange(rating,count):
            nonlocal afterChange
            currentValue = float(rating, count)
            newValue = float(rating+1, count+1)
            afterChange = newValue - currentValue

        afterChange = 0
        length = len(productRatings)
        heap = []
        for rating, count in productRatings:
            setNewValueAfterChange(rating, count)
            heapq.heappush(heap, (-afterChange, rating, count))

        current = [float(rating, count) for rating, count in productRatings]
        diff = threshold / 100 - (sum(current)/length)
        count = 0
        while diff > 0:
            gain, rating, ratingCount = heapq.heappop(heap)
            increaseRating, increaseCount = increaseRatings(rating, ratingCount)
            setNewValueAfterChange(increaseRating, increaseCount)
            heapq.heappush(heap, (-afterChange, increaseRating, increaseCount))
            gain = gainRating(increaseRating, increaseCount, rating, ratingCount)
            diff -= gain / length
            count += 1
        return count


productRatings = [[4,4],[1,2],[3,6]]
threshold = 77
print(Solution.fiveStarSeller((), productRatings, threshold))