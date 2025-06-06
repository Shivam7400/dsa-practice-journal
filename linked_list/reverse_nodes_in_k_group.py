# Important | Hard Level
"""
Problem: Reverse Nodes in k-Group
Topics: Linked List, Recursion, Iteration
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1) (excluding recursion stack)

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count = 0
        ptr = head

        # Check if there are at least k nodes left
        while ptr and count < k:
            ptr = ptr.next
            count += 1
        
        if count < k:
            return head

        # Reverse k nodes
        prev = None
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Recursively call for the rest of the list
        if curr:
            head.next = self.reverseKGroup(curr, k)

        return prev

def return_linked_list(head: ListNode):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    return " -> ".join(res)

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

    k = 3
    reversed_group = sol.reverseKGroup(node, k)
    print(f"Reversed in Groups of {k}: {return_linked_list(reversed_group)}")
    
