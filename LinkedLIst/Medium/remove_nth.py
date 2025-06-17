'''
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
'''



def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        c=0
        curr=head
        while curr:
            c+=1
            curr=curr.next
        
        curr=head

        if(c==n):
            return head.next
        for _ in range(c-n-1):
            curr=curr.next
        curr.next=curr.next.next

        return head