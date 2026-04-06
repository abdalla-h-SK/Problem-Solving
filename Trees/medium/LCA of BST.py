# 235
# my solution ->

#   Time : O(n)
#   Space: O(1)

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        ans = None
        curr1, curr2 = root, root

        while True:
            if curr1.val == p.val and curr2.val == q.val:
                return ans

            if curr1.val == curr2.val:
                ans = curr1

            if curr1.val == p.val:
                pass
            elif curr1.val > p.val:
                curr1 = curr1.left
            else:
                curr1 = curr1.right

            if curr2.val == q.val:
                pass
            elif curr2.val > q.val:
                curr2 = curr2.left
            else:
                curr2 = curr2.right


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        lca = [root]

        def search(root):
            if not root:
                return

            lca[0] = root
            if root is p or root is q:
                return
            elif root.val < p.val and root.val < q.val:
                search(root.right)
            elif root.val > p.val and root.val > q.val:
                search(root.left)
            else:
                return

        search(root)
        return lca[0]

# Time Complexity: O(h) { here "h" is the height of the binary search tree }
# Space Complexity: O(h) { here "h" is the height of the binary search tree }
