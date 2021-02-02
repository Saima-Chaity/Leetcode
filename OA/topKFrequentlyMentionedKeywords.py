'''Given a list of reviews, a list of keywords and an integer k. Find the most popular k keywords in order of most
to least frequently mentioned.

The comparison of strings is case-insensitive. If keywords are mentioned an equal number of times in reviews,
sort alphabetically.'''

import re
from  collections import defaultdict
import heapq

class Solution:
  def topKFrequentlyMentionedKeyword(self, k, keywords, reviews ):

    if not keywords or not reviews:
      return []

    top_freq_keywords = defaultdict(list)
    for keyword in keywords:
      top_freq_keywords[keyword] = (0, 0)

    for review in reviews:
      updated_review_count = {keyword:False for keyword in keywords}
      for word in review.lower().split():
        word = re.sub('[^a-z]', '', word)
        if top_freq_keywords.get(word):
          curr_freq, curr_review = top_freq_keywords[word][0], top_freq_keywords[word][1]
          if not updated_review_count[word]:
            updated_review_count[word] = True
            curr_review += 1
          top_freq_keywords[word] = (curr_freq + 1, curr_review)

    for keyword in keywords:
      if top_freq_keywords[keyword][0] == 0:
        del top_freq_keywords[keyword]


    topKeywordsCollections = []
    for keyword in top_freq_keywords:
      total_freq, total_reviewCount = top_freq_keywords[keyword][0], top_freq_keywords[keyword][1]
      heapq.heappush(topKeywordsCollections, (-1*total_freq, -1*total_reviewCount, keyword))

    topKeywords = []
    for i in range(k):
      keyword = heapq.heappop(topKeywordsCollections)
      topKeywords.append(keyword[2])
      if not topKeywords:
        break
    return topKeywords


k = 2
keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews = [
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better than deltacellular.",
]

# Output:
# ["betacellular", "anacell"]

print(Solution.topKFrequentlyMentionedKeyword((), k, keywords, reviews))
