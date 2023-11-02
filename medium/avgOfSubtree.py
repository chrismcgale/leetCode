class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        # Returns [average, num of nodes in subtree, count]
        def avgRecur(root) -> List[int]:
            if not root:
                return [0, 0, 0]
            
            left = avgRecur(root.left)
            right = avgRecur(root.right)
            
            avg = (left[0] + root.val + right[0]) // (left[1] + 1 + right[1])
            
            return [left[0] + root.val + right[0], left[1] + right[1] + 1, left[2] + right[2] + (1 if root.val == avg else 0)]
        
        return avgRecur(root)[2]