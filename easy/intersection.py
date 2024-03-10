class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = {}
        ans = []
        
        for i in nums1:
            seen[i] = 1
            
        for i in nums2:
            if i in seen and seen[i] == 1:
                ans.append(i)
                seen[i] = 0
                
        return ans
                