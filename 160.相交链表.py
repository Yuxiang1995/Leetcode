# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        tmpA = headA
        tmpB = headB

        flagA = flagB = 0
        while tmpA is not None or not (flagA and flagB):
            if tmpA == tmpB:
                return tmpA

            if tmpA.next or flagA:
                tmpA = tmpA.next
            else:
                tmpA = headB
                flagA = 1

            if tmpB.next or flagB:
                tmpB = tmpB.next
            else:
                tmpB = headA
                flagB = 1

        return None

