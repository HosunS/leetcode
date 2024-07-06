# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = 0
        temp = head
        while temp:
            counter += 1
            temp = temp.next
        
        if counter == 2:
            head.next = None
            return head
        if counter == 1:
            head = None
            return head

        mid = counter//2
        temp2= head
        for _ in range(mid - 1):
            temp2 = temp2.next
        
        temp3 = temp2.next
        temp2.next = temp3.next

        return head
