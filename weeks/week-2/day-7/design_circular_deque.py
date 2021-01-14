class Node:
    def __init__(self, value: int = 0, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class MyCircularDeque:
    def __init__(self, k: int):
        self.k = k
        self.count = 0
        self.head = None
        self.tail = None

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
            self.count += 1
            return True
        prev_head = self.head
        self.head = Node(value, next=prev_head)
        prev_head.prev = self.head
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
            self.count += 1
            return True
        self.tail.next = Node(value, self.tail)
        self.tail = self.tail.next
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if not self.head:
            return False
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if not self.head:
            return False
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self.count -= 1
        return True

    def getFront(self) -> int:
        if not self.head:
            return -1
        return self.head.value

    def getRear(self) -> int:
        if not self.head:
            return -1
        return self.tail.value

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k
