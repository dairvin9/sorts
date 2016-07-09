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

    def insert(self, node):
        if self.root is None:
            self.root = node
        else:
            parent = self.root
            while True:
                if node.value <= parent.value:
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
            
    def remove_smallest_value():
        pass #while
    
def my_heap_sort(numbers):
    pass
    
    
a = Node(5)
b = Node(5)
h = Heap()
h.insert(a) 
h.insert(b)