#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations.

from design_linked_list import ListNode

# Code implements deletion of Node from linked list
# create linked list
head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

head.next = node2
node2.next = node3
node3.next = node4
tail = node4

# delete node with value 3
node = head
while node:
    if node.val == 3 and node == head:
        head = head.next
        break
    if node.next.val == 3:
        next_node = node.next
        node.next = next_node.next
        break
    node = node.next

# After deletion
_node = head
while _node:
    print(_node.val)
    _node = _node.next
