import seed
import algorithms.bubble
import algorithms.selection
import algorithms.insertion
import algorithms.quick
import algorithms.merge


data = seed.generateRandomArray(15)

print(data)
print("----" * len(data))

print("Bubble:   ", algorithms.bubble.sort(data.copy()))
print("Selection:", algorithms.selection.sort(data.copy()))
print("Insertion:", algorithms.insertion.sort(data.copy()))
print("Quick:    ", algorithms.quick.sort(data.copy()))
print("Merge:    ", algorithms.merge.sort(data.copy()))
