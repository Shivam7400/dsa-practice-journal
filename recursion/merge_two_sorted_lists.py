# Importent | Eazy
"""
Problem: Merge Two Sorted Lists
Topics: Linked List, Recursion
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# Solution class with recursive merge function
class Solution:
    # Time Complexity: O(n + m)
    # Space Complexity: O(1)
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

# list1 = ListNode(1)
# list1.next = ListNode(2)
# list1.next.next = ListNode(4)

# list2 = ListNode(1)
# list2.next = ListNode(3)
# list2.next.next = ListNode(4)

# solution = Solution()
# merged_head = solution.mergeTwoLists(list1, list2)

# current = merged_head
# while current:
#     print(current.val, end=" -> " if current.next else "")
#     current = current.next
# print("\n")

def create_linked_list(values):
    dummy = ListNode()
    tail = dummy
    for val in values:
        tail.next = ListNode(val)
        tail = tail.next
    return dummy.next

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()

list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])

solution = Solution()
merged_head = solution.mergeTwoLists(list1, list2)

print_linked_list(merged_head)