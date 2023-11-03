class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        curr = 1
        for i in target:
            res.append("Push")
            while curr < i:
                res.append("Pop")
                res.append("Push")
                curr += 1
                
            curr += 1
                
        return res