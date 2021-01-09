#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations.

# Class implements node of linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


_node1 = ListNode(1)
_node2 = ListNode(2)

_node1.next = _node2

# print nodes in linked list
if __name__ == '__main__':
    _node = _node1
    while _node:
        print(_node.val)
        _node = _node.next
