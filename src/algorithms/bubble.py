
# Bubble Sort
#   + Simple
#   - Inefficient

# Best Runtime:     Ω(n)
# Avg. Runtime:     Θ(n²)
# Worst Runtime:    O(n²)

def sort(array):
    length = len(array) - 1
    # loop through all elements
    for x in range(0, length):
        # loop through unsorted elements
        for y in range(0, length-x):
            if array[y] > array[y+1]:
                # swap elements if next element is higher
                array[y], array[y+1] = array[y+1], array[y]
    return array
