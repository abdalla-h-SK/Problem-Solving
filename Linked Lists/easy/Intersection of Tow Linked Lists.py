# 160
# my solution -> O(n) Space

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        a_nodes, b_nodes = [], set()
        cur1, cur2 = headA, headB

        while cur1 or cur2:
            if cur1:
                a_nodes.append(cur1)
                cur1 = cur1.next
            
            if cur2:
                b_nodes.add(cur2)
                cur2 = cur2.next
        
        for node in a_nodes:
            if node in b_nodes:
                return node


# my soluiton -> O(1) Space
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        cur1, cur2 = headA, headB
        m = n = 0

        while cur1 or cur2:
            if cur1:
                m += 1
                cur1 = cur1.next
            
            if cur2:
                n += 1
                cur2 = cur2.next
        
        if n < m:
            cur1 = headA
            for i in range(m - n):
                cur1 = cur1.next

            cur2 = headB

        elif n > m:
            cur2 = headB
            for i in range(n - m):
                cur2 = cur2.next

            cur1 = headA
        else:
            cur1 = headA
            cur2 = headB

        for i in range(min(n, m)):
            if cur1 is cur2:
                return cur1
            else:
                cur1 = cur1.next
                cur2 = cur2.next


# another solution -> O(1) Space
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        a, b = headA, headB
        while (a != b):
            a = headB if not a else a.next
            b = headA if not b else b.next
        return a      