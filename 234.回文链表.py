# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True

        firstHalfEnd = self.endOfHalf(head)
        secondHalfStart = self.reverseList(firstHalfEnd.next)

        firstPosition = head
        secondPosition = secondHalfStart
        while secondPosition:
            if firstPosition.val != secondPosition.val:
                return False
            firstPosition = firstPosition.next
            secondPosition = secondPosition.next

        firstHalfEnd.next = self.reverseList(secondHalfStart)
        return True

    def endOfHalf(self, head: ListNode):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head: ListNode):
        pre = None
        cur = head

        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next

        return pre