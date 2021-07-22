# Created by mire on 7/22/21. Copyright 2021, All rights reserved.

# Definition for singly-linked list.
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack, temp = deque(), head.next
        while temp:
            stack.append(temp)
            temp = temp.next
        cur = head
        while len(stack) > 1:
            for node in (stack.pop(), stack.popleft()):
                cur.next, cur = node, node
        if stack:
            cur = stack[0]
        cur.next = None


if __name__ == "__main__":
    Solution().reorderList(ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4)))))
