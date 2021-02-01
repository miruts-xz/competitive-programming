# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        i, tail, prevTail, prev, node, root = 1, None, None, None, head, None
        c = self.count(head)
        if c < 2:
            return head
        while node:
            temp = node.next
            node.next = None
            # i is not multiple of k
            if i % 2:
                if not prev and tail:
                    prevTail = tail
                    tail = node
                if not tail and not prev:
                    tail = node
                    prev = node
                else:
                    node.next = prev
                    prev = node
            else:
                node.next = prev
                if not tail:
                    tail = node
                if not root:
                    root = node
                if prevTail:
                    prevTail.next = node
                prev = None
                if c - i < 2:
                    node = temp
                    break
            i += 1
            node = temp
        if node:
            tail.next = node
        return root

    def count(self, head: ListNode) -> int:
        c = 0
        node = head
        while node:
            c += 1
            node = node.next
        return c
