class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_sums = []
        queue = [(root, 0)]
        
        while queue:
            node, level = queue.pop()
            if len(level_sums) > level:
                level_sums[level] += node.val
            else:
                level_sums.append(node.val)
            
            if node.left:
                queue.append((node.left, level + 1))
                
            if node.right:
                queue.append((node.right, level + 1))
                
        return level_sums.index(max(level_sums)) + 1