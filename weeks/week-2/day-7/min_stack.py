class MinStack:
    def __init__(self):
        self.s = []

    def push(self, x: int) -> None:
        if self.s:
            prev_min = self.s[-1][1]
            self.s.append((x, min(x, prev_min)))
            return
        self.s.append((x, x))

    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        return self.s[-1][0]

    def getMin(self) -> int:
        return self.s[-1][1]
