# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):

        def ConstructTree(pre,ino):
            if len(pre)<1 or len(ino)<1:
                return None
            #此时的根节点
            root=pre[0]
            rootTree=TreeNode(root)
            #此时的左子树是
            leftIn=ino[:ino.index(root)]
            leftPre=pre[1:len(leftIn)+1]
            # print(leftPre,leftIn)

            rootTree.left=ConstructTree(leftPre,leftIn)
            #此时的右子树
            rightIn=ino[ino.index(root)+1:]
            rightPre=pre[-len(rightIn):]
            # print(rightPre,rightIn)

            rootTree.right=ConstructTree(rightPre, rightIn)

            return rootTree
        treeHead=ConstructTree(preorder,inorder)
        return treeHead
        # print(treeHead)
        # def pre(head:TreeNode):
        #     if head:
        #         print(head.val)
        #         pre(head.left)
        #         pre(head.right)
        # pre(treeHead)


Solution().buildTree([3,9,20,15,7],[9,3,15,20,7])