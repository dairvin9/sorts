# Quick sort. In python.

# Explanation: I wanted to see if I could write this from memory in python.

numbers = raw_input("Give me a list of numbers: ")
numbers = numbers.split()

parsed = []
for n in numbers:
    parsed.append(float(n))

numbers = parsed
    
def my_qsort(numbers):
    if len(numbers) == 0:
        return []
    
    lesser = []
    greater = []
    
    pivot = numbers[0]
    
    if len(numbers) == 1:
        return numbers
    
    # The first element in the list is the pivot number
    for n in numbers[1:]:
        if n <= pivot:
            lesser.append(n)
            
        if n > pivot:
             greater.append(n)
        
    if len(lesser) > 1: 
        lesser = my_qsort(lesser)
    if len(greater) > 1:
        greater = my_qsort(greater)
    
    lesser.append(pivot)

    return lesser + greater
    
print my_qsort(numbers)    
    