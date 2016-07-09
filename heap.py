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
    
    def __init__(self,num):
        self.value = num

    def __repr__(self):
        return str(self.value)  
        
class Heap:

    root = None
    
    def make_none(self):
        self = None

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
            
    def remove_smallest_value(self):
        if self.root is None:
            return
        parent = self.root
        if parent.lchild is None:
            print parent.value
            self.root = self.root.rchild
            return 
            
        while parent.lchild is not None:
            if parent.lchild.lchild is not None:
                parent = parent.lchild
            else:
                break
                
        print parent.lchild.value
        parent.lchild = parent.lchild.rchild
        

def my_heap_sort(numbers):
    h = Heap()
    for n in numbers:
        h.insert(Node(n))
    for n in numbers:
        h.remove_smallest_value()
    
 
 
my_heap_sort(numbers)