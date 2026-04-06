from collections import deque
class TreeNode:
    pass

class Codec:

    def serialize(self, root):
        if not root:
            return ""

        nodes = []
        bfs_que = deque([root])

        while bfs_que:
            node = bfs_que.popleft()
            if node == "#":
                nodes.append(node)
                continue
            nodes.append(str(node.val))
            
            if node.left:
                bfs_que.append(node.left)
            else:
                bfs_que.append("#")

            if node.right:
                bfs_que.append(node.right)
            else:
                bfs_que.append("#")
                
        return ','.join(nodes)

    def deserialize(self, data):
        data = data.split(',')
        if not data:
            return None
        
        head = None
        curr_order = []
        i = 0

        turn = 1
        for node in data:
            if not head:
                head = TreeNode(node)
                curr = head
                curr_order.append(curr)
                continue
            
            if turn == 1:
                if node != '#':
                    curr.left = TreeNode(node)
                    curr_order.append(curr.left)
                turn = 2
            else:
                if node != '#':
                    curr.right = TreeNode(node)
                    curr_order.append(curr.right)
                turn = 1
            
                if i + 1 == len(curr_order):
                    return head
                curr = curr_order[i+1]
                i += 1