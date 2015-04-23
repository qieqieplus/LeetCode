# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        c=0
        l = []
        while l1 or l2 or c:
            d1 = l1.val if l1 else 0
            d2 = l2.val if l2 else 0
            n = d1 + d2 + c
            c = n//10
            val = n%10
            l.append(val)
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        #return l;
        return self.listCreator(l);

    def listCreator(self, nodeValues):
        temp = head = ListNode(0)
        for value in nodeValues:
            temp.next = ListNode(value)
            temp = temp.next
    
        return head.next
