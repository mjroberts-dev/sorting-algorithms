import seed
import algorithms.bubble
import algorithms.selection
import algorithms.insertion
import algorithms.quick

data = seed.generateRandomArray(15)

print(data)
print("----" * len(data))

print("Bubble:   ", algorithms.bubble.sort(data))
print("Selection:", algorithms.selection.sort(data))
print("Insertion:", algorithms.insertion.sort(data))
print("Quick:    ", algorithms.quick.sort(data))