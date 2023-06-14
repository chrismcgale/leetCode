class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.minDistance = 1e9
        self.prev = None
        
        def inorderTraversal(node):
            if node is None:
                return
            
            inorderTraversal(node.left)
            if self.prev is not None:
                self.minDistance = min(self.minDistance, node.val - self.prev)
            self.prev = node.val
            inorderTraversal(node.right)
            
        inorderTraversal(root)
        return self.minDistance