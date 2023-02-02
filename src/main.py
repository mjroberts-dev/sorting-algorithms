import seed
import algorithms.bubble
import algorithms.selection
import algorithms.insertion

data = seed.generateRandomArray(15)

print(data)
print("----" * len(data))

print(algorithms.bubble.sort(data))
print(algorithms.selection.sort(data))
print(algorithms.insertion.sort(data))