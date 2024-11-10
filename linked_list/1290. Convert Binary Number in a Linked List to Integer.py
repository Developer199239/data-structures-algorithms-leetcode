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

    # def getDecimalValue(self, head: Optional[ListNode]) -> int:
    #     decimal_number = 0
    #     decimal_array = []
    #     while head:
    #         decimal_array.append(head.val)
    #         head = head.next

    #     length = len(decimal_array)
    #     for i in range(length):
    #         decimal_number = decimal_number + decimal_array[length - i -1] * pow(2,i)    
    #     return decimal_number
    
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        decimal_number = 0
        while head:
            decimal_number = decimal_number*2 + head.val
            head = head.next  
        return decimal_number

# Example test
s = Solution()
head = s.create_linked_list([1,1,0])

result = s.getDecimalValue(head)
print(result)
