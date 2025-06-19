'''
82. Remove Duplicates from Sorted List II
Solved

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
'''
#SOLUTION



from collections import Counter
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        freq=Counter()
        curr=head
        while curr:
            freq[curr.val]+=1
            curr=curr.next
        dummy=ListNode(0)
        curr=dummy
        while head:
            if freq[head.val]==1:
                curr.next=ListNode(head.val)
                curr=curr.next
            head=head.next
        return dummy.next
        
'''
curr.val	freq After Adding
1	{1: 1}
2	{1: 1, 2: 1}
3	{1: 1, 2: 1, 3: 1}
3	{1: 1, 2: 1, 3: 2}
4	{1: 1, 2: 1, 3: 2, 4: 1}
4	{1: 1, 2: 1, 3: 2, 4: 2}
5	{1: 1, 2: 1, 3: 2, 4: 2, 5: 1}

 if freq[head.val] == 1:
        curr.next = ListNode(head.val)
        curr = curr.next


1st node = 1 → frequency = 1 
2nd node = 2 → frequency = 1
3rd node = 3 → frequency = 2
4th node = 3 → frequency = 2
5th node = 4 → frequency = 2
6th node = 4 → frequency = 2
7th node = 5 → frequency = 1

1 → 2 → 5

'''