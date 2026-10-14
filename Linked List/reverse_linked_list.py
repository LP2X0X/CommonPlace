class Node:
    def __init__(self, value: int, next: Node):
        self.value = value
        self.next = next

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

def reverse_linked_list (start: Node) -> Node:
    if (start.next == None): return start
    
    prv_pnt = None
    cur_pnt = start
    
    while cur_pnt != None:
        # Don't mess up this order
        nxt_pnt = cur_pnt.next
        cur_pnt.next = prv_pnt
        prv_pnt = cur_pnt
        cur_pnt = nxt_pnt
    
    return prv_pnt
    