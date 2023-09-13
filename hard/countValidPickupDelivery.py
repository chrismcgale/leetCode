class Solution:
    def countOrders(self, n: int) -> int:
        mod = 10 ** 9 + 7
        
        return (math.factorial(n) * math.prod([2 * i - 1 for i in range(1, n + 1)])) % mod