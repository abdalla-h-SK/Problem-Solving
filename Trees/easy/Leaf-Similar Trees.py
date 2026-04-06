# 872
# my solution ->

#   Time : O(n) , Space : O(n)

class Solution(object):
    def leafSimilar(self, root1, root2):
        leaf_1 = []
        leaf_2 = []

        def get_leaf(node, group):
            if not node:
                return

            if not (node.left or node.right):
                group.append(node.val)

            get_leaf(node.left, group)
            get_leaf(node.right, group)
        
        get_leaf(root1, leaf_1)
        get_leaf(root2, leaf_2)

        return leaf_1 == leaf_2