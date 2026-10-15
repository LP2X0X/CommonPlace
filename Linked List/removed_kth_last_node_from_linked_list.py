from node import Node

# OBSERVATION:
# This problem can be solve by answering 2 questions:
# How to remove that Kth node?
# How to find that Kth node?

# How do we remove the Kth last node?
# Example: A --> B --> C. Remove the second till last node
# Intuitively, we could remove B not by pointing at it because then we do not know what would be the one to point to the next one of B (which is A in this case)
# How about, when we get to A, we set A.next = A.next.next (which is C)!
# Now the second question become, how to find that Kth - 1 node

# How to find that Kth - 1 node
# EDGE CASE: If the Kth last node does not exist, then...
# We could use 2 pointers, both start from the head
# If K == 2 then we move the traverse pointer twice. After that, we move both
# If the traverse pointer node.next == null. Then we know we should begin remove the Kth last node
# EDGE CASE: What happen if the head is already the Kth node? Then what node should be Kth - 1 node 
# A --> B --> C where K = 3
# => We could create a dummy node at the front then begin traverse from there
# => This won't break the normal flow since we just moving the pointers

# What do we return? The same head?
# No. dummy.next

# EDGE CASE: K > than number of nodes

def removed_kth_last_node_from_linked_list (head: Node, k: int) -> Node:
    dummy = Node()
    dummy.next = head
    
    anchor = dummy
    traverse = dummy
    
    for _ in range(k):
        traverse = traverse.next
        
        if traverse == None:
            return head
    
    while traverse.next != None:
        anchor = anchor.next
        traverse = traverse.next
    
    anchor.next = anchor.next.next

    # Since head could be remove
    return dummy.next