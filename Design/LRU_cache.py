# Design a LRU cache
# What is a LRU Cache?
# LRU means Least Recently Used cache that support the following operations:
#   Initialize an LRU cache with a specific size
#   get(key : int) => Return the value associate with a key. Return -1 if the key does not exist. 
#   put(key : int, value : int) => Add a key and value to the cache.
#       If adding it exceed the maximum capacity of the cache then remove the oldest element of the cache.
#       If the key exist then replace the value AND move them to the last (latest position) 
# CONSTRAINT: All keys and values are positive numbers
# CONSTRAINT: Cache capacity is positive number

# OBSERVATION: How to quickly get the value? What is the fastest way to access a value by key?
# => Use Hash Map
# => There are 2 operations we need to handle here:
#       (1) Check if the key exist:
#           If not return -1 
#           (2) If yes :
#               Remove it
#               Change it position to last
#               Return the value associate with that key

# OBSERVATION: For the put feature, we need to handles:
#       (3) If the key exist:
#           We need to update its value 
#       If the key does not, add it to the cache
#           (4) If the new key exceed the capacity of the cache 
#               Remove the oldest one
#       Change it new position to last
#          
# What data structure we can use to know the order of the data AND can remove the end and the beginning elements at that order?
# => Doubly Linked List

# Definition for LRU_cache design
class Doubly_Node:
    def __init__(self, key: int, value: int): 
        self.value = value
        self.key = key
        self.nxt = self.prv = None

# TIME: get O(1) put O(1)
# SPACE: O(2n) = O(n)
class LRU_cache:
    def __init__ (self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}
        
        # Dummy nodes to access oldest or newest
        # (newest) <-> (actual newest) <-> ... <-> (actual oldest) <-> (oldest)
        self.oldest = Doubly_Node(-1, -1)
        self.newest = Doubly_Node(-1, -1)
        self.newest.nxt = self.oldest
        self.newest.prv = None
        self.oldest.prv = self.newest
        self.oldest.nxt = None
    
    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1
        node = self.hash_map[key]
        self.remove_node(node)
        self.add_to_front(node)
        return node.value
        
    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            node = self.hash_map[key]
            node.value = value
            self.remove_node(node)
            self.add_to_front(node)
            return
        node = Doubly_Node(key, value)
        self.hash_map[key] = node
        self.add_to_front(node)
        if len(self.hash_map) > self.capacity:
            del self.hash_map[self.oldest.prv.key]
            self.remove_node(self.oldest.prv)
    
    def remove_node(self, node: Doubly_Node):
        node.prv.nxt = node.nxt
        node.nxt.prv = node.prv

        node.prv = None
        node.nxt = None
    
    def add_to_front(self, node: Doubly_Node):
        node.nxt = self.newest.nxt 
        self.newest.nxt.prv = node
        self.newest.nxt = node
        node.prv = self.newest