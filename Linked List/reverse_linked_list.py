from node import Node

# OBSERVATION:
# For example we need to reverse this list: 1 -> 2 -> 3
# First of all we need a pointer to know what node is currently being selected: cur_pnt
# Also, we need to know which node we need to point to: prv_pnt
# Now, if we make cur_pnt point to prev_pnt, then we lost the reference to the next node cur_pnt currently pointing at => We need another one ref the next node in the line also: nxt_pnt
# => In conclusion, we need one pointer represent the selected node, one represent what will that node will need to point to and one represent the existing next node of the selected node

# With these pointers, how do we proceeds?
# First iteration: prv = null -- cur = 1 -- nxt = 2 
# => 1 next point to null 
# => move prv = cur = 1 then cur = nxt = 2 then nxt = cur.next = 3 (using existing nxt.next)
# => here we can see the nxt we store earlier helps with the second logic
# => Result null <- 1 -- 2 --> 3 --> null
# Second iteration: prv = 1 -- cur = 2 -- nxt = 3
# => 2 next point to 1 
# => move prv = cur = 2 then cur = nxt = 3 then nxt = cur.next = null (using existing nxt.next)
# => Result null <- 1 <-- 2 -- 3 --> null
# Third iteration: prv = 1 -- cur = 2 -- nxt = 3
# => 3 next point to 2 
# => move prv = cur = 3 then cur = nxt = null 
# => Result null <- 1 <-- 2 <-- 3 
# => Stop when cur = null


# TIME: O(n)
# SPACE: O(1)
def reverse_linked_list (head: Node) -> Node:
    if (head.next == None): return head
    
    prv_pnt = None
    cur_pnt = head
    
    while cur_pnt != None:
        # Don't mess up this order
        nxt_pnt = cur_pnt.next
        cur_pnt.next = prv_pnt
        prv_pnt = cur_pnt
        cur_pnt = nxt_pnt
    
    return prv_pnt
    
    
# RECURSION VERSION
# The trick is understanding that recursion defers work until it hits the base case.
# => Imagine working from the base case up
# Usually the structure of a recursive function will be:
#   (1) Base check logic
#   (2) Recursive call
#   (3) Logic after recursive call return

# OBSERVATION: 
# For example, 1 --> 2 --> 3 --> null
# KEY: We need the new HEAD (which is the end of the original list) returned (2)
# KEY: Base case? If cur.next = null then return cur. What happen if the tree contain no element? cur = null => return cur => if cur or cur.next = null (1)
# What happen when recursive call return? (3) Now 2 --> 3. 3 is returned and we are at head == 2 level. 
# => head.next.next = head (which roughly translate to 3.next = 2) so 2 <--> 3
# => head.next = null (now remove the point from 2 to 3) so 2 --> 3

def recursive_reverse_linked_list (head: Node) -> Node:
    # Base case
    if head == None or head.next == None:
        return head

    # Recursive call
    new_head = recursive_reverse_linked_list(head.next) # transporting the new head to the start of the call stack 

    # Normal case
    head.next.next = head
    head.next = None
    return new_head # transporting the new head 