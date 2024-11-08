# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        ptr1 = list1
        ptr2 = list2
    
        dummy = ListNode()
        ans = dummy

        while ptr1 != None and ptr2 != None:

            if ptr1.val <= ptr2.val:

                temp = ptr1.next
                dummy.next = ptr1
                ptr1.next = None
                ptr1 = temp
                dummy = dummy.next 
            else:

                temp = ptr2.next
                dummy.next = ptr2
                ptr2.next = None
                ptr2 = temp
                dummy = dummy.next

        if ptr2 != None:

            dummy.next = ptr2
        else:
            dummy.next = ptr1

        return ans.next

        