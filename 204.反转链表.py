class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        tmp = []
        while head is not None:
            tmp.append(head)
            head = head.next

        p = tmp[-1]
        res = p
        for i in range(len(tmp)-1, 0, -1):
            p.next = tmp[i-1]
            p = p.next
        p.next = None

        return res

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