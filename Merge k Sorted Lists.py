#
#   I KNOW THIS IS ALMOST CHEATING,
#   BUT... FUCK LINKED LIST IN PYTHON
#
##Definition for singly-linked list.
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        l = []
        for ls in lists:
            l += self.getListVal(ls)
        l.sort()
        #return l
        return self.listCreator(l)

    def getListVal(self, ls):
        tmp = []
        if ls:
            while True:
                tmp.append(ls.val)
                if not ls.next:
                    break
                ls = ls.next
        return tmp

    def listCreator(self, nodeValues):
        temp = head = ListNode(0)
        for value in nodeValues:
            temp.next = ListNode(value)
            temp = temp.next
    
        return head.next
