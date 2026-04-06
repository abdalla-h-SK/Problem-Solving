# 105
# my solution -> small fixes ChatGpt!

class TreeNode:
    pass

class Solution(object):
    def buildTree(self, preorder, inorder):
        self.i = 0
        n = len(inorder)
        def divide(l, r):
            if l == r:
                return None

            j = inorder.index(preorder[self.i])
            node = TreeNode(preorder[self.i])
            self.i += 1

            node.left = divide(l, j)
            node.right = divide(j+1, r)
            
            return node

        return divide(0, n)