class MinStack:
    def __init__(self):
        self.items = []

    def push(self, value: int) -> None:
        if not self.items:
            self.items.append([value, value])
        else:
            current_min = self.items[-1][1]
            self.items.append([value, min(current_min, value)])

    def pop(self) -> None:
        self.items.pop()

    def top(self) -> int:
        return self.items[-1][0]

    def getMin(self) -> int:
        return self.items[-1][1]