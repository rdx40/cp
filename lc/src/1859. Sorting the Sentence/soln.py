class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        ord = [""] * len(words)

        for word in words:
            index = int(word[-1])-1
            ord[index] = word[:-1]
        return  " ".join(ord) 
        
