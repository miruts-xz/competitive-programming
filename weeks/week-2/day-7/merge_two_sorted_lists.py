#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Class implements merge two sorted lists leetcode challenge @https://leetcode.com/problems/merge-two-sorted-lists
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = []
        node1 = l1
        node2 = l2
        i, j = 0, 0
        if self.count(l1) == 0:
            return l2
        if self.count(l2) == 0:
            return l1
        while node1 and node2:
            val1 = self.get(l1, i)
            val2 = self.get(l2, j)
            print(val1, val2)
            if val1 <= val2:
                result.append(val1)
                node1 = node1.next
                i += 1
            else:
                result.append(val2)
                node2 = node2.next
                j += 1
        while node1:
            result.append(node1.val)
            node1 = node1.next
        while node2:
            result.append(node2.val)
            node2 = node2.next
        result.reverse()
        r = []
        for i in range(len(result)):
            if i > 0:
                r.append(ListNode(result[i], r[i - 1]))
            else:
                r.append(ListNode(result[i]))
        return r.pop()

    def count(self, head: ListNode) -> int:
        count = 0
        node = head
        while node:
            count += 1
            node = node.next
        return count

    def get(self, head: ListNode, index: int) -> int:
        node = head
        for i in range(index):
            node = node.next
        return node.val
