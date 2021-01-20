# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:
            head = head.next
        node = head
        while node and node.next:
            if node.next.val == val:
                nxt = node.next.next
                node.next = nxt
                continue
            node = node.next
        return head
