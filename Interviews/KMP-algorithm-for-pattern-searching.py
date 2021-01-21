def computeLPSArray(pattern, patternLength, lps):
    initialLength = 0
    lps[0] = 0
    i = 1
    while i < patternLength:
        if pattern[i] == pattern[initialLength]:
            initialLength += 1
            lps[i] = initialLength
            i += 1
        else:
            if initialLength != 0:
                initialLength = lps[initialLength-1]
            else:
                lps[i] = 0
                i += 1

def KMPSearch(pattern, text):
    textLength = len(text)
    patternLength = len(pattern)
    lps = [0] * patternLength

    computeLPSArray(pattern, patternLength, lps)
    print(lps)
    i = 0
    j = 0
    while i < textLength:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == patternLength:
            print(str(i-j))
            j = lps[j-1]

        elif i < textLength and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
KMPSearch(pat, txt)