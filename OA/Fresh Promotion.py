'''Fresh Promotion
Amazon is running a promotion in which customers receive prizes for purchasing a secret
combination of fruits. The combination will change each day, and the team running the
promotion wants to use a code list to make it easy to change the combination. The code list
contains groups of fruits. Both the order of the groups within the code list and the order
of the fruits within the groups matter. However, between the groups of fruits, any number,
and type of fruit is allowable. The term "anything" is used to allow for any type of fruit
to appear in that location within the group.

Consider the following secret code list: [[apple, apple], [banana, anything, banana]]
Based on the above secret code list, a customer who made either of the following purchases
would win the prize:
orange, apple, apple, banana, orange, banana
apple, apple, orange, orange, banana, apple, banana, banana

Write an algorithm to output 1 if the customer is a winner else output 0.

Input
The input to the function/method consists of two arguments:
codeList, a list of lists of strings representing the order and grouping of specific fruits
that must be purchased in order to win the prize for the day.
shoppingCart, a list of strings representing the order in which a customer purchases fruit.

Output
Return an integer 1 if the customer is a winner else return 0.

Note
'anything' in the codeList represents that any fruit can be ordered in place of 'anything'
in the group. 'anything' has to be something, it cannot be "nothing."
'anything' must represent one and only one fruit.
If secret code list is empty then it is assumed that the customer is a winner.

Example 1:

Input: codeList = [[apple, apple], [banana, anything, banana]]
shoppingCart = [orange, apple, apple, banana, orange, banana]

Output: 1
Explanation:
codeList contains two groups - [apple, apple] and [banana, anything, banana].
The second group contains 'anything' so any fruit can be ordered in place of 'anything'
in the shoppingCart. The customer is a winner as the customer has added fruits in the
order of fruits in the groups and the order of groups in the codeList is also maintained
in the shoppingCart.

Example 2:

Input: codeList = [[apple, apple], [banana, anything, banana]]
shoppingCart = [banana, orange, banana, apple, apple]

Output: 0
Explanation:
The customer is not a winner as the customer has added the fruits in order of groups but
group [banana, orange, banana] is not following the group [apple, apple] in the codeList.

Example 3:

Input: codeList = [[apple, apple], [banana, anything, banana]]
shoppingCart = [apple, banana, apple, banana, orange, banana]

Output: 0
Explanation:
The customer is not a winner as the customer has added the fruits in an order which is not
following the order of fruit names in the first group.

Example 4:
Input: codeList = [[apple, apple], [apple, apple, banana]] shoppingCart = [apple, apple, apple, banana]

Output: 0
Explanation:
The customer is not a winner as the first 2 fruits form group 1, all three fruits would
form group 2, but can't because it would contain all fruits of group 1.'''

class Sol:
    def determine_winner(self, secretFruitList, customerPurchasedList) -> int:

        def hasOrder(customerPurchasedList, codeList, cartIndex):
            for code in codeList:
                if cartIndex < len(customerPurchasedList) and (code == "anything" or code == customerPurchasedList[cartIndex]):
                    cartIndex += 1
                else:
                    return False
            return True

        if len(secretFruitList) == 2:
            if len(secretFruitList[0]) + len(secretFruitList[0]) > len(customerPurchasedList):
                return False
        else:
            if len(secretFruitList[0]) < len(customerPurchasedList) or len(secretFruitList[0]) > len(customerPurchasedList):
                return False

        cartIndex = 0
        firstList = False
        secondList = False if len(secretFruitList) == 2 else True
        while cartIndex < len(customerPurchasedList):
            current = customerPurchasedList[cartIndex]
            if not firstList and (secretFruitList[0][0] == 'anything' or secretFruitList[0][0] == current) and hasOrder(customerPurchasedList, secretFruitList[0], cartIndex):
                firstList = True
                cartIndex += len(secretFruitList[0])
            elif len(secretFruitList) == 2 and (
                (secretFruitList[1][0] == 'anything' or secretFruitList[1][0] == current) and hasOrder(customerPurchasedList, secretFruitList[1], cartIndex)):
                cartIndex += len(secretFruitList[1])
                secondList = True
                if not firstList:
                    return False
            else:
                cartIndex += 1

        return True if firstList and secondList else False

if __name__ == '__main__':
    solution = Sol()

    codeList = [["apple", "apple"]]
    shoppingCart = ["apple", "apple"]
    print(solution.determine_winner(codeList, shoppingCart))

    codeList = [['anything', 'apple'], ['banana', 'anything', 'banana']]
    shoppingCart = ['orange', 'grapes', 'apple', 'orange', 'orange', 'banana', 'apple', 'banana', 'banana']
    print(solution.determine_winner(codeList, shoppingCart))

    codeList = [["apple"]]
    shoppingCart = ["orange"]
    print(solution.determine_winner(codeList, shoppingCart))

    codeList = [['apple', 'apple'], ['banana', 'anything', 'banana']]
    shoppingCart = ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']
    print(solution.determine_winner(codeList, shoppingCart))

    codeList = [['apple', 'apple'], ['banana', 'anything', 'banana']]
    shoppingCart = ['banana', 'orange', 'banana', 'apple', 'apple']
    print(solution.determine_winner(codeList, shoppingCart))

    codeList = [["apple", "apple"], ["banana", "apple", "anything"]]
    shoppingCart = ["orange", "apple", "apple", "banana", "orange", "apple", "orange"]
    print(solution.determine_winner(codeList, shoppingCart))

    codeList = [['apple', 'apple'], ['apple', 'apple', 'banana']]
    shoppingCart = ['apple', 'apple', 'apple', 'banana']
    print(solution.determine_winner(codeList, shoppingCart))

    codeList = [['apple', 'apple'], ['banana', 'anything', 'banana']]
    shoppingCart = ['apple', 'banana', 'apple', 'banana', 'orange', 'banana']
    print(solution.determine_winner(codeList, shoppingCart))
