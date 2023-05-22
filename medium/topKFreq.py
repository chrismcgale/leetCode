class Solution:
    # Fastest
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        mp = {}
        res = []
        
        for i in nums:
            mp[i] = 1 if i not in mp else mp[i] + 1
        
        
        arr = []
        
        for key in mp.keys():
            arr.append((key, mp[key]))
            
            
        arr.sort(key=lambda x: -x[1])
        
        for i in range(k):
            res.append(arr[i][0])
            
        return res
    
    def simpleTopK(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        count = Counter(nums)
        
        
        return heapq.nlargest(k, count.keys(), key=count.get)
    
    def bucketTopKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for val, freq in cnt.items():
            buckets[freq].append(val)
        
        res = []
        for bucket in reversed(buckets):
            for val in bucket:
                res.append(val)
                k -= 1
                if k == 0:
                    return res