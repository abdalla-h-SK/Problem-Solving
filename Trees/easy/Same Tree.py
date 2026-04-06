# 100
# my solution ->

#   Time : O(n)
#   Space: O(n)

class Solution(object):
    def isSameTree(self, p, q):
        flag = [True]

        def same(p,q):
            if (p and not q) or (q and not p):
                flag[0] = False
                return
            elif not p and not q:
                return

            if p.val != q.val:
                flag[0] = False
                return
            
            same(p.left, q.left)
            if flag[0] == False:
                return
            same(p.right, q.right)
            
        same(p,q)

        return flag[0]