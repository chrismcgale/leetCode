class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left, right = 1 + self.minDepth(root.left), 1 + self.minDepth(root.right)
        
        if (left == 1) != (right == 1):
            return max(left, right)
        
        return min(left, right)
    
    def minDepthBfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        que = [root]
        level = 0

        while que:
            level = level + 1
            for _ in range(len(que)):
                node = que.pop(0)
                if not node.left and not node.right:
                    return level
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)