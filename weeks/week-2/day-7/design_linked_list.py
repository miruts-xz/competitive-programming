class Node:
    def __init__(self, val=int, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        count = self.count()
        if index > count - 1:
            return -1
        node = self.head
        for i in range(index):
            node = node.next
        return node.val

    def count(self):
        count = 0
        head = self.head
        while head:
            count += 1
            head = head.next
        return count

    def addAtHead(self, val: int) -> None:
        self.head = Node(val, self.head)

    def addAtTail(self, val: int) -> None:
        node = self.head
        if node is None:
            self.head = Node(val)
            return
        while node.next:
            node = node.next
        node.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        node = self.head
        i = 0
        if node is None:
            self.head = Node(val)
            return
        if index == 0:
            return self.addAtHead(val)
        elif index == self.count():
            return self.addAtTail(val)
        for i in range(index - 1):
            node = node.next
        node.next = Node(val, node.next)

    def deleteAtIndex(self, index: int) -> None:
        node = self.head
        if node is None:
            return
        elif index >= self.count():
            return
        elif index == 0:
            self.head = self.head.next
            return
        for i in range(index - 1):
            node = node.next
        new_node = node.next
        if new_node.next is None:
            node.next = None
        else:
            node.next = new_node.next


ll = MyLinkedList()

ll.addAtHead(1)
print(ll.get(0))
