# Merge sort. In python.

# Explanation: I wanted to see if I could write this from memory in python.

numbers = raw_input("Give me a list of numbers: ")
numbers = numbers.split()

parsed = []
for n in numbers:
    parsed.append(float(n))

numbers = parsed

# Merge sort: halfs the list until there is one element adn then combines the lists one after another

def my_splitter(numbers):
    if len(numbers) > 1:
        # Python 2 rounds it for you! (Bug/Feature)
        half = len(numbers) / 2 
        list1 = numbers[:half]
        list2 = numbers[half:]
        
        list1 = my_splitter(list1)
        list2 = my_splitter(list2)
        return my_merger(list1,list2)
        
    if len(numbers) == 1 or len(numbers) == 0:
        return numbers        
        
def my_merger(list1, list2):
    merged = []
    while True:
        if list1[0] < list2[0]:
            merged.append(list1.pop(0))
            if len(list1) == 0:
                return merged + list2
        else:
            merged.append(list2.pop(0))
            if len(list2) == 0:
                return merged + list1
       
print my_splitter(numbers)        