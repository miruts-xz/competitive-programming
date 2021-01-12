#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations.

# Implements Stack using two Queues (List with only Queue operations)
from design_linked_list import LinkedList as Queue


class MyStack:
    def __init__(self):
        self.stack = Queue()

    def push(self, x: int) -> None:
        self.stack.addAtTail(x)

    def pop(self) -> int:
        temp = Queue()
        while not self.empty():
            val = self.stack.get(0)
            temp.addAtTail(val)
            self.stack.deleteAtIndex(0)
        elem = temp.get(temp.count()-1)
        while temp.count() > 1:
            val = temp.get(0)
            self.push(val)
            temp.deleteAtIndex(0)
        return elem

    def top(self) -> int:
        elem = self.pop()
        self.push(elem)
        return elem

    def empty(self) -> bool:
        return self.stack.count() == 0


s = MyStack()
s.push(1)
s.push(2)
s.push(3)
s.push(0)
print(s.pop())
print(s.pop())
print(s.top())
