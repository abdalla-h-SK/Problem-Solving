# 101
# my solution ->

#   Time : O(n)
#   Space: O(n)

class Solution(object):
    def isSymmetric(self, root):
        flag = [True]

        def same(p, q):
            if (p and not q) or (q and not p):
                flag[0] = False
                return
            elif not p and not q:
                return
            if(p.val != q.val):
                flag[0] = False
                return
            
            same(p.left, q.right)
            if flag[0] == False:
                return
            same(p.right, q.left)

        same(root.left, root.right)

        return flag[0]
    
# another solution ->

class Solution(object):
    def isSymmetric(self, root):
        def same(p, q):
            if not p and not q:
                return True

            elif not p or not q:
                return False

            if(p.val != q.val):
                return False

            return same(p.left, q.right) and same(p.right, q.left)
        
        return same(root.left, root.right)