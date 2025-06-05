# Important | Medium Level
"""
Problem: Reverse a Linked List
Topics: Linked List, Iteration, Recursion
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1) (iterative), O(n) (recursive due to call stack)

    def reverseListIterative(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def reverseListRecursive(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        new_head = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None
        return new_head

def return_linked_list(head: ListNode):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return "->".join(map(str, res))

def build_linked_list(values: list[int]) -> ListNode:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

if __name__ == "__main__":
    node = build_linked_list([1, 2, 3, 4, 5])

    sol = Solution()
    print(f"Original List: {return_linked_list(node)}")
    reversed_iterative = sol.reverseListIterative(node)
    print(f"Reversed List (Iterative): {return_linked_list(reversed_iterative)}")
    reversed_recursive = sol.reverseListRecursive(reversed_iterative)
    print(f"Reversed Again (Recursive): {return_linked_list(reversed_recursive)}")
