# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head 

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        for _ in range(left - 1):
            pre = pre.next

        current = pre.next
        pre_node = None
        for _ in range(right - left + 1):
            next_node = current.next
            current.next = pre_node
            pre_node = current
            current = next_node
            # print(f"current value: {current.val}")
            # print(f"pre value: {pre.val}")
            

        # print(f"current value: {current.val}")
        # print(f"pre value: {pre.val}")
        # print(f"pre value: {pre.next.val}")
        # Connect the end of the reversed part to the next part
        pre.next.next = current 
        # Connect the beginning of the reversed part
        pre.next = pre_node 

        return dummy.next
        