# 25

# my solution ->

#   Time : O(n)
#   Space: O(n)

class Solution(object):
    def reverseKGroup(self, head, k):
        if k == 1:
            return head
        
        stack, left_nodes_head = self.prepare(head, k)

        inner_head = stack.pop()
        temp = inner_head
        count = 1

        while stack:
            temp.next = stack.pop()
            temp = temp.next
            count += 1

            if count == k:
                temp.next = left_nodes_head
                left_nodes_head = inner_head

                if stack:
                    inner_head = stack.pop()
                    temp = inner_head
                    count = 1

        head = left_nodes_head
        return head

    def prepare(self, head, k):
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        stack = []

        curr = head
        while len(stack) // k != count // k:
            stack.append(curr)
            curr = curr.next

        left_nodes_head = curr
        
        return stack, left_nodes_head