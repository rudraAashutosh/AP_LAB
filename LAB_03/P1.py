# Q.1 Design and implement a data structure for the Least Recently Used (LRU) cache It should support the following 
# operations get and put.
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, 
# it should invalidate the least recently used item before inserting a new item. The cache is always initialized with 
# positive capacity
# class Node:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.prev = None
#         self.next = None

# class LRUCache:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache = {}
#         self.head = Node(0, 0)
#         self.tail = Node(0, 0)
#         self.head.next = self.tail
#         self.tail.prev = self.head

#     def _remove(self, node):
#         prev = node.prev
#         next = node.next
#         prev.next = next
#         next.prev = prev

#     def _add(self, node):
#         prev = self.tail.prev
#         prev.next = node
#         self.tail.prev = node
#         node.prev = prev
#         node.next = self.tail

#     def get(self, key: int) -> int:
#         if key in self.cache:
#             node = self.cache[key]
#             self._remove(node)
#             self._add(node)
#             return node.value
#         return -1

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self._remove(self.cache[key])
#         node = Node(key, value)
#         self._add(node)
#         self.cache[key] = node
#         if len(self.cache) > self.capacity:
#             lru = self.head.next
#             self._remove(lru)
#             del self.cache[lru.key]

cache = {}
size = 4

def isfull():
    if(len(cache) == size):
        return True
    else:
        return False
def remove():
    least = float('inf')
    character = ''
    for i in cache:
        if(cache[i]<least):
            least = cache[i]
            character = i
    cache.pop(character)

def add(c):
    if(isfull() and c not in cache):
        remove()
    cache[c] = cache.get(c,0)+1

def getkey(c):
    ans = cache.get(c,-1)
    return ans

def print_cache():
    print(cache)

while True:
    print("enter 1 to add key\n")
    print("enter 2 to get key value\n")
    print("enter 0 to exit\n")
    choice = int(input("enter the choice"))
    if(choice == 1):
        character = str(input())
        add(character)
        print_cache()
    elif(choice == 2):
        character = str(input())
        print("the value is "+str(getkey(character)))
        print_cache()
    else:
        exit()