"""
LeetCode [141]: Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Approach:
Use the two-pointer technique with a fast pointer and a slow pointer.
Initialize both pointers to the head of the linked list.
Move the fast pointer by two steps and the slow pointer by one step in each iteration.
If the fast pointer catches up with the slow pointer at any point, there is a cycle in the linked list.

Code with Comments:
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize both pointers to the head of the linked list
        fast = head
        slow = head
        
        # Iterate through the linked list using the two-pointer technique
        while fast and fast.next:
            # Move the fast pointer by two steps and the slow pointer by one step
            fast = fast.next.next
            slow = slow.next
            
            # If the fast pointer catches up with the slow pointer, there is a cycle
            if fast == slow:
                return True
        
        # If the loop completes without detecting a cycle, return False
        return False
