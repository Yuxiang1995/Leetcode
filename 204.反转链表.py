class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head

        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next

        return pre

if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    a.next = b
    b.next = c
    ss = Solution()
    res = ss.reverseList(a)
    while res:
        print(res.val)
        res = res.next