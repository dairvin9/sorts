# A Stack. In Python.

# stacks have push, pop, top, and is empty.

class Node:
    value = None
    prev = None
    
    def __init__(self, num):
        self.value = num
        
        
class Stack:
    
    top_node = None

    def push(self, node):
        if self.top_node is None:
            self.top_node = node
        else:
            node.prev = self.top_node
            self.top_node = node
    
    def pop(self):
        if self.top_node is None:
            return None
        old = self.top_node
        self.top_node = old.prev
        return old.value
        
    def top(self):
        if self.top_node is None:
            return None
        return self.top_node.value    
    
    def is_empty(self):
        return self.top_node is None
        
def testing():        
    s = Stack()

    a = Node(3)
    b = Node(4)
    c = Node(5)
    d = Node(6)
    e = Node(7)
    f = Node(8)
    g = Node(9)
    h = Node(10)
    j = Node(11)
    s.push(a)
    s.push(b)
    s.push(c)
    s.push(d)
    s.push(e)
    s.push(f)
    s.push(g)
    s.push(h)
    s.push(j)
    print s.is_empty()
    print s.pop()
    print s.pop()
    print s.pop()
    print s.pop()
    print s.pop()
    print s.pop()
    print s.top()
    print s.pop()
    print s.pop()
    print s.pop()
    print s.pop()
    print s.pop()
    print s.pop()
    print s.is_empty()        