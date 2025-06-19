'''
61. Rotate List

Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 
'''    


def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k==0:
            return head
        l=1
        tail=head
        while tail.next:
            tail=tail.next
            l+=1

        tail.next=head

        k=k%l
        steps=l-k

        new_tail=head


        for _ in range(steps-1):
            new_tail=new_tail.next
        new_head=new_tail.next
        new_tail.next=None

        return new_head
'''
1 → 2 → 3 → 4 → 5 → None

1 → 2 → 3 → 4 → 5
↑               ↓
└──────←───────┘

1 → 2 → 3 ║ 4 → 5 → (back to 1)
                ↑         ↓
              new_head ←──┘

4 → 5 → 1 → 2 → 3 → None

'''