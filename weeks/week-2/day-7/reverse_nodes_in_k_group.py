#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count = 0
        result = []
        node = head
        while node:
            count += 1
            result.append(node.val)
            node = node.next
        pairs = count // k
        rem = count % k
        reverse = []
        for i in range(1, pairs + 1):
            reverse += result[k * (i - 1):k * i][::-1]
        print(reverse)
        reverse += result[(pairs * k):]

        node = head
        count = 0
        while node:
            node.val = reverse[count]
            count += 1
            node = node.next
        return head
