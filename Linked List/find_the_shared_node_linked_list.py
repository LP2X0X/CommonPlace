from node import Node

# Problem: Return the node where two linked list intersect
# 1 -> 2 -> 3 \
#               -> (C) -> D -> E
#      A -> B /

# Intuition, we can use hash map for this. Traverse the first linked list, map it then traverse the second list. If any node exist before in the hash map then its the shared node we are looking for.

# OBSERVATION: 
# Imagine If the 2 linked list of the same length, we could just traverse them and compare the node simultaneously. If they are the same, then that node is the shared node.
# But, what happen when the linked list is not of same length?
# Well since 1 + 2 = 2 + 1 therefore, we could just join the two linked list together!
# This ways, they still share the last tail nodes as below => Traverse both and find the shared one
# (*)
# A -> B -> (C) -> D -> E -> 1 -> 2 -> 3 -> (C) -> D -> E
# 1 -> 2 -> 3 -> (C) -> D -> E -> A -> B -> (C) -> D -> E
# How can we do this? When any pointer first find null, instead we next at other linked list head! 

# When do we stop? When both next head is null

# TIME: O(m + n)
# SPACE: 
def find_the_shared_node_linked_list_better (head_A: Node, head_B: Node) -> Node:
    traverse_A = head_A
    traverse_B = head_B
    
    # Notice that we stop when traverse_A = traverse_B
    # since even at the end the both of them will be None also

    # Imagine the end null is part of the linked list also
    while traverse_A != traverse_B:
        traverse_A = traverse_A.next if traverse_A else head_B
        traverse_B = traverse_B.next if traverse_B else head_A
    
    return traverse_A
