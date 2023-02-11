
# Quick Sort

# - Unstable

# Best Runtime:     Ω(nlogn)
# Avg. Runtime:     Θ(nlogn)
# Worst Runtime:    O(n²)


def partition(array, start, end):
    pivot = start
    for i in range(start+1, end+1):
        if array[i] <= array[start]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[start] = array[start], array[pivot]
    return pivot



def sort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1
    def quicksort(array, start, end):
        if start >= end:
            return
        pivot = partition(array, start, end)
        quicksort(array, start, pivot-1)
        quicksort(array, pivot+1, end)
        return array
    return quicksort(array, start, end)