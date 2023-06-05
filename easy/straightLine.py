class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        last = False
        n = len(coordinates)
        for i in range(n - 1):
            c1, c2 = coordinates[i], coordinates[i + 1]
            slope = sys.maxsize if c1[0] == c2[0] else (c2[1] - c1[1]) / (c2[0] - c1[0])

            if last != False and last != slope:
                return False
            
            last = slope
            
        return True