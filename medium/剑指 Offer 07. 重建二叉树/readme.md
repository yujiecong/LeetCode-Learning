#### [剑指 Offer 07. 重建二叉树](https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/)

输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

 

例如，给出

```
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
```

返回如下的二叉树：

```
    3
   / \
  9  20
    /  \
   15   7
```

 

**限制：**

```
0 <= 节点个数 <= 5000
```

 

这题我是不能直接做的,因为我对这些不是很熟

那么只能慢慢来了



我们知道前序遍历 的根节点在一开始的,我们可以知道直接获取根节点的值

然后中序遍历 的话 左结点 根结点 右结点的顺序

所以在根结点左边n个结点都是左子树 位于 根结点右边的都是右子树结点

可以发现是递归找到的

那么每一次 都找到 左右子树 和 根节点即可



一个小时,泪目,终于做出来了

```
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
```

![1618123082299](readme.assets/1618123082299.png)