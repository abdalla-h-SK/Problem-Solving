# 572
# my solution ->

#   Time : O(m * n)
#   Space: O(m + n)

class Solution(object):
    def isSubtree(self, root, subRoot):
        isSub = [False]

        def same(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False
            
            if(p.val != q.val):
                return False
            
            return same(p.left, q.left) and same(p.right, q.right)

        def seek(root, subRoot):
            curr = root
            if not curr:
                return
            
            if curr.val == subRoot.val:
                if same(curr, subRoot):
                    isSub[0] = True
                    return
            
            seek(curr.left, subRoot)
            if isSub[0] == True:
                return
            seek(curr.right, subRoot)
        
        seek(root, subRoot)
        
        return isSub[0]