# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fastNode = head
        slowNode = head
        previousNode = None
        for _ in range(n):
            if fastNode:
                fastNode = fastNode.next
            else:
                return None
            
        if not fastNode:
            return head.next
    
        while fastNode:
            previousNode = slowNode
            slowNode = slowNode.next
            fastNode = fastNode.next

            
        previousNode.next = slowNode.next
        slowNode = None
        return head

# Helper functions
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test function to test removeNthFromEnd
def test_solution():
    solution = Solution()

    # Test case 1
    head = create_linked_list([1, 2, 3, 4, 5])
    n = 2
    modified_head = solution.removeNthFromEnd(head, n)
    print(linked_list_to_list(modified_head))  # Expected output: [1, 2, 3, 5]

    # Test case 2
    head = create_linked_list([1])
    n = 1
    modified_head = solution.removeNthFromEnd(head, n)
    print(linked_list_to_list(modified_head))  # Expected output: []

    # Test case 3
    head = create_linked_list([1, 2])
    n = 1
    modified_head = solution.removeNthFromEnd(head, n)
    print(linked_list_to_list(modified_head))  # Expected output: [1]

# Run tests
test_solution()
