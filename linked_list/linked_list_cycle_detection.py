# Medium Level
"""
Problem: Linked List Cycle Detection
Algorithm: Floyd's Cycle Detection (Tortoise & Hare)
Topics: Linked List, Two Pointers
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedListBuilder:
    @staticmethod
    def build_linked_list(values: list[int], pos: int = -1) -> ListNode:
        """
        Builds a linked list from a list of values.
        If pos >= 0, creates a cycle connecting the tail to the node at index 'pos'.
        """
        if not values:
            return None

        head = ListNode(values[0])
        current = head
        cycle_node = None

        for i in range(1, len(values)):
            current.next = ListNode(values[i])
            current = current.next
            if i == pos:
                cycle_node = current

        if pos == 0:
            cycle_node = head
        if pos != -1:
            current.next = cycle_node

        return head

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

if __name__ == "__main__":
    head = LinkedListBuilder.build_linked_list([3, 2, 0, -4], pos=1)
    
    obj = Solution()
    print("Has cycle:", obj.hasCycle(head))
