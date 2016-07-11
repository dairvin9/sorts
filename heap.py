# Heap sort. In Python

numbers = raw_input("Give me a list of numbers: ")
numbers = numbers.split()

parsed = []
for n in numbers:
    parsed.append(float(n))

numbers = parsed

class Node:
    
    # default value
    value = None
    rchild = None
    lchild = None
    parent = None # Added for upheap
    
    def __init__(self,num):
        self.value = num

    def __repr__(self):
        return str(self.value)  
        
class Heap:

    root = None
    open_parent = None
    last = None
    
    def make_none(self):
        self = None
        

    # Go up until you realize you are in an lchild, then follow the rchilds. If you arent an lchild, you get to start a new row!
    def set_open_parent(self):
        current = self.open_parent
        if current.lchild is None or current.rchild is None:
            return
        while True:
            if current.parent is not None:
                if current.parent.lchild is current:
                    # Take rchild fork
                    current = current.parent.rchild
                else:
                    current = current.parent
            else:  # Start a new row in the heap!
                break
        while current.lchild is not None:
            current = current.lchild
        
        open_parent = current    
      
    def insert(self,node):
        if self.root is None:
            self.root = node
            self.open_parent = node # Update where to add to
            self.last = node
        else:
            if self.open_parent.lchild is not None:
                self.open_parent.lchild = node
                self.upheap(node)
            else:
                self.open_parent.rchild = node
                self.last = node
                self.upheap(node)
                self.set_open_parent()
                


    def remove_smallest_value(self):
        if self.root is None:
            return
        value = self.root.value
            
        self.root.value = self.last.value
        self.downheap()
        
        return value
            
        
    def upheap(self,node):
        # Current is new node in heap
        current = node
        while current.parent is not None:
            if current.value < current.parent.value:
                val = current.value
                current.value = current.parent.value
                current.parent.value = val
                current = current.parent
            else:
                break
        
            
        
    def downheap(self):
        current = self.root
        while current.rchild is not None or current.lchild is not None:
            if current.rchild is not None and current.lchild is not None:
                if current.lchild.value > current.rchild.value:
                    if current.value > current.rchild.value:
                        val = current.rchild.value
                        current.rchild.value = current.value
                        current.value = val
                        current = current.rchild
                    else:
                        break
                elif current.lchild.value < current.rchild.value:
                    if current.value > current.lchild.value:
                        val = current.lchild.value
                        current.lchild.value = current.value
                        current.value = val
                        current = current.lchild
                    else:
                        break
                else: # We are done!
                    break
            elif current.lchild is not None:
                if current.lchild.value < current.value:
                    val = current.lchild.value
                    current.lchild.value = current.value
                    current.value = val
                    current = current.lchild
            else:
                return

def my_heap_sort(numbers):
    h = Heap()
    for n in numbers:
        h.insert(Node(n))
    for n in numbers:
        print h.remove_smallest_value()
    
 
 
my_heap_sort(numbers)

""" Naive, inefficient Insert
    def insert(self, node):
        if self.root is None:
            self.root = node
        else:
            parent = self.root
            while True:
                if node.value >= parent.value:
                    if parent.rchild is None:
                        parent.rchild = node
                        break
                    else:
                        parent = parent.rchild
                        continue
                else:
                    if parent.lchild is None:
                        parent.lchild = node
                        break
                    else:
                        parent = parent.lchild
                        continue
"""      
    