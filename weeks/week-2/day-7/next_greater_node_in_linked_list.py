# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        i, n = 0, head
        while n:
            i += 1
            n = n.next
        result, stack, node, i = [0] * i, [], head, 0
        while node:
            next_node = node.next
            node.next = None
            if not stack:
                stack.append((i, node))
            else:
                while stack and stack[-1][1].val < node.val:
                    n = stack.pop()
                    result[n[0]] = node.val
                stack.append((i, node))
            node = next_node
            i += 1
        while stack:
            n = stack.pop()
            result[n[0]] = 0
        return result
