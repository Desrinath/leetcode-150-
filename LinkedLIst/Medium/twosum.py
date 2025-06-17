'''
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''
#SOLUTION

def addTwoNumbers(self, l1, l2):
    dummy=ListNode()
    c=dummy
    carry=0

    while l1 or l2 or carry :
        if l1:
            val1=l1.val 
        else:
             val1=0
        if l2:
            val2=l2.val
        else:
            val2=0

        total=val1+val2+carry

        digit=total%10
        carry=total//10

        c.next=ListNode(digit)
        c=c.next

        if l1:
            l1=l1.next
        if l2:
            l2=l2.next

    return dummy.next
'''
STEP1

List1: [2] → [4] → [3] → None
List2: [5] → [6] → [4] → None

dummy → [ ] → None
curr  → dummy
carry = 0

STEP2

val1 = 2     (l1.val)
val2 = 5     (l2.val)
carry = 0

total = val1 + val2 + carry = 2 + 5 + 0 = 7
digit = total % 10 = 7
carry = total // 10 = 0

dummy → [7] → None
           ↑
         curr


STEP3

val1 = 4
val2 = 6
carry = 0

total = 4 + 6 + 0 = 10
digit = 0
carry = 1

dummy → [7] → [0] → None
                 ↑
               curr

STEP4

val1 = 3
val2 = 4
carry = 1

total = 3 + 4 + 1 = 8
digit = 8
carry = 0

dummy → [7] → [0] → [8] → None
                          ↑
                        curr

'''