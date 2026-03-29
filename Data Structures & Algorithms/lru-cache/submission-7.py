class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def remove_node(self, node):
        nxt = node.next
        prev = node.prev
        prev.next = nxt
        nxt.prev = prev

    def add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_node(node)

    def pop_tail(self):
        last_node = self.tail.prev
        self.remove_node(last_node)
        return last_node
    
    def get(self, key: int) -> int:
        node = self.cache.get(key)

        if not node:
            return -1

        self.move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)

        if not node:
            new_node = Node(key, value)

            if len(self.cache) >= self.capacity:
                tail = self.pop_tail()
                del self.cache[tail.key]

            self.cache[key] = new_node
            self.add_node(new_node)
        else:
            node.value = value
            self.move_to_head(node)





