class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        lis=[]
        for i in s:
            if i in '1234567890':
                lis.append(int(i))
        lis1 = list(set(lis))
        lis1.sort()
        
        if len(lis1) < 2:
            return -1
        else:
            return lis1[-2]
