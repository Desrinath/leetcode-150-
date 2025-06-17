'''
141. Linked List Cycle


Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
'''

    #🐢🐇 Floyd’s Cycle Detection 

def cycle(self):
        slow=self.head
        fast=self.head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                print("yes cycle")           # Cycle found

        print("No Cycle") 
    

'''
slow
fast
HEAD → [1] → [2] → [3] → [4] 
               ↑         ↓
               ←←←←←←←←←←
slow = [1]
fast = [1]

slow = [2]
fast = [3]

slow = [3]
fast = [2]

slow = [4]
fast = [4] → Both pointers met 🎯

'''