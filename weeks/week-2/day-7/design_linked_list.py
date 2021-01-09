#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations.

# Class implements node of linked list
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


node1 = Node(1)
node2 = Node(2)

node1.next = node2

# print nodes in linked list
node = node1
while node:
    print(node.val)
    node = node.next
