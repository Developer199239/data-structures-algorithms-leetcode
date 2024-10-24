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

        values = set()
        temp = head
        pre_node = None

        while temp:
            if temp.val in values:
                print(f"Duplicate found: {temp.val}")
                pre_node.next = temp.next 
            else:
                print(f"Adding {temp.val} to values set")
                values.add(temp.val)
                pre_node = temp
            temp = temp.next
        
        return head

# Example test
s = Solution()
head = s.create_linked_list([1,1,1,2,3])
s.print_linked_list(head)

result = s.deleteDuplicates(head)
s.print_linked_list(result)
