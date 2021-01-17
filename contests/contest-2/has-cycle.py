# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    nodes = []
    n = head
    while n:
        if n in nodes:
            return 1
        nodes.append(n)
        n = n.next
    return 0
