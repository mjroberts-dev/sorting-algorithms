
# Selection Sort - O(n²)
#   + Simple
#   - Very Inefficient

# Best Runtime:     Ω(n²)
# Avg. Runtime:     Θ(n²)
# Worst Runtime:    O(n²)

def sort(array):
    length = len(array) - 1
    # loop through all elements
    for x in range(0, length):
        min_index = x
        # find the next minimum element
        for y in range(x+1, length):
            if array[min_index] > array[y]:
                min_index = y
            
        # swap elements
        array[x], array[min_index] = array[min_index], array[x]
    return array
