class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        sign = 0
        last = nums[0]
        for i in nums[1:]:
            if sign == 0:
                sign = -1 if i < last else 1 if i > last else 0
            elif sign == 1:
                if i < last:
                    return False
            elif sign == -1:
                if i > last:
                    return False
                
            last = i
        return True