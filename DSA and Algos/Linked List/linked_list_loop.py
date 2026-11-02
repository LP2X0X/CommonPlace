# Given a singly linked list, determine if it contains a cycle. A cycle occurs if a node's next pointer references an earlier node in the list, causing a loop.
# Example:
# 0 → 1 → 2 → 3 → 4
#         ↑         ↓
#         5 ← ← ← ←
# Output: True

# Brute force way, traverse the linked list, store the node in a hash set, if the same node already exist in the hash set => loop exist

from node import Node

# TIME: O(n)
# SPACE: O(n)
def brute_force_linked_list_loop (head: Node) -> bool:
    nodeSet = set()

    while head.next != None:
        if head.next in nodeSet:
            return True
        nodeSet.add(head)
        head = head.next

    return False 

# Observation: Man I don't think any intuition of me could progress to this solution... 
# We can traverse the list with two pointers, 
# Anyway, imagine if there are two runners. The first one can traverse one node at a time, the second one can traverse two node at a time. If two of the pointers reach the same node at the same time => There is a loop. How?
# Each time both the pointers run, the second one will be one step closer to the first one. Think about it clockwise.
# So unless the linked list is a loop, there is no way for the second pointer to reach the first pointer on the same node.
# The step of each pointer here is also important. The difference between them must be one to guarantee that the second one will catch the first one. If the step different is bigger than the second one might jump through the first.
# Based on this information, the maximum number of step taken if the two pointers are in a loop is n (since each step taken will decrease their node distance by one).

# TIME: O(n)
# Space: O(1)
def linked_list_loop(head: Node) -> bool:
    slowPointer = head
    fastPointer = head

    while fastPointer and fastPointer.next:
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next
        if slowPointer == fastPointer:
            return True

    return False