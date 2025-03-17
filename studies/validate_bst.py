# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node, lowerbound, upperbound):
            if node.val <= lowerbound or node.val >= upperbound:
                return False
            if node.left and not check(node.left, lowerbound, node.val):
                return False
            if node.right and not check(node.right, node.val, upperbound):
                return False
            return True
        return check(root, -9999999999, 9999999999)