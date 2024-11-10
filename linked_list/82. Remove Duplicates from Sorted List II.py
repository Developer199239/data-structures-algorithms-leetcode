from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def create_linked_list(self, arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def print_linked_list(self, head):
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        print(values)

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy_node = ListNode(0)
        dummy_node.next = head

        pre_node = dummy_node
        current_node = head

        while current_node:
            if current_node.next and current_node.val == current_node.next.val:
                while current_node.next and current_node.val == current_node.next.val:
                    current_node = current_node.next
                pre_node.next = current_node.next

            else:
                pre_node =  pre_node.next

            current_node = current_node.next 

        return dummy_node.next               
                           
  

# Example test
s = Solution()
head = s.create_linked_list([1,1,1,2,3])
s.print_linked_list(head)

result = s.deleteDuplicates(head)
s.print_linked_list(result)
