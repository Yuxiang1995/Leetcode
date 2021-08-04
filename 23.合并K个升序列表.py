class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists) -> ListNode:
        res = ListNode()
        r = res
        flag = True
        while flag:
            mmin = 10000000
            index = -1
            for i, listnode in enumerate(lists):
                if listnode:
                    flag = True
                    if listnode.val < mmin:
                        index = i
                        mmin = listnode.val
                else:
                    flag = False
            if flag:
                res.val = lists[index].val
                lists[index] = lists[index].next
                tmp = ListNode()
                res.next = tmp
                res = res.next
            else:
                del res
                print(r)
                print(res)
        return r
