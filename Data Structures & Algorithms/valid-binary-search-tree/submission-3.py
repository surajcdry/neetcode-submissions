# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.store = []
        self.res = True

        def dfs(root):
            if not root:
                return
            if not self.res:
                return

            dfs(root.left)
            if len(self.store) > 0 and root.val <= self.store[-1]:
                self.res = False
            self.store.append(root.val)

            dfs(root.right)

        dfs(root)
        
        return self.res
