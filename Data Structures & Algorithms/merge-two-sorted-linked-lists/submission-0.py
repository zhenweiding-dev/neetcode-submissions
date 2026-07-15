# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None

        dummy = node = ListNode()

        temp1, temp2 = list1, list2
        while temp1 and temp2:
            if temp1.val <= temp2.val:
                node.next = temp1
                temp1 = temp1.next
            else:
                node.next = temp2
                temp2 = temp2.next
            node = node.next
        
        node.next = temp1 or temp2

        return dummy.next

