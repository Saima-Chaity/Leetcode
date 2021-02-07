'''
The input to the function/method consists of five arguments - numCompetitors, an integer representing
the number of competitors for the Echo device;
topNCompetitors, is an integer representing the maximum number of competitors that Amazon wants to
identify;
competitors, a list of strings representing the competitors;
numReviews, an integer representing the number of reviews from different websites that are identified
by the automated webcrawler;
reviews, a list of string where each element is a string that consists of space-separated words
representing user reviews.

Output
Return a list of strings representing Amazon's top N competitors in order of most frequently mentioned
to least frequent.

Note
The comparison of strings is case-insensitive. If the value of topNCompetitors is more than the
number of competitors discussed in the reviews then output the names of only the competitors mention.
If competitors have the same count (e.g. newshop=2, shopnow=2, mymarket=4), sort alphabetically.
topNCompetitors=2, Output=[mymarket, newshop]

Example
Input:
numCompetitors=6
topNCompetitors = 2
competitors = [newshop, shopnow, afashion, fashionbeats, mymarket, tcellular]
numReviews = 6
reviews = [
"newshop is providing good services in the city; everyone should use newshop",
"best services by newshop",
"fashionbeats has great services in the city",
"I am proud to have fashionbeats",
"mymarket has awesome services",
"Thanks Newshop for the quick delivery"]

Output
["newshop", "fashionbeats"]

Explanation
"newshop" is occurring in 3 different reviews. "fashionbeats" is occuring in 2 different user
reviews and "mymarket" is occurring in only 1 review.
'''

import re
import heapq
class Solution:
  def topKFrequentlyMentionedKeyword(self, numCompetitors, topNCompetitors, competitors, numReviews, reviews):

    if not competitors or not reviews:
        return []

    if topNCompetitors == 0:
        return []

    competitors_dict = dict()
    for item in competitors:
        competitors_dict[item] = (0, 0)

    for review in reviews:
        updatedCount = {item:False for item in competitors}
        for word in review.lower().split():
            word = re.sub('[^a-z]', '', word)
            if competitors_dict.get(word):
                freq, review = competitors_dict[word][0], competitors_dict[word][1]
                if not updatedCount[word]:
                    updatedCount[word] = True
                    review += 1
                competitors_dict[word] = (freq + 1, review)


    for item in competitors:
        if competitors_dict[item][0] == 0:
            del competitors_dict[item]

    if topNCompetitors > numCompetitors:
        return [competitor for competitor in competitors_dict]

    topCompetitors = []
    for item in competitors_dict:
        freq, review = competitors_dict[item][0], competitors_dict[item][1]
        heapq.heappush(topCompetitors, (-1*freq, -1*review, item))

    output = []
    for i in range(topNCompetitors):
        item = heapq.heappop(topCompetitors)
        output.append(item[2])
        if len(topCompetitors) == 0:
            break
    return output



numToys = 6
topToys = 2
toys = ["elmo", "elsa", "legos", "drone", "tablet", "warcraft"]
numQuotes = 6
quotes = [
"Elmo is the hottest of the season! Elmo will be on every kid's wishlist!",
"The new Elmo dolls are super high quality",
"Expect the Elsa dolls to be very popular this year, Elsa!",
"Elsa and Elmo are the toys I'll be buying for my kids, Elsa is good",
"For parents of older kids, look into buying them a drone",
"Warcraft is slowly rising in popularity ahead of the holiday season"
];

print(Solution.topKFrequentlyMentionedKeyword((), numToys, topToys, toys, numQuotes, quotes))


numToys = 6
topToys = 2
toys = ["newshop", "shopnow", "afashion", "fashionbeats", "mymarket", "tcellular"]
numQuotes = 6
quotes = [
  "newshop is providing good services in the city; everyone should use newshop",
  "best services by newshop",
  "fashionbeats has great services in the city",
  "I am proud to have fashionbeats",
  "mymarket has awesome services",
  "Thanks Newshop for the quick delivery"
];

print(Solution.topKFrequentlyMentionedKeyword((), numToys, topToys, toys, numQuotes, quotes))
