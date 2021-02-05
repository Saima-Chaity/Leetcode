'''# Search Suggestions System - https://leetcode.com/problems/search-suggestions-system/
'''
class Solution:
    def suggestedProducts(self, products: [str], searchWord: str):

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

        for i in range(2, len(searchWord)+1):
            current = searchWord[:i]
            words = getMatchingWords(current)
            result.append(words[:3])
        return result

products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
#output : [['mobile', 'moneypot', 'monitor'], ['mouse', 'mousepad'],
# ['mouse', 'mousepad'], ['mouse', 'mousepad']]
print(Solution.suggestedProducts((), products, searchWord))