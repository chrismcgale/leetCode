class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr, m = 0, 0
        for i in gain:
            curr += i
            m = max(m, curr)
        return m