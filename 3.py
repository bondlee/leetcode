def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    start = 0
    maxlen = 0
    alpha = {}
    
    for i,a in enumerate(s):
        if a in alpha:
            if alpha[a]>=start:
                start = alpha[a]+1
                                
        alpha[a] = i
        length = i-start+1
        if length>maxlen:
            maxlen = length
    return maxlen


if __name__ == "__main__":
    s = "abba"
    print lengthOfLongestSubstring(s)
        