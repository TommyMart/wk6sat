# Non primitive data types - hold/store multiple pieces of data

# Lists - Array (other languages) - collection of data - indexed - mutable (can be changed)
numbers = [13, 2, 5, 98, 56]
#           0  1  2   3   4    index

print(numbers)
print(numbers[2])

numbers[2] = 10 
print(numbers)

numbers.append(42) # Appends to end
print(numbers)

numbers.insert(2, 16)
print(numbers)

numbers.pop()
print(numbers)

numbers.remove(98)
print(numbers)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

print(len(numbers))

# index, count (other uses)

# Tuple - collection of data - indexed - immutable (cannot be changed)

names = ("John", "Jane", "Mike", "Jane", "Jane") # parenthasis

# () - parenthesis
# {} - curly
# [] - square

print(names)
print(names[1])

# () tuple - cannot be changed ie calender, no append / pop / insert

print(len(names))
print(names.count("Jane"))

print(names.count)