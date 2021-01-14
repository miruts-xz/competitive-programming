# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        s = self.insertionSortList(head.next)
        head.next = None
        h = self.insertNode(s, head)
        return h

    def insertNode(self, s: ListNode, node: ListNode) -> ListNode:
        n = s
        prev = None
        while n and n.val < node.val:
            prev = n
            n = n.next
        if prev:
            prev.next = node
        node.next = n
        return s if prev else node
