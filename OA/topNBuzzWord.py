import heapq
import re

# Input:
# numToys = 6
# topToys = 2
# toys = ["elmo", "elsa", "legos", "drone", "tablet", "warcraft"]
# numQuotes = 6
# quotes = [
# "Elmo is the hottest of the season! Elmo will be on every kid's wishlist!",
# "The new Elmo Elsa dolls are super high quality",
# "Expect the Elsa dolls to be very popular this year, Elsa!",
# "Elsa and Elmo are the toys I'll be buying for my kids, Elsa is good",
# "For parents of older kids, look into buying them a drone",
# "Warcraft is slowly rising in popularity ahead of the holiday season"
# ];


class Solution:
    def topNBuzzWords(self, numToys, topToys, toys, numQuotes, quotes):

        # Base case: if toys list is empty or quotes list is empty, the output list should also be []
        if not toys or not quotes:
            return []

        # Base case: if topToys are 0, that means we don't have to return any buzzwords
        if topToys == 0:
            return []


        # Dict to store toy buzzword as key and value as tuple in form of (total_freq, total_quotes)
        # So we will have dict like: {'elmo': (4, 3), 'elsa': (4, 2)}
        # Here, 'elmo': (4, 3) means word 'elmo' occurs total 4 times throughout all the quotes and it comes in 3 different quotes.
        #
        # We will first create entry for all toys with (total_freq, total_quotes) = (0, 0)
        toy_freq_quote = dict()
        for toy in toys:
            toy_freq_quote[toy] = (0, 0)

        # Iterate through all the quotes
        for q in quotes:
            # We need this updated_quote_count dict so that we don't increment the quote count for a buzzword more than once,
            # in case if it occurs multiple times in a single quote
            updated_quote_count = {toy: False for toy in toys}
            for word in q.lower().split():
                # Convert all the words to lowercase and split them.
                # Go through all the words of a quote and:
                #   - Remove all the extra characters from the words except "a-z". Basically we replace them with '' using regex.
                word = re.sub('[^a-z]', '', word)
                # Check if the current word is a toy/buzzword
                if toy_freq_quote.get(word):
                    curr_freq, curr_quote = toy_freq_quote[word][0], toy_freq_quote[word][1]
                    # If the current quote count is not already incremented for word w, do it and mark it in updated_quote_count
                    if not updated_quote_count[word]:
                        updated_quote_count[word] = True
                        curr_quote += 1
                    # Update freq and quote_count values
                    toy_freq_quote[word] = (curr_freq+1 , curr_quote)

        # Initially toy_freq_quote was created for all the given toys.
        # It is possible that some of those just don't appear in quotes.
        # Remove such toys from the toy_freq_quote whose frequency is 0

        for toy in toys:
            if toy_freq_quote[toy][0] == 0:
                del toy_freq_quote[toy]

        # Now, we have the dict ready with all the buzzwords from toys list that come in quotes,
        # along with their total frequency and total quote count.
        #
        # First thing to check is if topToys (i.e. number of top toys/buzzwords to return) is > total numToys (i.e. total buzzwords)
        #   - If it is, then as per the given requirement, we just need to return the list of present buzzwords in quotes.
        #
        # If we return here, then all the computation stops and we are done.

        if topToys > numToys:
            return [toy for toy in toy_freq_quote]

        # Declare a list which we can use as heap.
        buzzword_heap = []

        # Go through all buzzwords from toy_freq_quote dict and take their (total_freq, total_quote_count).
        # Add it to the buzzword_heap as (-1*total_freq, -1*total_quote_count, buzzword)
        #
        # - Since we want to order by maximum total_freq and after that maximum total_quote_count, we will multiply them with -1 when
        #   pushing into the heap.
        # - We do that because in Python heapq.heapify(list), the heap created is min-heap.
        # - If we don't multiply those numbers by -1, then we will output with minimum total_freq and total_quotes.
        # - Also, we keep the ordering like (total_freq, total_quote_count, buzzword)
        #   because we first have to get the buzzword with max frequency, after that with max quote_count, and in the end
        #   in alphabetical order of buzzwords themselves.
        for toy in toy_freq_quote:
            total_freq, total_quote_count = toy_freq_quote[toy][0], toy_freq_quote[toy][1]
            heapq.heappush(buzzword_heap, (-1*total_freq, -1*total_quote_count, toy))


        # Final result list
        top_buzzwords = []

        # Now we just do heappop equal to the total number of top buzzwords we have to return.
        # For every heappop, we will get back the tuple we have pushed:
        #   (total_freq, total_quote_count, buzzword)
        #
        # Since, in final output, all we need is buzzword, we just take the last element of the tuple, and append it to final list.
        for i in range(topToys):
            toy = heapq.heappop(buzzword_heap)
            top_buzzwords.append(toy[2])

            if not buzzword_heap:
                break

            # Check if there are any buzzwords left in the buzzword_heap or not.
            # There can be a case where we are asked to return top 5 buzzwords, but among all the quotes, only 3 buzzwords are present
            # In such case, we will return whatever buzzwords are present as per the sorting requirements given
            # This should be conveyed and discussed with interviewer

        return top_buzzwords

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

print(Solution.topNBuzzWords((), numToys, topToys, toys, numQuotes, quotes))

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

print(Solution.topNBuzzWords((), numToys, topToys, toys, numQuotes, quotes))