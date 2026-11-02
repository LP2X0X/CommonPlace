# Intuition, iterate list to find the length of it, then travel the linked list again to find the middle node (n/2) 

# Observation
# Based on the above info, using a fast pointer and a slow pointer we can do the same. Since the faster pointer move 2 node instead of one, its traverse length will be twice of the slow pointer => The slow pointer will be at middle node when fast poitner reach the end of the list

# Example: a -> b -> c -> d -> e (odd)
# F at c, S at b -> F at e, S at c -> F at null, S at c => Stop when F.next = null

# Example: a -> b -> c -> d (even)
# F at c, S at b -> F at null, S at c => Stop when F.next != null but F.next.next = null 

from node import Node

# TIME: O(n)
# SPACE: O(1)
def linked_list_mid (head: Node) -> Node:
    slowPtr = head  
    fastPtr = head  
    
    # If you need the first middle node in even case
    while fastPtr.next or fastPtr.next.next:
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next.next
        
    # If you need the second middle node in even case
    # while fastPtr or fastPtr.next: 
    #     slowPtr = slowPtr.next
    #     fastPtr = fastPtr.next.next
        
    return slowPtr