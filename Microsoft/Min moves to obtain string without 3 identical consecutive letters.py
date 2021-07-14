'''Min moves to obtain string without 3 identical consecutive letters
'''

'''To solve this task we need to find sequences of the same letters and if the sequence is longer than 3 divide 
length of this sequence to 3 and add result of the division to counters of needed moves.
Example of work:
3 consecutive: baaab, replace the middle a (3 / 3 == 1)
4 consecutive: baaaab, replace the third a (4 / 3 == 1)
5 consecutive: baaaaab, replace the third a (5 / 3 == 1)
6 consecutive: baaaaaab -> baabaaab -> baaab -> bab with 2 replacements (6 / 3 == 2)
10 consecutive: baaaaaaaaaab -> baabaaaaaaab -> baaaaaaab -> baaaab -> baab with 3 replacements (10 / 3 == 3)'''

def min_moves(s):
    moveCount = 0
    i = 0
    while i < len(s):
        nextIndex = i+1
        # if we meet sequence of the same letters
        while nextIndex < len(s) and s[i] == s[nextIndex]:
            nextIndex += 1
        # Here "next - i" is length of the sequence
        # Each third letter should be changed to remove too long sequences
        moveCount += (nextIndex - i) // 3
        i = nextIndex
    return moveCount

print(min_moves("baaab"))
print(min_moves("baaaab"))
print(min_moves("baaaaab"))
print(min_moves("baaaaaab"))
print(min_moves("baaaaaaaaaab"))