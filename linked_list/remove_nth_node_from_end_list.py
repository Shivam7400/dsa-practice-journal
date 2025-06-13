"""
Problem: Remove Nth Node From End of List
Algorithm: Two Pointers
Topics: Linked List, Two Pointers
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedListBuilder:
    @staticmethod
    def build_linked_list(values: list[int]) -> ListNode:
        if not values:
            return None

        head = ListNode(values[0])
        current = head

        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next

        return head

    @staticmethod
    def print_linked_list(head: ListNode) -> None:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        print("->".join(map(str, values)))

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = second = dummy

        for _ in range(n + 1):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next

if __name__ == "__main__":
    head = LinkedListBuilder.build_linked_list([1, 2, 3, 4, 5])
    n = 2

    obj = Solution()
    new_head = obj.removeNthFromEnd(head, n)

    print("Updated list after removing", n, "th node from the end:")
    LinkedListBuilder.print_linked_list(new_head)
