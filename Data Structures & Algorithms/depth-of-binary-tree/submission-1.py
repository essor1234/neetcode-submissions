# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # create a queue
        q = deque()

        if root:
            q.append(root)

        level = 0

        while q:
            for i in range(len(q)):
                # pop the first left node(old one)
                node = q.popleft()
                # Add new node on left and right
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)

            level += 1

        return level