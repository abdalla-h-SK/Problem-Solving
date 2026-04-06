# 61
# we can also reverse all the list then reverse it in [(k % count) , (count - (k % count))] groups

class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head

        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next


        tail = head.next 
        tail.prev = head
        while tail.next:
            temp = tail
            tail = tail.next
            tail.prev = temp
        
        head.prev = tail

        for i in range(k % count):
            tail.next = head
            head = tail
            tail = tail.prev
            tail.next = None

        return head
    
    # Time : O (len(head))
    # Space: O (1)