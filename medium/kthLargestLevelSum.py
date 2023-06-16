class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
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
                
        level_sums.sort()
        
        return -1 if k > len(level_sums) else level_sums[-1 * k]