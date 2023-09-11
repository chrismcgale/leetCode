class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res = []
        
        groups = [[] for _ in range(len(groupSizes) + 1)]
        
        for i, size in enumerate(groupSizes):
            groups[size].append(i)
            
            if len(groups[size]) == size:
                res.append(groups[size])
                groups[size] = []
                
            
        return res