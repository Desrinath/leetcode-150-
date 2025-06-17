'''
92. Reverse Linked List II

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
 

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
 

Follow up: Could you do it in one pass?
'''
#Solution

def reverseBetween(self, head, left, right):
    arr=[]
    while head:
        arr.appeand(head.val)
        head=head.next
    arr[left-1:right]=arr[left-1:right][::-1]

    dummy=ListNode(-1)
    c=dummy

    for val in arr:
        c.next=ListNode(val)
        c=c.next
    return dummy.head

'''
convert linked list into arr
head → 1 → 2 → 3 → 4 → 5 → None

arr = [1, 2, 3, 4, 5]

arr[left-1:right] = arr[left-1:right][::-1]
arr[1:4] = arr[1:4][::-1]

Before:
arr = [1, 2, 3, 4, 5]
            ↑ ↑ ↑
         index 1 to 3
         subarray = [2, 3, 4]
arr[1:4] = [4, 3, 2]

After:
arr = [1, 4, 3, 2, 5]

arr to linked list with the help of Dummy

[1 → 4 → 3 → 2 → 5 → None]

'''