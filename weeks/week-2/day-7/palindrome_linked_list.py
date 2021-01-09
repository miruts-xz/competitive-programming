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


head = ListNode(2)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(1)

head.next = node2
node2.next = node3
node3.next = node4


# Method implements palindrome linked list leetcode challenge @https://leetcode.com/problems/palindrome-linked-list
def isPalindrome(head: ListNode) -> bool:
    head_low = head
    head_high = reverse_linked_list(head)

    while head_low and head_high:
        if not head_low.val == head_high.val:
            return False
        head_low = head_low.next
        head_high = head_high.next
        if head_low == head_high:
            break
    return True


def reverse_linked_list(head: ListNode) -> ListNode:
    node_list = []
    node = head
    while node:
        node_list.append(ListNode(node.val))
        node = node.next
    local_head = None
    for i in range(len(node_list) - 1, 0, -1):
        if i == len(node_list) - 1:
            local_head = node_list[i]
            local_head.next = node_list[i - 1]
        else:
            node = node_list[i]
            node.next = node_list[i - 1]
    return local_head


print(isPalindrome(head))
