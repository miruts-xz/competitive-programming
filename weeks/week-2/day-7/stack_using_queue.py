#  Copyright (c) 2021. This code is licensed to mire
#  Copying and / or distributing without appropriate permission from author is
#  illegal and would mount to theft.
#  Please contact developer at miruts.hadush@aait.edu.et prior to
#  copying/distributing to ask and get proper authorizations.

# Implements Stack using two Queues (List with only Queue operations)
class MyStack:
    def __init(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        temp = []
        while not self.empty():
            val = self.stack[0]
            temp.append(val)
            self.stack.remove(val)
        elem = temp.pop()
        while len(temp) > 0:
            val = temp[0]
            self.push(val)
            temp.remove(val)
        return elem

    def top(self) -> int:
        elem = self.pop()
        self.push(elem)
        return elem

    def empty(self) -> bool:
        return len(self.stack) == 0
