# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        lis = []
        while head:
            lis.append(head.val)
            head = head.next
        
        if lis == lis[::-1]:
            return True
        else:
            return False