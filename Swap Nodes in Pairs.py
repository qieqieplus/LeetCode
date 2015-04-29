# Definition for singly-linked list.
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
