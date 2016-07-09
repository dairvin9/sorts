# Heap sort. In Python

numbers = raw_input("Give me a list of numbers: ")
numbers = numbers.split()

parsed = []
for n in numbers:
    parsed.append(float(n))

numbers = parsed

class Node:
    
    def __init__(self,num):
        self.value = num

    def __repr__(self):
        print self.value  
        
class Heap:
    pass 
    
def my_heap_sort(numbers):
    pass