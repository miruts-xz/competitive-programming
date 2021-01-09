#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations.
from design_linked_list import Node


# Method implements reversing linked list
def reverse_linked_list(head: Node) -> Node:
    node_list = []
    node = head
    while node:
        node_list.append(Node(node.val))
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


# Create linked list
head = Node()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4

node = head
# Before reversal
if __name__ == '__main__':
    print('Before')
    while node:
        print(node.val)
        node = node.next

node = reverse_linked_list(head)
# After reversal
if __name__ == '__main__':
    print('After')
    while node:
        print(node.val)
        node = node.next
