# A Queue. In Python.

# queues have enqueue, dequeue, front and is empty.
# this stack is built off a singly linked list

class Node:
    value = None
    prev = None
    
    def __init__(self, num):
        self.value = num
        
        
class Queue:
    
    front_node = None
    back_node = None

    def enqueue(self, node):
        if self.front_node is None:
            self.front_node = node
            self.back_node = node
        else:
            self.back_node.prev = node
            self.back_node = node
    
    def dequeue(self):
        if self.front_node is None:
            return None
        old = self.front_node
        self.front_node = old.prev
        return old.value
        
    def front(self):
        if self.front_node is None:
            return None
        return self.front_node.value    
    
    def is_empty(self):
        return self.front_node is None
        
def testing():        
    s = Queue()

    a = Node(3)
    b = Node(4)
    c = Node(5)
    d = Node(6)
    e = Node(7)
    f = Node(8)
    g = Node(9)
    h = Node(10)
    j = Node(11)
    s.enqueue(a)
    s.enqueue(b)
    s.enqueue(c)
    s.enqueue(d)
    s.enqueue(e)
    s.enqueue(f)
    s.enqueue(g)
    s.enqueue(h)
    s.enqueue(j)
    print s.is_empty()
    print s.dequeue()
    print s.dequeue()
    print s.dequeue()
    print s.dequeue()
    print s.dequeue()
    print s.dequeue()
    print s.front()
    print s.dequeue()
    print s.dequeue()
    print s.dequeue()
    print s.dequeue()
    print s.dequeue()
    print s.dequeue()
    print s.is_empty()        
    
    
testing()    