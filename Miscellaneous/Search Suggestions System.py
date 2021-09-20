# Search Suggestions System - https://leetcode.com/problems/search-suggestions-system/
'''Given an array of strings products and a string searchWord. We want to design a system that suggests at most three
product names from products after each character of searchWord is typed. Suggested products should have common prefix
with the searchWord. If there are more than three products with a common prefix return the three lexicographically
minimums products.

Return list of lists of the suggested products after each character of searchWord is typed.

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]'''


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        def getMatchingWords(char):
            output = []
            for product in products:
                if product.startswith(char):
                    output.append(product)
                    if len(output) > 3:
                        break
            return output

        products.sort()
        result = []
        current = ""
        for char in searchWord:
            current += char
            words = getMatchingWords(current)
            result.append(words[:3])
        return result



#Using heap
import heapq
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        heap = []
        result = []
        current = ""
        for char in searchWord:
            current += char
            for product in products:
                if product.startswith(current):
                    heapq.heappush(heap, product)

            temp = []
            for i in range(0, 3):
                if heap:
                    temp.append(heapq.heappop(heap))
            result.append(temp)
            heap = []
        return result


# Using Trie
class Trie:
    def __init__(self):
        self.nodes = dict()
        self.words = list()

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        self.trie = Trie()
        for product in products:
            self.buildTrie(product, self.trie)

        output = []
        prefix = ""
        for char in searchWord:
            prefix += char
            result = self.find(prefix)
            result.sort()
            if len(result) > 3:
                output.append(result[:3])
            else:
                output.append(result)
        return output

    def find(self, keyword):
        t = self.trie
        for char in keyword:
            if char in t.nodes:
                t = t.nodes[char]
            else:
                return []
        return t.words

    def buildTrie(self, product, t):
        for char in product:
            if char not in t.nodes:
                t.nodes[char] = Trie()
            t = t.nodes[char]
            t.words.append(product)
