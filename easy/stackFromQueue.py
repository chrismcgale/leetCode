class MyStack:

    def __init__(self):
        self.q1, self.q2 = [], []
        self.first = True
        

    def push(self, x: int) -> None:
        if self.first:
            self.q1.append(x)
        else:
            self.q2.append(x)
        

    def pop(self) -> int:
        res = 0
        if self.first:
            while len(self.q1) > 1:
                self.q2.append(self.q1.pop(0))
            res = self.q1[0]
            self.q1 = []
        else:
            while len(self.q2) > 1:
                self.q1.append(self.q2.pop(0))
            res = self.q2[0]
            self.q2 = []
            
        self.first = not self.first
        return res

    def top(self) -> int:
        res = 0
        if self.first:
            while len(self.q1) > 1:
                self.q2.append(self.q1.pop(0))
            res = self.q1[0]
            self.q2.append(self.q1.pop(0))
        else:
            while len(self.q2) > 1:
                self.q1.append(self.q2.pop(0))
            res = self.q2[0]
            self.q1.append(self.q2.pop(0))
            
        self.first = not self.first
        return res
        

    def empty(self) -> bool:
        if self.first:
            return len(self.q1) == 0
        else:
            return len(self.q2) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()