# 257

#   Time : O (n)
#   Space: O (h)

class Solution(object):
    def binaryTreePaths(self, root):
        def dfs(node, curr_path, paths):
            if not node:
                return 
            
            curr_path += str(node.val)
            if not node.left and not node.right:
                paths.append(curr_path)
            else:
                curr_path += "->"
                if node.left:
                    dfs(node.left, curr_path, paths)
                if node.right:
                    dfs(node.right, curr_path, paths)
        
        paths = []
        dfs(root, "", paths)
        return paths