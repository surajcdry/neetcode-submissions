# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        deq = collections.deque()

        def bfs(root):
            if not root:
                return

            deq.append(root)

            while len(deq) > 0:
                temp = []

                for i in range(len(deq)):
                    curr = deq.popleft()
                    temp.append(curr.val)

                    if curr.left:
                        deq.append(curr.left)

                    if curr.right:
                        deq.append(curr.right)

                res.append(temp[-1])

        bfs(root)

        return res
