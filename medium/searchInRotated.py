class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        
        while lo <= hi:
            m = lo + (hi - lo) // 2
            
            # target found
            if nums[m] == target:
                return m
            
            # subarray on mid's left is sorted
            elif nums[m] >= nums[lo]:  
                if nums[lo] <= target < nums[m]:
                    hi = m - 1
                else:
                    lo = m + 1
            # subarray on mid's right is sorted
            else:
                if nums[m] < target <= nums[hi]:
                    lo = m + 1
                else:
                    hi = m - 1
        
        return -1