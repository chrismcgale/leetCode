class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mid = (len(nums1) + len(nums2)) // 2
        
        merge = []
        
        p1, p2 = 0, 0
        
        while p1 + p2 < mid + 1:
            if p1 < len(nums1) and p2 < len(nums2):
                if nums1[p1] < nums2[p2]:
                    merge.append(nums1[p1])
                    p1 += 1
                else:
                    merge.append(nums2[p2])
                    p2 += 1
            elif p1 < len(nums1):
                merge.append(nums1[p1])
                p1 += 1
            else:
                merge.append(nums2[p2])
                p2 += 1

        if (len(nums1) + len(nums2)) % 2 == 0:
            return (merge[mid - 1] + merge[mid]) / 2
        return merge[mid]
    
    def findMedianSortedArraysBinarySearch(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)


        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            partitionA = (left + right) // 2
            partitionB = (m + n + 1) // 2 - partitionA

            maxLeftA = float('-inf') if partitionA == 0 else nums1[partitionA - 1]
            minRightA = float('inf') if partitionA == m else nums1[partitionA]
            maxLeftB = float('-inf') if partitionB == 0 else nums2[partitionB - 1]
            minRightB = float('inf') if partitionB == n else nums2[partitionB]

            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if (m + n) % 2 == 0:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
                else:
                    return max(maxLeftA, maxLeftB)
            elif maxLeftA > minRightB:
                right = partitionA - 1
            else:
                left = partitionA + 1