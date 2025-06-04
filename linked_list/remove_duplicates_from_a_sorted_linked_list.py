# Important | Easy Level
"""
Problem: Remove Duplicates from a Sorted Linked List
Topics: Linked List, Two Pointers
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def deleteDuplicates(self, head):
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

def printList(head):
    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next
    print()

def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

if __name__ == "__main__":
    values = [1, 1, 2, 3, 3]
    head = createLinkedList(values)
    solution = Solution()
    result = solution.deleteDuplicates(head)
    printList(result)
