# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
from typing import List, Optional

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        
        def helper(n):
            if n == 1:
                return [TreeNode(0)]
            trees = []
            for i in range(1, n, 2):
                left_trees = helper(i)
                right_trees = helper(n - 1 - i)
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        trees.append(root)
            return trees
        
        return helper(n)