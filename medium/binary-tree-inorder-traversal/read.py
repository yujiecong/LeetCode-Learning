# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode):
        # inorder
        if root==None:
            return []
        path=[]
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            path.append(root.val)
            inorder(root.right)
        inorder(root)

        return path
