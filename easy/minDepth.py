class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left, right = 1 + self.minDepth(root.left), 1 + self.minDepth(root.right)
        
        if (left == 1) != (right == 1):
            return max(left, right)
        
        return min(left, right)