class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 0
        
        for k, v in count.items():
            ans += comb(v, 2)
            
        return ans