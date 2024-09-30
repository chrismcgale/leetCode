class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.container = [0] * maxSize
        self.length = 0

    def push(self, x: int) -> None:
        if self.length < self.maxSize:
            self.container[self.length] = x
            self.length += 1
        

    def pop(self) -> int:
        if self.length == 0:
            return -1
        self.length -= 1
        return self.container[self.length]
        

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.length)):
            self.container[i] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)