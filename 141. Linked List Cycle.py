from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False

#Helper
def create_linked_list_with_cycle(values, pos):
    head = ListNode(values[0])
    current = head
    cycle_node = None
    
    if pos == 0:
        cycle_node = head
    
    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
        if i == pos:
            cycle_node = current
    
    if pos != -1:
        current.next = cycle_node
    
    return head

# test cases
solution = Solution()

head1 = create_linked_list_with_cycle([3, 2, 0, -4], 1)
print(solution.hasCycle(head1)) #True

head2 = create_linked_list_with_cycle([1, 2], 0)
print(solution.hasCycle(head2))  #True


head3 = create_linked_list_with_cycle([1], -1)
print(solution.hasCycle(head3))  # False

head4 = create_linked_list_with_cycle([1, 2, 3, 4], -1)
print(solution.hasCycle(head4))  # False
