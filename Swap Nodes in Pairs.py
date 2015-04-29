# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        if not head:
            return None
        if not head.next:
            return head
        ne = head.next
        head.next = self.swapPairs(ne.next)
        ne.next = head
        return ne
