class Solution(object):
    def mergeAlternately(self, word1, word2):
        str_res = ""
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                str_res += word1[i]
            if i < len(word2):
                str_res += word2[i]
        return str_res
## O(n+m) where n and m is len of the words 
## O(n+m) space where n+m is len of result string
## string concatenation with += is not optimal for performance on longer strings. Each += on a string creates a new copy of the string (since strings are immutable in Python), so the operation ends up being O(n²) in time if the strings are long.

