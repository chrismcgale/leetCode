class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        
        for n in nums:
            count[n] = count.get(n, 0) + 1

        for key, val in count.items():
            if val == 1:
                return key