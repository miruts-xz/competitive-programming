# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        self.reverse(head, head.next)
        return self.head

    def reverse(self, curr, nxt):
        if nxt is None:
            self.head = curr
            return curr
        prev_head = self.reverse(curr.next, nxt.next)
        curr.next = None
        prev_head.next = curr
        return curr
