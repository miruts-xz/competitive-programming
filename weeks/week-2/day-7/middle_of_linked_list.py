# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        s, f = head, head
        while f:
            if f.next is None:
                return s
            s = s.next
            fnx = f.next
            f = fnx.next
        return s
