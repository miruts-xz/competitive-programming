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


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head
        i, tail, prevTail, prev, node, root = 1, None, None, None, head, None
        c = self.count(head)
        while node:
            temp = node.next
            node.next = None
            # i is not multiple of k
            if i % k:
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
                if c - i < k:
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


s = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

print(s.reverseKGroup(head, 2))
