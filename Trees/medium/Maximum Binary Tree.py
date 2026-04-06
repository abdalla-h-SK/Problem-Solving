# 654
# my solution ->

class TreeNode:
    pass

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        n = len(nums)
        def construct(l, r):
            if l == r:
                return None
            
            j = nums.index(max(nums[l:r]))
            node = TreeNode(nums[j])

            node.left = construct(l, j)
            node.right = construct(j+1, r)

            return node
        
        return construct(0, n)