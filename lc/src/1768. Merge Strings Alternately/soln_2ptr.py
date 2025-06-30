class Solution(object):
    def mergeAlternately(self, word1, word2):
        i = j = 0
        res = []

        while i < len(word1) or j < len(word2):
            if i < len(word1):
                res.append(word1[i])
                i += 1
            if j < len(word2):
                res.append(word2[j])
                j += 1

        return ''.join(res)


# Two pointers i and j track current positions in word1 and word2.
# While loop runs as long as either pointer hasn't reached the end.
#Time Complexity: O(n + m)
#space Complexity: O(n + m) for the output list


