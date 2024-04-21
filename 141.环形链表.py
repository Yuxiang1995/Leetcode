# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head and head.next:
            pt1 = head
            pt2 = head.next
            while pt1 and pt2:
                if pt1 == pt2:
                    return True

                if pt2.next:
                    pt1 = pt1.next
                    pt2 = pt2.next.next
                else:
                    return False

        return False