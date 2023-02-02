
# Insertion Sort
#   + Simple
#   - Runtimes no different to Bubble Sort

# Best Runtime:     Ω(n)
# Avg. Runtime:     Θ(n²)
# Worst Runtime:    O(n²)

def sort(array):
    length = len(array) - 1
    # loop through all elements
    for x in range(0, length):
        cursor_index = x
        # check if next element is greater than cursor
        if array[cursor_index+1] > array[cursor_index]:
            # loop through left-hand side of the cursor
            for y in range(0, cursor_index+1):
                # reverse bubble sort
                if array[y] > array[y+1]:
                    array[y], array[y+1] = array[y+1], array[y]

    return array
