from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        while len(lists) > 1:
            lists.append(self.mergeTwoLists(lists.pop(), lists.pop()))
        return lists.pop() if lists else None

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = None
        tail = None
        while l1 and l2:
            if l1.val <= l2.val:
                temp = l1.next
                l1.next = None
                if not root:
                    root = l1
                    tail = root
                else:
                    tail.next = l1
                    tail = tail.next
                l1 = temp
            else:
                temp = l2.next
                l2.next = None
                if not root:
                    root = l2
                    tail = root
                else:
                    tail.next = l2
                    tail = tail.next
                l2 = temp
        if l1:
            if not root:
                root = l1
            else:
                tail.next = l1
        if l2:
            if not root:
                root = l2
            else:
                tail.next = l2
        return root
