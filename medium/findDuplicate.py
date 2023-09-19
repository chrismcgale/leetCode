class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            cur = abs(num)
            if nums[cur] < 0:
                duplicate = cur
                break
            nums[cur] = -nums[cur]

        # Restore numbers
        for i in range(len(nums)):
            nums[i] = abs(nums[i])

        return duplicate
    
    def findDuplicateMap(self, nums: List[int]) -> int:
        while nums[0] != nums[nums[0]]:
            nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
        return nums[0]
    
    def findDuplicateBits(self, nums: List[int]) -> int:
        duplicate = 0
        n = len(nums) - 1
        bits = n.bit_length()
        for bit in range(bits):
            mask = 1 << bit
            base_count = 0
            nums_count = 0
            for i in range(n + 1):
                # If bit is set in number (i) then add 1 to base_count
                if i & mask:
                    base_count += 1
                    
                # If bit is set in nums[i] then add 1 to nums_count
                if nums[i] & mask:
                    nums_count += 1
                    
            # If the current bit is more frequently set in nums than it is in 
            # the range [1, 2, ..., n] then it must also be set in the duplicate number.
            if nums_count - base_count > 0:
                duplicate |= mask
                
        return duplicate
    
    def findDuplicateCycle(self, nums):
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare