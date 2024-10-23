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

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        low_node = None
        low_head = None
        high_list = None
        high_head = None
        current = head
        
        while current:
            if current.val < x:
                if low_node is None:
                    low_node = ListNode(current.val)
                    low_head = low_node
                else:
                    low_node.next = ListNode(current.val)
                    low_node = low_node.next  
            else:
                if high_list is None:
                    high_list = ListNode(current.val)
                    high_head = high_list
                else:
                    high_list.next = ListNode(current.val)
                    high_list = high_list.next     

            current = current.next

        if low_node:
            low_node.next = high_head 
            return low_head
        else:
            return high_head
  

# Example test
s = Solution()
head = s.create_linked_list([1, 4, 3, 2, 5, 2])
s.print_linked_list(head)

# After implementing partition function, you can test it by:
result = s.partition(head, 3)
s.print_linked_list(result)
